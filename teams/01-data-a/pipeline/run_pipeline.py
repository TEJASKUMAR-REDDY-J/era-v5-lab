"""One command for Data A's pipeline: clean -> overlap -> dedup -> apply the remove list -> F2 -> survivor loss.

  python -I teams/01-data-a/pipeline/run_pipeline.py --config teams/01-data-a/pipeline/pipeline.json [--from STAGE] [--to STAGE]

It runs or adopts each stage in order, checks that each stage's counts follow from the one before, and writes
<out>/<run_id>/pipeline_manifest.json. It never reimplements a stage: clean (#244), overlap and dedup (#255) and F2 (run_f2.py)
are the team's scripts, called as they are; apply_dedup.py and survivor_loss.py are in this folder.

STAGES
======
  clean          cleaned parts: <output>/train/**.parquet and <output>/heldout/**.parquet          (TSAI job, #244)
  overlap        overlap_summary.json, overlap_matches.csv, overlap_docs.parquet                    (TSAI job, #255)
  dedup          remove_list.csv, dedup_groups.csv, dedup_summary.json                              (TSAI job, #255)
  apply          apply_dedup.py on clean's output with dedup's remove list  -> <run>/deduped
  f2             run_f2.py once per split on <run>/deduped/<split>            -> <run>/final/<split>
  survivor_loss  survivor_loss.py on dedup_groups.csv and F2's reports        -> <run>/report

clean, overlap and dedup take "mode": "adopt" (TSAI ran the job; "output" names the folder it returned) or "mode": "run"
("command": the script and its arguments, run with this Python from the repository root; "output": where that script writes).
apply, f2 and survivor_loss always run. f2 takes "script" (default teams/01-data-a/spec_v1/run_f2.py).

CONFIG (JSON; keys starting with "_" are comments; paths relative to the repository root, or absolute)
=====================================================================================================
  run_id   name of this run; out    folder for runs (default out/pipeline); stages  as above

CHECKS (any failure stops the run; exit code 1)
==============================================
  - each stage's expected files exist; a "run" stage's script exits 0
  - overlap's documents_all = the cleaned rows; dedup's removed = the remove list's rows; dedup removed no held-out doc
  - apply's rows = the cleaned rows and apply's removed = the remove list's rows (apply_dedup.py also checks each row)
  - F2's rows = apply's kept rows, F2's kept + dropped + errors = its rows, F2 reported no errors
  - with --from, every earlier stage's output must still have the digest the manifest recorded for it: an adopted
    folder changed after it was recorded stops the run

MANIFEST
========
<out>/<run_id>/pipeline_manifest.json: the git commit, Python and pyarrow versions; per stage its mode, command, the
script's sha256, its output folder's digest (sha256 over the sorted relative paths and sha256 of every file), file count,
counts and seconds; the checks; and totals (cleaned, removed by dedup, dropped by F2, final). IDs, counts and hashes only.
"""
import sys
sys.dont_write_bytecode = True

import argparse, hashlib, json, platform, subprocess, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
STAGES = ("clean", "overlap", "dedup", "apply", "f2", "survivor_loss")
EXTERNAL = ("clean", "overlap", "dedup")
NEEDED = {"overlap": ("overlap_summary.json", "overlap_matches.csv", "overlap_docs.parquet"),
          "dedup": ("remove_list.csv", "dedup_groups.csv", "dedup_summary.json")}
DEFAULT_F2 = "teams/01-data-a/spec_v1/run_f2.py"
SPLITS = ("train", "heldout")


class Stop(Exception):
    """A check failed: the message says which and where."""


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def digest(folder):
    """(sha256 over every file's relative path and sha256, file count). Order-independent of the file system."""
    files = sorted(p for p in Path(folder).rglob("*") if p.is_file() and not p.name.endswith(".tmp"))
    h = hashlib.sha256()
    for p in files:
        h.update(f"{p.relative_to(folder).as_posix()}\t{sha256(p)}\n".encode("utf-8"))
    return h.hexdigest(), len(files)


def path(p):
    p = Path(p)
    return p if p.is_absolute() else REPO / p


def run_script(script, args, stage):
    cmd = [sys.executable, "-I", str(path(script)), *map(str, args)]
    p = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
    if p.returncode != 0:
        tail = (p.stderr or p.stdout).strip().splitlines()[-5:]
        raise Stop(f"{stage}: {Path(script).name} failed with exit code {p.returncode}: " + " | ".join(tail))
    return p


def parquet_rows(folder):
    import pyarrow.parquet as pq
    by_split = {}
    for split in SPLITS:
        if (folder / split).is_dir():
            by_split[split] = sum(pq.ParquetFile(f).metadata.num_rows for f in sorted((folder / split).rglob("*.parquet")))
    if not by_split:
        raise Stop(f"clean: {folder} has no train/ or heldout/ folder")
    return {"rows": sum(by_split.values()), "by_split": by_split}


