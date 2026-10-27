"""Tests for medicine_extract.py. Run: python -I teams/01-data-a/tools/test_medicine_extract.py"""
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

sys.path.insert(0, str(Path(__file__).resolve().parent))
import harm_test  # noqa: E402
import medicine_extract  # noqa: E402

FENCE = "```"


def md(*parts):
    return "\n".join(parts)


def py(code):
    return f"{FENCE}python\n{code}\n{FENCE}"


class ExtractCase(unittest.TestCase):
    def extract(self, text, load=True):
        tmp = Path(tempfile.mkdtemp())
        src, out = tmp / "medicine.md", tmp / "rules.py"
        src.write_text(text)
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(io.StringIO()):
            rc = medicine_extract.main([str(src), "--out", str(out)])
        ns = harm_test.load_rules(out)[0] if load and out.exists() else None  # loading RUNS the generated code
        return rc, stdout.getvalue(), ns

    def test_cure_functions_found_by_name(self):
        rc, out, ns = self.extract(md(
            "1. **Disease:** B3, ghost markers", py("def cure_b3(t):\n    return t.replace('<x>', '')"),
            "## Medicine 2", "1. **Disease:** B4, tags", py("import re\ndef cure_b4(t):\n    return re.sub('<y>', '', t)")))
        self.assertEqual(rc, 0)
        self.assertEqual(sorted(ns["RULES"]), ["B3", "B4"])
        self.assertEqual(ns["RULES"]["B3"]("a<x>b"), "ab")

    def test_any_function_name_when_it_is_the_only_one_in_the_section(self):
        rc, out, ns = self.extract(md("**Disease:** A1, junk", py("def strip_junk(t):\n    return t.strip()")))
        self.assertEqual(rc, 0)
        self.assertIn("the only function in the section", out)
        self.assertEqual(ns["RULES"]["A1"]("  x "), "x")

    def test_several_functions_are_reported_not_guessed(self):
        rc, out, ns = self.extract(md("**Disease:** A1, junk", py("def one(t):\n    return t\ndef two(t):\n    return t")))
        self.assertEqual(rc, 1)
        self.assertIn("several functions in the section (one, two)", out)
        self.assertIsNone(ns)  # nothing written

    def test_rules_dict_fragments_and_appendix(self):
        # Mirrors amukka's file: fragments in the sections, the complete code in an appendix, a RULES dict.
        rc, out, ns = self.extract(md(
            "## Medicine 1", "1. **Disease:** B3, markers", py("MARKER = 1\ntext = MARKER + text"),
            "## Medicine 2", "1. **Disease:** E1, generated", py("if x drop"),
            "## Appendix", py("import re\nMARKER = re.compile('<m>')\ndef b3(t):\n    return MARKER.sub('', t)\n"
                              "RULES = {'B3': b3, 'E1': lambda t: ('drop', '')}")))
        self.assertEqual(rc, 0)
        self.assertEqual(sorted(ns["RULES"]), ["B3", "E1"])
        self.assertEqual(ns["RULES"]["B3"]("a<m>b"), "ab")
        self.assertEqual(ns["RULES"]["E1"]("x"), ("drop", ""))  # a lambda in RULES is kept
        self.assertIn("left out: block 1, fragment", out)
        self.assertIn("left out: block 2, syntax error", out)

    def test_support_block_that_fails_does_not_break_the_file(self):
        rc, out, ns = self.extract(md("**Disease:** A1, junk", py("PATTERN = re.compile('x')"),  # `re` never imported
                                      py("def cure_a1(t):\n    return t")))
        self.assertEqual(rc, 0)
        self.assertIn("1 support", out)
        self.assertEqual(ns["RULES"]["A1"]("q"), "q")

    def test_second_medicine_for_the_same_code_is_reported_and_ignored(self):
        rc, out, ns = self.extract(md(
            "**Disease:** B3, first", py("def cure_b3(t):\n    return 'first'"),
            "**Disease:** B3, second", py("def other(t):\n    return 'second'")))
        self.assertEqual(rc, 0)
        self.assertEqual(ns["RULES"]["B3"](""), "first")
        self.assertIn("second medicine for this code", out)

    def test_no_disease_line(self):
        rc, _, ns = self.extract(md("# Medicine sheet", py("def cure_b3(t):\n    return t")))
        self.assertEqual(rc, 1)
        self.assertIsNone(ns)

    def test_extractor_does_not_run_the_code(self):
        marker = Path(tempfile.mkdtemp()) / "ran"
        rc, _, _ = self.extract(md("**Disease:** A1, junk", py(
            f"open({str(marker)!r}, 'w').write('x')\ndef cure_a1(t):\n    return t")), load=False)
        self.assertEqual(rc, 0)
        self.assertFalse(marker.exists())

    def test_default_out_only_inside_submissions(self):
        self.assertIsNone(medicine_extract.default_out(Path("/tmp/x/medicine.md")))
        p = Path("/r/diagnosis/submissions/code-rust/amukka/medicine.md")
        self.assertEqual(medicine_extract.default_out(p).parts[-3:], ("rules", "code-rust", "amukka.py"))


