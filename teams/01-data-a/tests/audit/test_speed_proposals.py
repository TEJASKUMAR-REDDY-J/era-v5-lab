"""Exercise the carried benchmark against the real cleaner and collated sheet."""
import re
import subprocess
import sys
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

DATA_A = Path(__file__).resolve().parents[2]
SCRIPT = DATA_A / "spec_v1_1" / "scripts" / "speed_proposals.py"
PACKS = ("en-dclm", "en-fineweb-edu", "en-nemotroncc", "en-nemotroncc-synth")


def test_benchmark_uses_pack_specific_cards_and_counts_changed_outputs(tmp_path):
    # A valid document, an encoding defect, and a fragment the cleaner drops.
    # Incorrect pack metadata must be replaced by the selected file's pack.
    body = " ".join(f"The researcher described observation {i} in a detailed report about the river and its surroundings."
                    for i in range(30))
    texts = [body, body + " The children\x92s books described their journey.",
             "A short fragment that ends with the word of"]
    rows = [{"doc_id": f"{i:016x}", "text": text, "url": "https://example.org/report", "lang_label": "en",
             "pack_id": "code-go"} for i, text in enumerate(texts)]
    for pack in PACKS:
        pq.write_table(pa.Table.from_pylist(rows), tmp_path / f"{pack}.parquet")
    result = subprocess.run([sys.executable, "-I", str(SCRIPT), "--clean", str(DATA_A / "spec_v1_1" / "clean.py"),
                             "--packs", str(tmp_path), "--repeat", "1"],
                            capture_output=True, text=True, check=True, timeout=60)
    sections = re.split(r"^== ", result.stdout, flags=re.M)[1:]
    assert len(sections) == 4
    for pack, section in zip(PACKS, sections):
        assert section.startswith(f"{pack}: 3 docs\n")
        assert "output differs on 1 docs" in section
        assert "DA-A2-010" in section and "DA-B3-012" in section and "DA-B4-016" in section
        if pack == "en-nemotroncc-synth":
            assert "DA-C2-010" in section and "DA-F1-009" in section
            assert "DA-C2-009" not in section and "DA-F1-007" not in section
        else:
            assert "DA-C2-009" in section and "DA-F1-007" in section
            assert "DA-C2-010" not in section and "DA-F1-009" not in section
    assert "ALL: 12 docs" in result.stdout and "output differs on 4 docs" in result.stdout
    assert body not in result.stdout


def test_empty_selected_pack_exits_without_a_misleading_speed(tmp_path):
    pq.write_table(pa.table({"doc_id": pa.array([], type=pa.string()), "text": pa.array([], type=pa.string())}),
                   tmp_path / "en-dclm.parquet")
    result = subprocess.run([sys.executable, "-I", str(SCRIPT), "--clean", str(DATA_A / "spec_v1_1" / "clean.py"),
                             "--packs", str(tmp_path), "--pack", "en-dclm", "--repeat", "1"],
                            capture_output=True, text=True, timeout=60)
    assert result.returncode != 0
    assert "no documents to time" in result.stderr
    assert "ALL:" not in result.stdout
