"""Harm test: run one cleaning rule on a gold set and count the damage.

Usage:
    python -I harm_test.py --pack <pack.parquet> --gold <pack_gold.csv> --rule <RULE_ID>
    python -I harm_test.py --pack <pack.parquet> --gold <pack_gold.csv> --rules <rules.py|medicine.md> --rule <CODE>

    --pack      the pack Parquet file (columns doc_id, text are read)
    --gold      the gold CSV (column doc_id; reader_1 and reader_2 are ignored)
    --rule      a rule ID such as DA-B3-001 (DA = Data A, DB = Data B, then the disease code and a number),
                or a disease code such as B3 when --rules is given
    --rules     a .py file, or a medicine.md file whose ```python blocks hold the code. Not needed for a rule ID:
                the registry says which file medicine_extract.py wrote the rule to
    --registry  the registry file (default: ../rules/registry.json)
    --limit     the failing limit in percent of the gold set (default 1)
    --show N    also list the first N changed or dropped doc_ids (ids only, never text)
    --timeout   seconds allowed for one rule call on one document (default 5)

Inside a rules file the rule is found in one of three ways:
    RULES_BY_ID = {"DA-B3-001": fn}   written by medicine_extract.py (used for a rule ID)
    RULES = {"B3": fn}                fn(text) -> ("keep" | "fix" | "drop", new_text)   (the shared format)
    def cure_b3(text): ...            returns the new text as a str

A document is "changed" when the rule returns text that differs from the input (compared byte for byte, no
normalisation). It is "dropped" when the rule returns the action "drop". Each document counts once.
PASS means (changed + dropped) is at most --limit percent of the gold documents.

Exit code: 0 = PASS, 1 = FAIL, 2 = the test could not be run (bad input, or the rule raised an error).

The rules file is run as code: read it before you run it. A per-document timeout stops runaway regexes (Unix only).
"""
import argparse
import csv
import hashlib
import json
import re
import signal
import sys
import textwrap
from fractions import Fraction
from pathlib import Path

import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq

ACTIONS = ("keep", "fix", "drop")
RULE_ID = re.compile(r"^D[AB]-[A-H][1-9]-\d{3}$")
DEFAULT_REGISTRY = Path(__file__).resolve().parent.parent / "rules" / "registry.json"
# A fenced block, possibly indented inside a list item. The closing fence must have the same indent.
FENCE = re.compile(r"^([ \t]*)```(?:python|py)[ \t]*\n(.*?)^\1```[ \t]*$", re.S | re.M)
HAS_ALARM = hasattr(signal, "setitimer")


class Fatal(Exception):
    """The test cannot be run. The message is printed and the exit code is 2."""


class RuleTimeout(Exception):
    pass


def _on_alarm(signum, frame):
    raise RuleTimeout


def load_rules(path: Path):
    """Run the code in the rules file and return (namespace, sha256 of the code that ran)."""
    try:
        src = path.read_text(encoding="utf-8")
    except OSError as e:
        raise Fatal(f"cannot read rules file {path}: {e.strerror}")
    is_md = path.suffix.lower() == ".md"
    blocks = [textwrap.dedent(m.group(2)) for m in FENCE.finditer(src)] if is_md else [src]
    if not blocks:
        raise Fatal(f"{path.name}: no ```python block found")
    ns = {"__name__": "rules"}
    ran = []
    for i, block in enumerate(blocks, 1):
        label = f"{path.name} block {i}" if is_md else path.name
        try:
            exec(compile(block, label, "exec"), ns)
            ran.append(block)
        except Exception as e:
            if not is_md:
                raise Fatal(f"{label}: {type(e).__name__}: {e}")
            # medicine.md often shows code fragments next to the complete code. Skip what does not run alone.
            print(f"warning: skipped {label} ({type(e).__name__}: {e})", file=sys.stderr)
    if not ran:
        raise Fatal(f"{path.name}: no code block ran without an error")
    return ns, hashlib.sha256("\n".join(ran).encode("utf-8")).hexdigest()


def registry_file_for(rule_id: str, registry: Path) -> Path:
    """Find the rules file of a rule ID in the registry."""
    try:
        entries = json.loads(registry.read_text(encoding="utf-8"))["rules"]
    except (OSError, ValueError, KeyError) as e:
        raise Fatal(f"cannot read the registry {registry}: {e}")
    for e in entries:
        if e["id"] == rule_id:
            if e.get("withdrawn"):
                print(f"warning: {rule_id} is withdrawn: its medicine.md no longer has this rule", file=sys.stderr)
            return registry.parent / e["file"]
    raise Fatal(f"{rule_id} is not in the registry {registry}")


def find_rule(ns: dict, code: str):
    if RULE_ID.match(code):
        by_id = ns.get("RULES_BY_ID")
        if isinstance(by_id, dict) and code in by_id:
            return by_id[code]
        raise Fatal(f"rule {code} is not in the rules file (found: {', '.join(sorted(by_id or {})) or 'none'})")
    rules = ns.get("RULES")
    if isinstance(rules, dict) and code in rules:
        return rules[code]
    fn = ns.get("cure_" + code.lower())
    if callable(fn):
        return fn
    found = sorted(rules) if isinstance(rules, dict) else sorted(k[5:].upper() for k in ns if k.startswith("cure_"))
    raise Fatal(f"no rule for {code} in the rules file (found: {', '.join(found) or 'none'})")


