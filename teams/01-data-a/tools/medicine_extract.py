"""Medicine extractor: turn one medicine.md into a rules file that harm_test.py can run.

Usage:
    python -I medicine_extract.py <medicine.md> [--out <rules.py>]

By default the output goes to teams/01-data-a/rules/<pack_id>/<handle>.py, taken from the path
diagnosis/submissions/<pack_id>/<handle>/medicine.md. (Do not write into the submissions folder: pr-guard allows
only labels.csv and medicine.md there.) For any other path, give --out.

The medicine.md is only read, never run. The steps:
  1. Each "**Disease:** <code>" line starts a medicine section. A section ends at the next one, or at an
     "Appendix" heading.
  2. Every ```python block in the file is read with ast:
       code      defines a function (or a RULES dict). It goes into the rules file as it is.
       support   only imports and UPPER_CASE constants. It goes in too, inside try/except.
       fragment  anything else (a code line that needs a variable from elsewhere, a syntax error). Left out.
  3. For each disease code the rule is the first of:
       - the RULES dict entry for that code
       - a function named cure_<code> (for example cure_b3)
       - the only public function (no leading underscore) in that section
     Anything else is reported, and nothing is guessed.
  4. The rules file ends with RULES = {"B3": <function>, ...} and RULES_BY_ID = {"DB-B3-001": RULES["B3"], ...}.
  5. Each rule gets an ID: <team>-<code>-<number>. The team is DA for the Data A packs (English, code, math,
     science) and DB for every other pack (Indic, cadj-*). The number counts up for each team and code. The ID
     goes into rules/registry.json with the pack, the handle and the file. When you run the extractor again, a
     (pack, handle, code) that is already in the registry keeps its ID. A code that has gone from the
     medicine.md is marked "withdrawn" and its ID is never used again.
     A second section for the same code is a second rule with its own ID (the registry keeps its number n).
     The registry also keeps the action the annotator wrote on the "**Action:**" line (fix or drop).
  Then harm_test.py can find the rule by its ID alone:
       python -I harm_test.py --pack <pack.parquet> --gold <gold.csv> --rule DB-B3-001
  A path outside diagnosis/submissions/<pack_id>/<handle>/ has no pack or handle, so it gets no IDs.

Two medicines for one code: the RULES dict and the name cure_<code> can only point to one function, so they are
used for the first section of a code. A later section of the same code needs the only-function rule: put its
function in that section, and give it a name that no earlier rule uses.
"""
import argparse
import ast
import json
import os
import re
import sys
import textwrap
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))  # python -I does not put the script folder on the path
import harm_test  # noqa: E402  (one definition of the code-fence regex)

DISEASE = re.compile(r"\*\*Disease:?\*\*:?[ \t]*`?([A-H][1-9])\b")
APPENDIX = re.compile(r"^#{1,6}[^\n]*appendix", re.I | re.M)
CONST_NAME = re.compile(r"^[A-Z][A-Z0-9_]*$")
ACTION = re.compile(r"\*\*Action:?\*\*:?[ \t]*([^\n]*)")
ACTION_WORD = re.compile(r"\b(fix|drop)\b", re.I)
DEFAULT_REGISTRY = HERE.parent / "rules" / "registry.json"
# The packs Data A owns (English, code, math, science). Data B owns the rest (Indic and cadj-*).
DATA_A_PACKS = frozenset({
    "code-cpp", "code-go", "code-java", "code-js-ts", "code-python", "code-rust",
    "en-dclm", "en-fineweb-edu", "en-nemotroncc", "en-nemotroncc-synth",
    "math-finemath", "math-megamath", "sci-finepdfs",
})


class Block:
    def __init__(self, index, text, pos):
        self.index, self.text, self.pos = index, text, pos
        self.section = None   # index into the sections list, or None
        self.kind = "fragment"
        self.funcs = []       # names of functions defined at the top level of the block
        self.rules_map = {}   # code -> function name (None if the RULES value is not a plain name)
        self._analyse()

    def _analyse(self):
        try:
            tree = ast.parse(self.text)
        except SyntaxError:
            self.kind = "syntax error"
            return
        defining, support_only = False, True
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                self.funcs.append(node.name)
                defining = True
            elif isinstance(node, ast.ClassDef):
                defining = True
            elif isinstance(node, ast.Assign) and all(isinstance(t, ast.Name) for t in node.targets):
                names = [t.id for t in node.targets]
                if isinstance(node.value, ast.Lambda):
                    self.funcs.extend(names)
                    defining = True
                elif names == ["RULES"] and isinstance(node.value, ast.Dict):
                    defining = True
                    for k, v in zip(node.value.keys, node.value.values):
                        if isinstance(k, ast.Constant) and isinstance(k.value, str):
                            self.rules_map[k.value.upper()] = v.id if isinstance(v, ast.Name) else None
                elif not all(CONST_NAME.match(n) for n in names):
                    support_only = False
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                pass
            elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                pass  # a docstring
            else:
                support_only = False
        if defining:
            self.kind = "code"
        elif support_only and tree.body:
            self.kind = "support"