def csv_rows(file):
    with open(file, encoding="utf-8", newline="") as f:
        return max(sum(1 for _ in f) - 1, 0)


def load_json(file):
    return json.loads(Path(file).read_text(encoding="utf-8"))


class Run:
    def __init__(self, cfg_path):
        self.cfg_path = Path(cfg_path)
        self.cfg = load_json(self.cfg_path)
        if not self.cfg.get("run_id"):
            raise Stop(f"{cfg_path}: run_id is missing")
        self.dir = path(self.cfg.get("out", "out/pipeline")) / self.cfg["run_id"]
        self.manifest_path = self.dir / "pipeline_manifest.json"
        self.stages = self.cfg.get("stages", {})
        self.done, self.checks = {}, []

    def output(self, stage):
        if stage in EXTERNAL:
            if "output" not in self.stages.get(stage, {}):
                raise Stop(f"config: stages.{stage}.output is missing")
            return path(self.stages[stage]["output"])
        return self.dir / {"apply": "deduped", "f2": "final", "survivor_loss": "report"}[stage]

    def check(self, name, ok, detail):
        self.checks.append({"check": name, "ok": bool(ok), "detail": detail})
        if not ok:
            raise Stop(f"check failed: {name}: {detail}")

    # --- the stages -------------------------------------------------------------------------------------------------
    def stage_external(self, stage):
        spec = self.stages.get(stage, {})
        mode = spec.get("mode", "adopt")
        if mode not in ("adopt", "run"):
            raise Stop(f"config: stages.{stage}.mode is {mode!r}, expected adopt or run")
        command = None
        if mode == "run":
            command = spec.get("command") or []
            if not command:
                raise Stop(f"config: stages.{stage}.command is missing for mode run")
            run_script(command[0], command[1:], stage)
        out = self.output(stage)
        for name in NEEDED.get(stage, ()):
            if not (out / name).is_file():
                raise Stop(f"{stage}: {out} has no {name}")
        if stage == "clean":
            counts = parquet_rows(out)
        elif stage == "overlap":
            s = load_json(out / "overlap_summary.json")
            self.check("overlap finished", s.get("status") == "complete", f"status {s.get('status')!r}")
            counts = {"documents_all": s.get("documents_all")}
            self.check("overlap read every cleaned row", counts["documents_all"] == self.done["clean"]["counts"]["rows"],
                       f"overlap documents_all {counts['documents_all']}, cleaned rows {self.done['clean']['counts']['rows']}")
        else:
            s = load_json(out / "dedup_summary.json")
            counts = {"remove_list_rows": csv_rows(out / "remove_list.csv"), "removed": s.get("removed"),
                      "heldout_removed": s.get("heldout_removed"),
                      "groups": len({r.split(",", 1)[0] for r in (out / "dedup_groups.csv").read_text(encoding="utf-8").splitlines()[1:] if r})}
            self.check("dedup summary matches its remove list", counts["removed"] == counts["remove_list_rows"],
                       f"summary removed {counts['removed']}, remove_list.csv rows {counts['remove_list_rows']}")
            self.check("dedup removed no held-out doc", counts["heldout_removed"] == 0,
                       f"heldout_removed {counts['heldout_removed']} (rule 0)")
        return {"mode": mode, "command": command, "code_sha256": sha256(path(command[0])) if command else None,
                "output": self.stages[stage]["output"], "counts": counts}

    def stage_apply(self):
        import apply_dedup
        out = self.output("apply")
        try:
            s = apply_dedup.apply(self.output("clean"), self.output("dedup") / "remove_list.csv", out)
        except apply_dedup.Stop as e:
            raise Stop(f"apply: {e}")
        counts = dict(s["totals"])
        self.check("apply read every cleaned row", counts["rows"] == self.done["clean"]["counts"]["rows"],
                   f"apply rows {counts['rows']}, cleaned rows {self.done['clean']['counts']['rows']}")
        self.check("apply removed the remove list", counts["removed"] == self.done["dedup"]["counts"]["remove_list_rows"],
                   f"apply removed {counts['removed']}, remove list {self.done['dedup']['counts']['remove_list_rows']}")
        return {"mode": "run", "command": ["teams/01-data-a/pipeline/apply_dedup.py"],
                "code_sha256": s["code_sha256"], "output": out.relative_to(self.dir).as_posix(), "counts": counts}

    def stage_f2(self):
        script = self.stages.get("f2", {}).get("script", DEFAULT_F2)
        if not path(script).is_file():
            raise Stop(f"f2: {script} not found (run_f2.py is in PR #35; set stages.f2.script to its path)")
        src, out = self.output("apply"), self.output("f2")
        totals = {"rows": 0, "kept": 0, "dropped_by_f2": 0, "errors": 0}
        sets = set()
        for split in SPLITS:
            if not (src / split).is_dir():
                continue
            run_script(script, ["--inputs", src / split, "--out", out / split], "f2")
            s = load_json(out / split / "f2_summary.json")
            sets.add(s.get("set_sha256"))
            for k in totals:
                totals[k] += s.get(k, 0)
        self.check("F2 used one fingerprint set", len(sets) == 1, f"set_sha256 values {sorted(map(str, sets))}")
        self.check("F2 read every deduplicated row", totals["rows"] == self.done["apply"]["counts"]["kept"],
                   f"F2 rows {totals['rows']}, apply kept {self.done['apply']['counts']['kept']}")
        self.check("F2 counts add up", totals["kept"] + totals["dropped_by_f2"] + totals["errors"] == totals["rows"],
                   f"{totals}")
        self.check("F2 reported no errors", totals["errors"] == 0, f"{totals['errors']} docs raised during the check")
        return {"mode": "run", "command": [script, "--inputs", "<run>/deduped/<split>", "--out", "<run>/final/<split>"],
                "code_sha256": sha256(path(script)), "output": "final", "set_sha256": sets.pop(), "counts": totals}

    def stage_survivor_loss(self):
        import survivor_loss
        out = self.output("survivor_loss")
        try:
            s = survivor_loss.report(self.output("dedup") / "dedup_groups.csv", self.output("f2"), out)
        except survivor_loss.Stop as e:
            raise Stop(f"survivor_loss: {e}")
        return {"mode": "run", "command": ["teams/01-data-a/pipeline/survivor_loss.py"], "code_sha256": s["code_sha256"],
                "output": "report", "counts": {**s["groups"], "survivors_dropped_by_f2": s["survivors_dropped_by_f2"]}}

    # --- the run ----------------------------------------------------------------------------------------------------
    def execute(self, start=None, to=None):
        start, to = start or STAGES[0], to or STAGES[-1]
        for s in (start, to):
            if s not in STAGES:
                raise Stop(f"unknown stage {s!r}; stages are {', '.join(STAGES)}")
        if STAGES.index(start) > STAGES.index(to):
            raise Stop(f"--from {start} comes after --to {to}")
        old = {s["stage"]: s for s in load_json(self.manifest_path)["stages"]} if self.manifest_path.is_file() else {}
        sys.path.insert(0, str(HERE))
        for stage in STAGES[: STAGES.index(to) + 1]:
            out = self.output(stage)
            if STAGES.index(stage) < STAGES.index(start):
                if stage not in old:
                    raise Stop(f"--from {start}: stage {stage} has no record in {self.manifest_path}; run it first")
                if not out.exists() or digest(out)[0] != old[stage]["digest"]:
                    raise Stop(f"{stage}: {out} changed after the manifest recorded it; rerun from {stage}")
                self.done[stage] = old[stage]
                continue
            t0 = time.time()
            rec = self.stage_external(stage) if stage in EXTERNAL else getattr(self, f"stage_{stage}")()
            rec["digest"], rec["files"] = digest(out)
            self.done[stage] = {"stage": stage, **rec, "seconds": round(time.time() - t0, 1)}
            self.write()
            print(f"{stage}: {json.dumps(self.done[stage]['counts'])}", file=sys.stderr, flush=True)
        return self.write()

    def write(self):
        c = {s: self.done[s]["counts"] for s in self.done}
        totals = {}
        if "clean" in c:
            totals["cleaned"] = c["clean"]["rows"]
        if "apply" in c:
            totals["removed_by_dedup"] = c["apply"]["removed"]
        if "f2" in c:
            totals["dropped_by_f2"] = c["f2"]["dropped_by_f2"]
            totals["final"] = c["f2"]["kept"]
        manifest = {"tool": "run_pipeline.py", "run_id": self.cfg["run_id"], "config": self.cfg,
                    "code_sha256": sha256(Path(__file__)), "git_commit": git_commit(),
                    "python": platform.python_version(), "pyarrow": pyarrow_version(),
                    "stages": [self.done[s] for s in STAGES if s in self.done], "checks": self.checks, "totals": totals}
        self.dir.mkdir(parents=True, exist_ok=True)
        tmp = self.manifest_path.with_name(self.manifest_path.name + ".tmp")
        tmp.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n")
        tmp.replace(self.manifest_path)
        return manifest


def git_commit():
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO, capture_output=True, text=True).stdout.strip() or None
    except OSError:
        return None


def pyarrow_version():
    try:
        import pyarrow
        return pyarrow.__version__
    except ImportError:
        return None


def run(config, start=None, to=None):
    return Run(config).execute(start, to)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", type=Path, required=True, help="pipeline JSON config")
    ap.add_argument("--from", dest="start", choices=STAGES, help="first stage to run (earlier ones must be recorded)")
    ap.add_argument("--to", choices=STAGES, help="last stage to run")
    args = ap.parse_args()
    try:
        m = run(args.config, args.start, args.to)
    except Stop as e:
        sys.exit(f"run_pipeline: {e}")
    print(json.dumps(m["totals"]))


if __name__ == "__main__":
    main()