class IdCase(unittest.TestCase):
    """Rule IDs and the registry. Medicine files live in <tmp>/submissions/<pack>/<handle>/medicine.md."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.registry = self.tmp / "rules" / "registry.json"

    def write_medicine(self, pack, handle, text):
        d = self.tmp / "submissions" / pack / handle
        d.mkdir(parents=True, exist_ok=True)
        (d / "medicine.md").write_text(text)
        return d / "medicine.md"

    def run_extract(self, path):
        out = self.tmp / "rules" / path.parent.parent.name / f"{path.parent.name}.py"
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(io.StringIO()):
            rc = medicine_extract.main([str(path), "--out", str(out), "--registry", str(self.registry)])
        return rc, stdout.getvalue(), out

    def entries(self):
        return {e["id"]: e for e in json.loads(self.registry.read_text())["rules"]}

    @staticmethod
    def b3(ret="t"):
        return md("**Disease:** B3, markers", py(f"def cure_b3(t):\n    return {ret}"))

    def test_team_prefix_and_counter(self):
        self.run_extract(self.write_medicine("code-rust", "alice", self.b3()))
        self.run_extract(self.write_medicine("code-rust", "bob", self.b3()))
        self.run_extract(self.write_medicine("cadj-stackexchange", "carol", self.b3()))
        self.assertEqual(sorted(self.entries()), ["DA-B3-001", "DA-B3-002", "DB-B3-001"])
        self.assertEqual(self.entries()["DA-B3-002"]["handle"], "bob")

    def test_rerun_keeps_ids_and_marks_withdrawn(self):
        two = md("**Disease:** B3, a", py("def cure_b3(t):\n    return t"), "**Disease:** B4, b", py("def cure_b4(t):\n    return t"))
        path = self.write_medicine("code-rust", "alice", two)
        self.run_extract(path)
        self.run_extract(self.write_medicine("code-rust", "bob", self.b3()))      # DA-B3-002
        before = self.entries()
        self.run_extract(path)
        self.assertEqual(self.entries(), before)                                   # rerun changes nothing
        self.run_extract(self.write_medicine("code-rust", "alice", self.b3()))   # B4 removed
        after = self.entries()
        self.assertTrue(after["DA-B4-001"]["withdrawn"])
        self.assertFalse(after["DA-B3-001"]["withdrawn"])
        self.assertEqual(sorted(after), ["DA-B3-001", "DA-B3-002", "DA-B4-001"])  # the ID is kept, not reused
        self.run_extract(self.write_medicine("code-rust", "alice", two))         # B4 comes back
        self.assertFalse(self.entries()["DA-B4-001"]["withdrawn"])

    def test_generated_file_has_rules_by_id(self):
        _, out, path = self.run_extract(self.write_medicine("code-rust", "alice", self.b3("'x'")))
        self.assertIn("-> DA-B3-001", out)
        ns = harm_test.load_rules(path.parent / "alice.py")[0]
        self.assertEqual(ns["RULES_BY_ID"]["DA-B3-001"]("anything"), "x")

    def test_harm_test_finds_the_rule_by_id(self):
        self.run_extract(self.write_medicine("code-rust", "alice", self.b3("t.replace('<m>', '')")))
        pack, gold = self.tmp / "pack.parquet", self.tmp / "gold.csv"
        ids = [f"d{i}" for i in range(100)]
        pq.write_table(pa.table({"doc_id": ids, "text": ["plain"] * 99 + ["has <m> marker"]}), pack)
        gold.write_text("doc_id,reader_1,reader_2\n" + "".join(f"{i},a,b\n" for i in ids))
        argv = ["--pack", str(pack), "--gold", str(gold), "--registry", str(self.registry)]
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = harm_test.main(argv + ["--rule", "DA-B3-001"])
        self.assertEqual(rc, 0)                                   # 1 of 100 = 1.00%
        self.assertIn("documents changed: 1", out.getvalue())
        self.assertIn("rule: DA-B3-001", out.getvalue())
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            self.assertEqual(harm_test.main(argv + ["--rule", "DA-B3-009"]), 2)   # not in the registry
            self.assertEqual(harm_test.main(argv + ["--rule", "B3"]), 2)           # a code needs --rules
        self.assertIn("not in the registry", err.getvalue())
        self.assertIn("give --rules", err.getvalue())

    def test_path_outside_submissions_gets_no_ids(self):
        src = self.tmp / "medicine.md"
        src.write_text(self.b3())
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            rc = medicine_extract.main([str(src), "--out", str(self.tmp / "r.py"), "--registry", str(self.registry)])
        self.assertEqual(rc, 0)
        self.assertIn("no IDs", stdout.getvalue())
        self.assertFalse(self.registry.exists())


if __name__ == "__main__":
    unittest.main()