def read_medicine(src: str):
    """Return (sections, blocks). A section is (start, end, code, action); action is "fix", "drop" or None."""
    starts = [(m.start(), m.group(1)) for m in DISEASE.finditer(src)]
    appendix = APPENDIX.search(src)
    cut = appendix.start() if appendix else len(src)
    sections = []
    for i, (pos, code) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(src)
        end = min(end, cut) if pos < cut else end
        line = ACTION.search(src, pos, end)
        word = ACTION_WORD.search(line.group(1)) if line else None  # the first one: "fix the text. No document is dropped."
        sections.append((pos, end, code, word.group(1).lower() if word else None))
    blocks = [Block(i, textwrap.dedent(m.group(2)), m.start()) for i, m in enumerate(harm_test.FENCE.finditer(src), 1)]
    for b in blocks:
        for si, (start, end, _, _) in enumerate(sections):
            if start <= b.pos < end:
                b.section = si
    return sections, blocks


def resolve(sections, blocks):
    """Return ([rule], [notes]). A rule is {code, n, expr, how, action}; n counts the sections of one code.

    expr is Python that names the rule's function. The RULES dict and cure_<code> serve the first section of
    a code only. A later section needs a function of its own, not already used by an earlier rule.
    """
    code_blocks = [b for b in blocks if b.kind == "code"]
    rules_map = {}
    for b in code_blocks:
        rules_map.update(b.rules_map)
    funcs = {n.lower(): n for b in code_blocks for n in b.funcs}
    chosen, notes, seen, claimed = [], [], {}, set()
    for si, (_, _, code, action) in enumerate(sections):
        n = seen[code] = seen.get(code, 0) + 1
        label = code if n == 1 else f"{code} (medicine {n})"
        expr = how = None
        if n == 1 and code in rules_map:
            expr = rules_map[code] or f'_student_rules["{code}"]'
            how = "RULES dict"
        elif n == 1 and f"cure_{code.lower()}" in funcs:
            expr, how = funcs[f"cure_{code.lower()}"], f"function cure_{code.lower()}"
        else:
            publics = sorted({f for b in code_blocks if b.section == si for f in b.funcs if not f.startswith("_")} - claimed)
            if len(publics) == 1:
                expr, how = publics[0], "the only function in the section"
            elif publics:
                notes.append(f"{label}: several functions in the section ({', '.join(publics)}); "
                             f"name the rule cure_{code.lower()} or add it to RULES")
            else:
                notes.append(f"{label}: no function found for this section")
        if expr:
            chosen.append({"code": code, "n": n, "expr": expr, "how": how, "action": action})
            claimed.add(expr)
    return chosen, notes


def origin(path: Path):
    """(pack_id, handle) for diagnosis/submissions/<pack_id>/<handle>/medicine.md, else None."""
    path = path.resolve()
    if path.parent.parent.parent.name == "submissions":
        return path.parent.parent.name, path.parent.name
    return None


def load_registry(path: Path):
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text(encoding="utf-8"))["rules"]
    except (OSError, ValueError, KeyError) as e:
        raise SystemExit(f"error: cannot read the registry {path}: {e}")


def save_registry(path: Path, entries):
    path.parent.mkdir(parents=True, exist_ok=True)
    entries = sorted(entries, key=lambda e: e["id"])
    path.write_text(json.dumps({"rules": entries}, indent=2) + "\n", encoding="utf-8")