def classify(text: str, out) -> str:
    """Return 'keep', 'fix' or 'drop' for one rule result. 'fix' means the text really differs."""
    if isinstance(out, str):
        return "fix" if out != text else "keep"
    if isinstance(out, tuple) and len(out) == 2 and out[0] in ACTIONS:
        if out[0] == "drop":
            return "drop"
        if not isinstance(out[1], str):
            raise TypeError("new_text is not a str")
        # Judge by the text: a rule that says "keep" but returns different text still changed the document.
        return "fix" if out[1] != text else "keep"
    raise TypeError("rule must return a str or (action, new_text)")


def read_gold(path: Path):
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if "doc_id" not in (reader.fieldnames or []):
                raise Fatal(f"{path.name}: no doc_id column")
            ids = [r["doc_id"].strip() for r in reader if r["doc_id"] and r["doc_id"].strip()]
    except OSError as e:
        raise Fatal(f"cannot read gold file {path}: {e.strerror}")
    unique = list(dict.fromkeys(ids))
    if len(unique) < len(ids):
        print(f"warning: {len(ids) - len(unique)} duplicate doc_id rows in the gold file were ignored", file=sys.stderr)
    if not unique:
        raise Fatal(f"{path.name}: the gold set is empty")
    return unique


def read_pack_texts(path: Path, ids):
    """Return {doc_id: text} for the gold ids only."""
    try:
        table = pq.read_table(path, columns=["doc_id", "text"])
    except (OSError, KeyError, ValueError) as e:
        raise Fatal(f"cannot read pack {path}: {e}")
    table = table.filter(pc.is_in(table["doc_id"], value_set=pa.array(ids, type=table["doc_id"].type)))
    texts = {}
    for doc_id, text in zip(table["doc_id"].to_pylist(), table["text"].to_pylist()):
        if doc_id in texts:
            raise Fatal(f"doc_id {doc_id} appears twice in the pack")
        if text is None:
            raise Fatal(f"doc_id {doc_id} has no text in the pack")
        texts[doc_id] = text
    missing = [i for i in ids if i not in texts]
    if missing:
        raise Fatal(f"{len(missing)} gold doc_ids are not in the pack, for example {', '.join(missing[:3])}")
    return texts


def harm_percent(changed: int, dropped: int, n: int, limit: Fraction):
    """Return (percent of the gold set that was changed or dropped, passed). The one place the limit is applied."""
    percent = Fraction((changed + dropped) * 100, n)
    return percent, percent <= limit


def run_rule(rule, texts: dict, timeout: float):
    changed, dropped, errors = [], [], []
    if HAS_ALARM:
        signal.signal(signal.SIGALRM, _on_alarm)
    for doc_id, text in texts.items():
        if HAS_ALARM:
            signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            verdict = classify(text, rule(text))
        except Exception as e:  # a rule that crashes is a rule bug; report the type only, never document text
            errors.append((doc_id, type(e).__name__))
            continue
        finally:
            if HAS_ALARM:
                signal.setitimer(signal.ITIMER_REAL, 0)
        if verdict == "fix":
            changed.append(doc_id)
        elif verdict == "drop":
            dropped.append(doc_id)
    return changed, dropped, errors


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Run one cleaning rule on a gold set and report the harm.")
    ap.add_argument("--pack", required=True, type=Path)
    ap.add_argument("--gold", required=True, type=Path)
    ap.add_argument("--rules", type=Path, help="rules .py or medicine.md (not needed for a rule ID)")
    ap.add_argument("--rule", required=True, help="rule ID such as DA-B3-001, or a disease code such as B3")
    ap.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    ap.add_argument("--limit", default="1", help="failing limit in percent of the gold set (default 1)")
    ap.add_argument("--show", type=int, default=0, metavar="N", help="list the first N affected doc_ids")
    ap.add_argument("--timeout", type=float, default=5.0, help="seconds per document (default 5)")
    args = ap.parse_args(argv)

    try:
        limit = Fraction(args.limit)
        if limit < 0:
            raise ValueError
    except ValueError:
        print(f"error: --limit must be a number of percent, not {args.limit!r}", file=sys.stderr)
        return 2
    code = args.rule.strip().upper()
    if args.rules is None and not RULE_ID.match(code):
        print("error: give --rules, or a rule ID such as DA-B3-001 as --rule", file=sys.stderr)
        return 2

    try:
        ids = read_gold(args.gold)
        texts = read_pack_texts(args.pack, ids)
        rules_path = args.rules or registry_file_for(code, args.registry)
        ns, digest = load_rules(rules_path)
        rule = find_rule(ns, code)
        if not HAS_ALARM:
            print("warning: no per-document timeout on this platform", file=sys.stderr)
        changed, dropped, errors = run_rule(rule, texts, args.timeout)
    except Fatal as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    n = len(texts)
    harmed = len(changed) + len(dropped)
    percent, passed = harm_percent(len(changed), len(dropped), n, limit)
    print(f"pack: {args.pack.name}   gold: {args.gold.name} ({n} documents)   rule: {code}")
    print(f"rules file: {rules_path.name}   code sha256: {digest[:16]}")
    print(f"documents changed: {len(changed)}")
    print(f"documents dropped: {len(dropped)}")
    print(f"percent: {float(percent):.2f}% of the gold set (limit {args.limit}%)")
    if args.show and harmed:
        print("affected doc_ids: " + ", ".join(((changed + dropped)[: args.show])))
    if errors:
        print(f"rule errors: {len(errors)} documents, for example {errors[0][0]} ({errors[0][1]})")
        print("result: ERROR (the rule failed on some gold documents, so the harm is not known)")
        return 2
    print("result: " + ("PASS" if passed else "FAIL"))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
