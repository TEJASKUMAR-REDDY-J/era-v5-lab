"""Only supported packs may be labelled PASS; missing G1 domains remain pending."""
import importlib.util
from pathlib import Path

here=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('run_harm_suite', here/'run_harm_suite.py')
runner=importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


def test_expected_pack_coverage():
    assert len(runner.ALL) == 13
    assert len(runner.SUPPORTED) == 9
    assert len(runner.PENDING) == 4
    assert 'code-python' in runner.PENDING
    assert 'math-megamath' in runner.PENDING


def test_missing_inputs_never_pass(tmp_path, monkeypatch):
    monkeypatch.setattr(runner,'TEAM',tmp_path/'team')
    assert runner.run(tmp_path/'original',tmp_path/'reports',tmp_path/'no-spec.md') == 1
    import json
    results=json.loads((tmp_path/'reports'/'g1_harm_summary.json').read_text())
    assert all(r['status'] in ('PENDING','NOT_EVALUATED') for r in results)
    assert len(results)==13
