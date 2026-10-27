"""Tests for harm_test.py. Run: python -I teams/01-data-a/tools/test_harm_test.py."""
import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

sys.path.insert(0, str(Path(__file__).resolve().parent))
import harm_test  # noqa: E402

RUST_MD = Path(__file__).resolve().parents[3] / "diagnosis/submissions/code-rust/amukka/medicine.md"


class HarmTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.texts = {f"d{i:03d}": f"clean document {i}" for i in range(200)}
        self.texts["d000"] = "<issue_start> marked document"
        self.texts["d001"] = "<issue_start> another one"
        self.texts["d002"] = "DROPME"
        pq.write_table(pa.table({"doc_id": list(self.texts), "text": list(self.texts.values())}), self.tmp / "pack.parquet")
        self.write_gold(list(self.texts))

    def write_gold(self, ids):
        (self.tmp / "gold.csv").write_text("doc_id,reader_1,reader_2\n" + "".join(f"{i},a,b\n" for i in ids))

    def run_ht(self, rules_src, code, name="rules.py", *extra):
        (self.tmp / name).write_text(rules_src)
        argv = ["--pack", str(self.tmp / "pack.parquet"), "--gold", str(self.tmp / "gold.csv"),
                "--rules", str(self.tmp / name), "--rule", code, *extra]
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = harm_test.main(argv)
        return rc, out.getvalue(), err.getvalue()

    def test_pass_at_exactly_one_percent(self):
        # 2 of 200 = 1.00%: PASS. The rule changes d000 and d001.
        rc, out, _ = self.run_ht("def cure_b3(t):\n    return t.replace('<issue_start>', '[issue_start]')\n", "B3")
        self.assertEqual(rc, 0)
        self.assertIn("documents changed: 2", out)
        self.assertIn("percent: 1.00%", out)
        self.assertIn("result: PASS", out)

    def test_fail_above_one_percent(self):
        # 3 of 200 = 1.50%: FAIL. Changed and dropped add up.
        src = ("RULES = {'X': lambda t: ('drop', '') if t == 'DROPME' else "
               "('fix', t.replace('<issue_start>', ''))}\n")
        rc, out, _ = self.run_ht(src, "x")
        self.assertEqual(rc, 1)
        self.assertIn("documents changed: 2", out)
        self.assertIn("documents dropped: 1", out)
        self.assertIn("result: FAIL", out)

    def test_limit_option(self):
        rc, out, _ = self.run_ht("cure_a1 = lambda t: t.upper()\n", "A1", "rules.py", "--limit", "100")
        self.assertEqual(rc, 0)
        self.assertIn("documents changed: 199", out)  # "DROPME" is already upper case

    def test_unchanged_fix_is_not_counted(self):
        rc, out, _ = self.run_ht("RULES = {'A1': lambda t: ('fix', t)}\n", "A1")
        self.assertEqual((rc, "documents changed: 0" in out), (0, True))

    def test_keep_with_different_text_counts_as_changed(self):
        rc, out, _ = self.run_ht("RULES = {'A1': lambda t: ('keep', t + ' ')}\n", "A1")
        self.assertEqual(rc, 1)
        self.assertIn("documents changed: 200", out)

    def test_show_lists_ids_only(self):
        _, out, _ = self.run_ht("cure_b3 = lambda t: t.replace('<issue_start>', '')\n", "B3", "rules.py", "--show", "5")
        self.assertIn("affected doc_ids: d000, d001", out)
        self.assertNotIn("marked document", out)

    def test_rule_exception_is_an_error_not_a_pass(self):
        rc, out, _ = self.run_ht("def cure_a1(t):\n    raise ValueError(t)\n", "A1")
        self.assertEqual(rc, 2)
        self.assertIn("result: ERROR", out)
        self.assertNotIn("clean document", out)  # the document text must not leak into the output

    def test_bad_return_value_is_an_error(self):
        rc, out, _ = self.run_ht("cure_a1 = lambda t: None\n", "A1")
        self.assertEqual(rc, 2)

    @unittest.skipUnless(harm_test.HAS_ALARM, "needs SIGALRM")
    def test_timeout(self):
        src = "import time\ndef cure_a1(t):\n    time.sleep(5)\n    return t\n"
        rc, out, _ = self.run_ht(src, "A1", "rules.py", "--timeout", "0.01")
        self.assertEqual(rc, 2)
        self.assertIn("RuleTimeout", out)

    def test_missing_rule(self):
        rc, _, err = self.run_ht("def cure_b3(t):\n    return t\n", "Z9")
        self.assertEqual(rc, 2)
        self.assertIn("no rule for Z9", err)

    def test_gold_id_missing_from_pack(self):
        self.write_gold(["d000", "nope"])
        rc, _, err = self.run_ht("cure_b3 = lambda t: t\n", "B3")
        self.assertEqual(rc, 2)
        self.assertIn("not in the pack", err)

    def test_duplicate_gold_ids_ignored(self):
        self.write_gold(["d005", "d005", "d006"])
        rc, out, err = self.run_ht("cure_b3 = lambda t: t\n", "B3")
        self.assertEqual(rc, 0)
        self.assertIn("(2 documents)", out)
        self.assertIn("duplicate", err)

    def test_markdown_skips_fragments(self):
        md = ("# Medicine\n\n- fragment:\n  ```python\n  text = MARKER.sub('', text)\n  ```\n\n"
              "```python\nimport re\n\ndef cure_b3(text):\n    return re.sub('<issue_start>', '', text)\n```\n")
        rc, out, err = self.run_ht(md, "B3", "medicine.md")
        self.assertIn("documents changed: 2", out)
        self.assertIn("skipped medicine.md block 1", err)

    @unittest.skipUnless(RUST_MD.exists(), "amukka's medicine.md is not in this checkout")
    def test_load_amukka_medicine(self):
        with contextlib.redirect_stderr(io.StringIO()):
            ns, _ = harm_test.load_rules(RUST_MD)
        self.assertEqual(sorted(ns["RULES"]), ["A2", "B3", "B4", "E1", "E4"])
        self.assertEqual(ns["RULES"]["B3"]("<reponame>x/y\nfn main() {}\n"), ("fix", "fn main() {}\n"))


if __name__ == "__main__":
    unittest.main()
