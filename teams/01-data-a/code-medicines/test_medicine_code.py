"""Harm test of medicine_code.md: every rule alone, then the whole sheet, on each code pack's gold set.

Each rule is a python block in the sheet with RULE_ID, LANGS and medicine(doc) -> (action, text),
doc = {"doc_id", "text", "url", "lang_label"}; action is keep, fix or drop. A gold doc counts once if its
text changes or it is dropped; harm = (changed + dropped) / gold, PASS at 1% or less (Spec v1).

Counting is the team's harm test: the gold file is read, each result classified and the limit applied by
teams/01-data-a/tools/harm_test.py (read_gold, classify, harm_percent). Only the pack is read here, because
the rules need "url" and "lang_label" as well as the text (H3 and F2 look at the path, LANGS at the language).

Checks:
  1. each rule alone: gold changed / dropped, PASS or FAIL, docs it touches in the pack, idempotence
  2. the sheet, one pass in section order (drops come first): gold harm, pack fixed / dropped / untouched
  3. the sheet run again on its own output: docs where the second pass still changes or drops something

  python -I teams/01-data-a/code-medicines/test_medicine_code.py --pack code-go=code-go.parquet \
      --pack code-rust=code-rust.parquet ...

Needs pyarrow. Gold files default to teams/01-data-a/gold/<pack>_gold.csv. Exit code 0 if all PASS, 1 if not.
"""
import argparse, os, re, sys, textwrap
from collections import Counter
from fractions import Fraction
from pathlib import Path
import pyarrow.parquet as pq

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tools"))
import harm_test as HT  # noqa: E402  the team's harm test: same counting and limit


def load_rules(sheet):
    rules = []
    for block in re.findall(r"```python\n(.*?)```", open(sheet, encoding="utf-8").read(), re.S):
        if "RULE_ID" not in block: continue
        ns = {}
        exec(textwrap.dedent(block), ns)
        rules.append((ns["RULE_ID"], ns["LANGS"], ns["medicine"]))
    ids = [r[0] for r in rules]
    assert len(ids) == len(set(ids)), "duplicate RULE_ID in the sheet"
    return rules


def run_sheet(rules, doc):
    """One pass in sheet order: ("drop" | "fix" | "keep", text, ids of the rules that acted)."""
    d, acted = dict(doc), []
    for rid, _, med in rules:
        act, t = med(d)
        if act == "drop": return "drop", "", acted + [rid]
        if act == "fix": d["text"] = t; acted.append(rid)
    return ("fix" if d["text"] != doc["text"] else "keep"), d["text"], acted


def test_pack(pack, rows, gold_ids, rules, limit):
    gold = [r for r in rows if r["doc_id"] in gold_ids]
    if not gold: return None
    out = {"pack": pack, "gold": len(gold), "missing": len(gold_ids) - len(gold), "rules": {}}
    for rid, langs, med in rules:
        g = Counter(HT.classify(r["text"], med(r)) for r in gold)
        touched = not_idem = 0
        for r in rows:
            act, t = med(r)
            if act == "keep": continue
            touched += 1
            if act == "fix" and med(dict(r, text=t))[0] != "keep": not_idem += 1
        pct, passed = HT.harm_percent(g["fix"], g["drop"], len(gold), limit)
        out["rules"][rid] = (g["fix"], g["drop"], float(pct), "PASS" if passed else "FAIL", touched, not_idem)
    g, p, again = Counter(), Counter(), []
    for r in rows:
        act, t, _ = run_sheet(rules, r)
        p[act] += 1
        if r["doc_id"] in gold_ids: g[act] += 1
        if act == "fix":
            act2, _, acted2 = run_sheet(rules, dict(r, text=t))
            if act2 != "keep": again.append((r["doc_id"], act2, acted2))
    pct, passed = HT.harm_percent(g["fix"], g["drop"], len(gold), limit)
    out["sheet"] = (g["fix"], g["drop"], float(pct), "PASS" if passed else "FAIL", p["fix"], p["drop"], p["keep"])
    out["again"] = again
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sheet", default=os.path.join(HERE, "medicine_code.md"))
    ap.add_argument("--pack", action="append", required=True, help="<pack_id>=<pack.parquet>, repeat per pack")
    ap.add_argument("--gold-dir", default=os.path.join(HERE, "..", "gold"))
    ap.add_argument("--limit", default="1", help="failing limit in percent of the gold set (default 1)")
    a = ap.parse_args()
    rules = load_rules(a.sheet)
    print(f"{len(rules)} rules in {os.path.basename(a.sheet)}\n")
    ok = True
    for spec in a.pack:
        pack, path = spec.split("=", 1)
        rows = pq.read_table(path, columns=["doc_id", "lang_label", "url", "text"]).to_pylist()
        gold_file = os.path.join(a.gold_dir, f"{pack}_gold.csv")
        gold_ids = set(HT.read_gold(Path(gold_file)))
        res = test_pack(pack, rows, gold_ids, rules, Fraction(a.limit))
        if res is None:
            print(f"## {pack}: NOT_EVALUATED (no gold doc in the pack)\n"); continue
        print(f"## {pack}: gold {res['gold']}" + (f" ({res['missing']} gold ids not in the pack)" if res["missing"] else ""))
        print("\n| rule | gold changed | gold dropped | harm % | result | pack docs touched | not idempotent |\n|---|---|---|---|---|---|---|")
        for rid, (ch, dr, pct, verdict, touched, ni) in res["rules"].items():
            if touched or ch or dr:
                print(f"| {rid} | {ch} | {dr} | {pct:.2f} | {verdict} | {touched} | {ni} |")
            ok &= verdict == "PASS"
        ch, dr, pct, verdict, pf, pd, pk = res["sheet"]
        ok &= verdict == "PASS"
        print(f"\nWhole sheet: gold changed {ch}, dropped {dr}, harm {pct:.2f}% {verdict}. "
              f"Pack: {pf} fixed, {pd} dropped, {pk} untouched.")
        print(f"Second pass over the output acts on {len(res['again'])} doc(s)"
              + "".join(f"\n  - {d}: {act} by {', '.join(ids)}" for d, act, ids in res["again"]) + "\n")
    print("ALL PASS" if ok else "SOME FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