def assign_ids(entries, pack: str, handle: str, rules, file_rel: str):
    """Return the rule ID of each rule in `rules`, in order. New entries are added to the registry list.

    A (pack, handle, code, n) that is in the registry keeps its ID. A new one takes the next number for its
    team and code. Rules of this pack and handle that are no longer in the medicine.md are marked withdrawn.
    """
    prefix = "DA" if pack in DATA_A_PACKS else "DB"
    mine = {(e["code"], e.get("n", 1)): e for e in entries if e["pack"] == pack and e["handle"] == handle}
    now = {(r["code"], r["n"]) for r in rules}
    for key, e in mine.items():
        e["withdrawn"] = key not in now
    ids = []
    for r in rules:
        e = mine.get((r["code"], r["n"]))
        if e is None:
            used = [int(x["id"].rsplit("-", 1)[1]) for x in entries if x["id"].startswith(f"{prefix}-{r['code']}-")]
            e = {"id": f"{prefix}-{r['code']}-{max(used, default=0) + 1:03d}", "pack": pack, "handle": handle,
                 "code": r["code"], "n": r["n"]}
            entries.append(e)
        e["n"], e["file"], e["action"], e["withdrawn"] = r["n"], file_rel, r["action"], False
        ids.append(e["id"])
    return ids


def render(source_name: str, blocks, chosen, ids=None) -> str:
    out = [f'"""Generated by medicine_extract.py from {source_name}. Do not edit by hand: '
           f'change the medicine.md and run the extractor again."""']
    for b in blocks:
        text = b.text.rstrip() + "\n"
        if b.kind == "code":
            out.append(f"# --- block {b.index} ---\n{text}")
        elif b.kind == "support":
            out.append(f"# --- block {b.index} (imports and constants; ignored if it does not run) ---\n"
                       f"try:\n{textwrap.indent(text, '    ')}except Exception:\n    pass\n")
    out.append('_student_rules = RULES if isinstance(globals().get("RULES"), dict) else {}')
    first = {}
    for r in chosen:
        first.setdefault(r["code"], r["expr"])  # RULES has one function for each code; the others are only in RULES_BY_ID
    out.append("RULES = {\n" + "".join(f'    "{code}": {expr},\n' for code, expr in first.items()) + "}\n")
    if ids:
        out.append("RULES_BY_ID = {\n" + "".join(f'    "{rid}": {r["expr"]},\n' for rid, r in zip(ids, chosen)) + "}\n")
    return "\n\n".join(out)


def default_out(path: Path):
    found = origin(path)
    return HERE.parent / "rules" / found[0] / f"{found[1]}.py" if found else None


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Turn one medicine.md into a rules file for harm_test.py.")
    ap.add_argument("medicine", type=Path)
    ap.add_argument("--out", type=Path, help="the rules file to write")
    ap.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY, help="the rule ID registry (default: ../rules/registry.json)")
    args = ap.parse_args(argv)

    out = args.out or default_out(args.medicine)
    if out is None:
        print("error: this path is not diagnosis/submissions/<pack_id>/<handle>/medicine.md; give --out", file=sys.stderr)
        return 2
    try:
        src = args.medicine.read_text(encoding="utf-8")
    except OSError as e:
        print(f"error: cannot read {args.medicine}: {e.strerror}", file=sys.stderr)
        return 2

    sections, blocks = read_medicine(src)
    if not sections:
        print("error: no '**Disease:** <code>' line found, so there is no medicine section", file=sys.stderr)
        return 1
    chosen, notes = resolve(sections, blocks)

    print(f"{args.medicine.name}: {len(sections)} sections, {len(blocks)} python blocks "
          f"({sum(b.kind == 'code' for b in blocks)} code, {sum(b.kind == 'support' for b in blocks)} support)")
    if not chosen:
        for n in notes:
            print(f"  note: {n}")
        print("error: no rule could be matched to a disease code; nothing written", file=sys.stderr)
        return 1

    found = origin(args.medicine)
    entries, ids = None, None
    if found:
        entries = load_registry(args.registry)
        file_rel = os.path.relpath(out.resolve(), args.registry.resolve().parent)
        ids = assign_ids(entries, found[0], found[1], chosen, file_rel)
    for i, r in enumerate(chosen):
        print(f"  {r['code']}: {r['expr']}   (from {r['how']}, action {r['action'] or 'not stated'})"
              + (f"   -> {ids[i]}" if ids else ""))
    for b in blocks:
        if b.kind in ("fragment", "syntax error"):
            print(f"  left out: block {b.index}, {b.kind}")
    for n in notes:
        print(f"  note: {n}")
    if not found:
        print("  note: the path has no pack and handle, so the rules get no IDs and the registry is not changed")
        if any(r["n"] > 1 for r in chosen):
            print("  note: without IDs only the first rule of each code is in the file")

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(args.medicine.name, blocks, chosen, ids), encoding="utf-8")
    print(f"written: {out}")
    if entries is not None:
        save_registry(args.registry, entries)
        print(f"registry: {args.registry}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
