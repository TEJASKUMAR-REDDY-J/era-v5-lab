"""Tests for run_pipeline.py: the whole chain on synthetic data, with clean, overlap and dedup adopted (as when TSAI ran
them) and apply, F2 (a stand-in, fake_run_f2.py) and survivor_loss run by the runner.

  python -m pytest teams/01-data-a/pipeline/tests -q
"""
import csv
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
import pyarrow.parquet as pq

from conftest import HEADER, PIPELINE
import run_pipeline as rp

FAKE_F2 = Path(__file__).resolve().parent / "fake_run_f2.py"
GROUP_HEADER = ["group_id", "group_size", "priority_rule", "role", "pack_id", "split", "part", "row_in_part", "doc_id"]


def write_csv(path, header, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


@pytest.fixture
def tsai_outputs(tmp_path, cleaned):
    """What TSAI's overlap and dedup jobs would return for the conftest parts (13 docs)."""
    overlap = tmp_path / "overlap"
    overlap.mkdir()
    for name in ("overlap_matches.csv", "overlap_docs.parquet"):
        (overlap / name).write_bytes(b"stand-in")
    (overlap / "overlap_summary.json").write_text(json.dumps({"status": "complete", "documents_all": 13}), encoding="utf-8")
    dedup = tmp_path / "dedup"
    write_csv(dedup / "remove_list.csv", HEADER, [["code-go", "train", "code-go/part-00001.parquet", 0, "g0"],
                                                  ["en-dclm", "train", "en-dclm/part-00000.parquet", 2, "e2"]])
    write_csv(dedup / "dedup_groups.csv", GROUP_HEADER, [
        [1, 2, "pack_order", "survivor", "code-go", "train", "code-go/part-00000.parquet", 0, "g0"],
        [1, 2, "pack_order", "removed", "code-go", "train", "code-go/part-00001.parquet", 0, "g0"],
        [2, 3, "heldout_first", "survivor", "code-go", "heldout", "code-go/part-00000.parquet", 0, "h0"],
        [2, 3, "heldout_first", "survivor", "code-go", "heldout", "code-go/part-00000.parquet", 1, "h1"],
        [2, 3, "heldout_first", "removed", "en-dclm", "train", "en-dclm/part-00000.parquet", 2, "e2"]])
    (dedup / "dedup_summary.json").write_text(json.dumps({"removed": 2, "heldout_removed": 0}), encoding="utf-8")
    return {"cleaned": cleaned, "overlap": overlap, "dedup": dedup}


@pytest.fixture
def config(tmp_path, tsai_outputs, monkeypatch):
    monkeypatch.setenv("FAKE_F2_DROP", "g0,h1")
    cfg = {"run_id": "test-run", "out": str(tmp_path / "runs"),
           "stages": {"clean": {"mode": "adopt", "output": str(tsai_outputs["cleaned"])},
                      "overlap": {"mode": "adopt", "output": str(tsai_outputs["overlap"])},
                      "dedup": {"mode": "adopt", "output": str(tsai_outputs["dedup"])},
                      "f2": {"script": str(FAKE_F2)}}}
    path = tmp_path / "pipeline.json"
    path.write_text(json.dumps(cfg), encoding="utf-8")
    return path


def test_full_chain(tmp_path, config):
    m = rp.run(config)
    run = tmp_path / "runs" / "test-run"
    assert [s["stage"] for s in m["stages"]] == list(rp.STAGES)
    c = {s["stage"]: s["counts"] for s in m["stages"]}
    assert c["clean"]["rows"] == 13 and c["overlap"]["documents_all"] == 13 and c["dedup"]["remove_list_rows"] == 2
    assert (c["apply"]["rows"], c["apply"]["removed"], c["apply"]["kept"]) == (13, 2, 11)
    assert (c["f2"]["rows"], c["f2"]["dropped_by_f2"], c["f2"]["kept"]) == (11, 2, 9)
    assert c["survivor_loss"]["lost"] == 1 and c["survivor_loss"]["partly_hit"] == 1
    assert m["totals"] == {"cleaned": 13, "removed_by_dedup": 2, "dropped_by_f2": 2, "final": 9}
    assert all(ch["ok"] for ch in m["checks"])
    final_ids = sorted(d for f in (run / "final").rglob("*.parquet") for d in pq.read_table(f).column("doc_id").to_pylist())
    assert final_ids == sorted(["g1", "g2", "g3", "g4", "g5", "g6", "e0", "e1", "h0"])
    on_disk = json.loads((run / "pipeline_manifest.json").read_text(encoding="utf-8"))
    assert on_disk["totals"] == m["totals"] and "synthetic text" not in json.dumps(on_disk)


def test_adopted_output_changed_after_recording_stops(tmp_path, config, tsai_outputs):
    rp.run(config, to="apply")
    with (tsai_outputs["dedup"] / "remove_list.csv").open("a", encoding="utf-8") as f:
        f.write("en-dclm,train,en-dclm/part-00000.parquet,1,e1\n")
    with pytest.raises(rp.Stop, match="changed"):
        rp.run(config, start="f2")


def test_from_and_to(tmp_path, config):
    m = rp.run(config, to="apply")
    assert [s["stage"] for s in m["stages"]] == ["clean", "overlap", "dedup", "apply"]
    m = rp.run(config, start="f2")
    assert [s["stage"] for s in m["stages"]] == list(rp.STAGES)
    assert m["totals"]["final"] == 9


def test_from_a_stage_whose_input_was_never_run_stops(config):
    with pytest.raises(rp.Stop, match="no record .* run it first"):
        rp.run(config, start="f2")


def test_count_mismatch_stops(tmp_path, config, tsai_outputs):
    (tsai_outputs["overlap"] / "overlap_summary.json").write_text(json.dumps({"status": "complete", "documents_all": 12}),
                                                                  encoding="utf-8")
    with pytest.raises(rp.Stop, match="overlap"):
        rp.run(config)


def test_dedup_removing_heldout_stops(tmp_path, config, tsai_outputs):
    (tsai_outputs["dedup"] / "dedup_summary.json").write_text(json.dumps({"removed": 2, "heldout_removed": 1}),
                                                              encoding="utf-8")
    with pytest.raises(rp.Stop, match="held-out"):
        rp.run(config)


def test_run_mode_calls_the_script_and_stops_on_failure(tmp_path, config):
    cfg = json.loads(config.read_text(encoding="utf-8"))
    bad = tmp_path / "bad_overlap.py"
    bad.write_text("import sys; sys.exit(3)\n", encoding="utf-8")
    cfg["stages"]["overlap"] = {"mode": "run", "output": cfg["stages"]["overlap"]["output"], "command": [str(bad)]}
    config.write_text(json.dumps(cfg), encoding="utf-8")
    with pytest.raises(rp.Stop, match="exit code 3"):
        rp.run(config)


def test_cli(tmp_path, config):
    env = {**os.environ, "FAKE_F2_DROP": "g0,h1"}
    p = subprocess.run([sys.executable, "-I", str(PIPELINE / "run_pipeline.py"), "--config", str(config)],
                       capture_output=True, text=True, env=env)
    assert p.returncode == 0, p.stderr
    assert json.loads(p.stdout.strip().splitlines()[-1])["final"] == 9
