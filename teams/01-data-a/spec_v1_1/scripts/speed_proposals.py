"""Time the collated proposals against the cleaner, carrying forward PR #75's benchmark.

For each pack, time every applicable card against the rule it replaces, then the
whole pipeline with all applicable cards in place. Use the collation's ordering,
pack scopes and merged cards, including the shared F1 rule. Best of --repeat
passes, one process, CPU only. Prints counts and timings, never document text.

From teams/01-data-a:
  python3 -I spec_v1_1/scripts/speed_proposals.py --clean spec_v1_1/clean.py --packs <sample-pack-folder>

The four English packs are the default; --pack can select any collated pack.
Synthetic inputs can check the command, but do not establish corpus throughput.
"""
import argparse
import sys
import time
from pathlib import Path

import pyarrow.parquet as pq

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE.parent / "audit"))
import collated_medicine_check as check  # noqa: E402

PACKS = ("en-dclm", "en-fineweb-edu", "en-nemotroncc", "en-nemotroncc-synth")


def run(doc, steps):
    d = dict(doc)
    for _, rule in steps:
        action, text = rule(d)
        if action == "drop":
            return "drop", doc["text"]
        d["text"] = text
    return ("fix" if d["text"] != doc["text"] else "keep"), d["text"]


def best(fn, repeat):
    times = []
    for _ in range(repeat):
        start = time.perf_counter()
        out = fn()
        times.append(time.perf_counter() - start)
    return min(times), out


def positive_int(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return number


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--clean", type=Path, required=True, help="spec_v1_1/clean.py")
    ap.add_argument("--packs", type=Path, required=True, help="folder with <pack>.parquet")
    ap.add_argument("--sheet", type=Path, default=check.SHEET)
    ap.add_argument("--pack", nargs="+", choices=check.PACKS, default=PACKS)
    ap.add_argument("--repeat", type=positive_int, default=3)
    args = ap.parse_args()

    check.replay.CLEAN, check.SHEET = args.clean, args.sheet
    check.load()
    total = {"docs": 0, "before": 0.0, "after": 0.0, "differ": 0}
    for pack in args.pack:
        docs = pq.read_table(args.packs / f"{pack}.parquet").to_pylist()
        for doc in docs:
            doc["pack_id"] = pack
        n = len(docs)
        print(f"== {pack}: {n} docs")
        if not n:
            print("  empty pack: skipped")
            continue
        baseline = check.replay.rules(pack)
        proposed, old = check.with_cards(pack)
        # Refuse to publish a speed comparison against an inaccurate replay.
        if any(run(doc, baseline) != check.replay.c.clean(doc) for doc in docs):
            raise SystemExit(f"baseline replay differs from clean(): {pack}")

        for card in (c for c in check.cards if pack in check.packs_of(c)):
            rid = card["RULE_ID"]
            row = [f"  {rid:<10}"]
            if rid in old:
                t_old, _ = best(lambda: [old[rid](doc) for doc in docs], args.repeat)
                row.append(f"{card['REPLACES']} {1000 * t_old / n:.3f}")
            t_new, _ = best(lambda: [card["medicine"](doc) for doc in docs], args.repeat)
            row.append(f"{rid} {1000 * t_new / n:.3f} ms/doc")
            print("  ".join(row))
        t_b, out_b = best(lambda: [run(doc, baseline) for doc in docs], args.repeat)
        t_a, out_a = best(lambda: [run(doc, proposed) for doc in docs], args.repeat)
        differ = sum(x != y for x, y in zip(out_b, out_a))
        print(f"  clean()    spec v1.1 {n / t_b:.1f} docs/s, with proposals {n / t_a:.1f} docs/s "
              f"({t_b / t_a:.2f}x), {t_a:.2f} s; output differs on {differ} docs")
        total["docs"] += n
        total["before"] += t_b
        total["after"] += t_a
        total["differ"] += differ
    if not total["docs"]:
        raise SystemExit("no documents to time")
    print(f"ALL: {total['docs']} docs, spec v1.1 {total['before']:.2f} s, with proposals {total['after']:.2f} s "
          f"({total['before'] / total['after']:.2f}x), output differs on {total['differ']} docs")


if __name__ == "__main__":
    main()
