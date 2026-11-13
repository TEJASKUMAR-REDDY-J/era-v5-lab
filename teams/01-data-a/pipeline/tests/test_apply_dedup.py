"""Tests for apply_dedup.py: filter cleaned parts with dedup.py's remove_list.csv. Synthetic data only (conftest.py).

  python -m pytest teams/01-data-a/pipeline/tests -q
"""
import hashlib
import json
import subprocess
import sys

import pytest
import pyarrow.parquet as pq

from conftest import PARTS, PIPELINE
import apply_dedup as ad


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ids(path):
    return pq.read_table(path).column("doc_id").to_pylist()


def test_removes_exactly_the_listed_rows(tmp_path, cleaned, write_remove_list):
    rl = write_remove_list([["code-go", "train", "code-go/part-00000.parquet", 1, "g1"],
                            ["code-go", "train", "code-go/part-00000.parquet", 3, "g3"]])
    out = tmp_path / "deduped"
    s = ad.apply(cleaned, rl, out)
    part = out / "train" / "code-go" / "part-00000.parquet"
    assert ids(part) == ["g0", "g2", "g4"]
    src = cleaned / "train" / "code-go" / "part-00000.parquet"
    assert pq.read_schema(part) == pq.read_schema(src)
    kept_text = dict(zip(ids(part), pq.read_table(part).column("text").to_pylist()))
    assert kept_text == {r["doc_id"]: r["text"] for r in PARTS[("train", "code-go/part-00000.parquet")] if r["doc_id"] in kept_text}
    assert (s["totals"]["rows"], s["totals"]["removed"], s["totals"]["kept"]) == (13, 2, 11)
    assert s["by_pack"]["code-go"]["train"] == {"rows": 8, "removed": 2, "kept": 6}


def test_untouched_parts_are_byte_copies(tmp_path, cleaned, write_remove_list):
    rl = write_remove_list([["code-go", "train", "code-go/part-00000.parquet", 0, "g0"]])
    out = tmp_path / "deduped"
    s = ad.apply(cleaned, rl, out)
    for split, part in [("train", "en-dclm/part-00000.parquet"), ("heldout", "code-go/part-00000.parquet"),
                        ("train", "code-go/part-00001.parquet")]:
        assert sha(out / split / part) == sha(cleaned / split / part)
    copied = {(p["split"], p["part"]): p["copied"] for p in s["parts"]}
    assert copied[("train", "en-dclm/part-00000.parquet")] is True
    assert copied[("train", "code-go/part-00000.parquet")] is False


def test_same_doc_id_in_two_parts_only_the_listed_copy_goes(tmp_path, cleaned, write_remove_list):
    rl = write_remove_list([["code-go", "train", "code-go/part-00001.parquet", 0, "g0"]])
    out = tmp_path / "deduped"
    ad.apply(cleaned, rl, out)
    assert ids(out / "train" / "code-go" / "part-00001.parquet") == ["g5", "g6"]
    assert ids(out / "train" / "code-go" / "part-00000.parquet") == ["g0", "g1", "g2", "g3", "g4"]


def test_empty_remove_list_copies_everything(tmp_path, cleaned, write_remove_list):
    out = tmp_path / "deduped"
    s = ad.apply(cleaned, write_remove_list([]), out)
    assert s["totals"] == {"rows": 13, "removed": 0, "kept": 13}
    assert all(p["copied"] for p in s["parts"])


def test_windows_style_part_path_matches(tmp_path, cleaned, write_remove_list):
    rl = write_remove_list([["code-go", "train", "code-go\\part-00000.parquet", 2, "g2"]])
    out = tmp_path / "deduped"
    ad.apply(cleaned, rl, out)
    assert "g2" not in ids(out / "train" / "code-go" / "part-00000.parquet")


@pytest.mark.parametrize("row, message", [
    (["en-dclm", "train", "en-dclm/part-00000.parquet", 1, "WRONG"], "doc_id"),
    (["code-go", "train", "en-dclm/part-00000.parquet", 1, "e1"], "pack_id"),
    (["en-dclm", "train", "en-dclm/part-00009.parquet", 0, "e0"], "not found"),
    (["en-dclm", "train", "en-dclm/part-00000.parquet", 99, "e0"], "row"),
    (["code-go", "heldout", "code-go/part-00000.parquet", 0, "h0"], "held-out"),
    (["en-dclm", "valid", "en-dclm/part-00000.parquet", 0, "e0"], "split"),
    (["en-dclm", "train", "en-dclm/part-00000.parquet", -1, "e0"], "row_in_part"),
    (["en-dclm", "train", "en-dclm/part-00000.parquet", "x", "e0"], "row_in_part"),
])
def test_stops_and_writes_nothing(tmp_path, cleaned, write_remove_list, row, message):
    # a good row in the first part processed (code-go) and the bad one in the last (en-dclm): a run that checked each
    # part just before writing it would already have written code-go when it reached the bad row
    rl = write_remove_list([["code-go", "train", "code-go/part-00000.parquet", 0, "g0"], row])
    out = tmp_path / "deduped"
    with pytest.raises(ad.Stop, match=message):
        ad.apply(cleaned, rl, out)
    assert not out.exists() or not any(out.rglob("*"))


def test_unlisted_part_without_pack_id_stops_before_writing(tmp_path, cleaned, write_remove_list):
    path = cleaned / "train" / "en-dclm" / "part-00000.parquet"
    pq.write_table(pq.read_table(path).drop(["pack_id"]), path)
    out = tmp_path / "deduped"
    with pytest.raises(ad.Stop, match="no pack_id column"):
        ad.apply(cleaned, write_remove_list([["code-go", "train", "code-go/part-00000.parquet", 0, "g0"]]), out)
    assert not out.exists() or not any(out.rglob("*"))


def test_row_groups_boundaries_and_codec_are_kept(tmp_path, write_remove_list):
    import pyarrow as pa
    root = tmp_path / "big"
    path = root / "train" / "sci" / "part-00000.parquet"
    path.parent.mkdir(parents=True)
    rows = [{"doc_id": f"d{i}", "text": f"t{i}", "pack_id": "sci"} for i in range(2500)]
    pq.write_table(pa.Table.from_pylist(rows), path, row_group_size=700, compression="zstd")
    gone = [0, 699, 700, 701, 1399, 1400, 2499]
    rl = write_remove_list([["sci", "train", "sci/part-00000.parquet", r, f"d{r}"] for r in gone])
    out = tmp_path / "deduped"
    ad.apply(root, rl, out, splits=("train",))
    got = out / "train" / "sci" / "part-00000.parquet"
    assert ids(got) == [f"d{i}" for i in range(2500) if i not in gone]
    md = pq.ParquetFile(got).metadata
    assert md.num_row_groups == 4 and md.row_group(0).column(0).compression == "ZSTD"


def test_stops_on_duplicate_rows(tmp_path, cleaned, write_remove_list):
    row = ["code-go", "train", "code-go/part-00000.parquet", 1, "g1"]
    with pytest.raises(ad.Stop, match="twice"):
        ad.apply(cleaned, write_remove_list([row, row]), tmp_path / "deduped")


def test_stops_on_wrong_header(tmp_path, cleaned, write_remove_list):
    rl = write_remove_list([], header=["doc_id", "pack_id"])
    with pytest.raises(ad.Stop, match="header"):
        ad.apply(cleaned, rl, tmp_path / "deduped")


def test_stops_when_out_is_inside_cleaned(cleaned, write_remove_list):
    with pytest.raises(ad.Stop, match="overlap"):
        ad.apply(cleaned, write_remove_list([]), cleaned / "deduped")


def test_rerun_skips_finished_parts(tmp_path, cleaned, write_remove_list):
    rl = write_remove_list([["code-go", "train", "code-go/part-00000.parquet", 1, "g1"]])
    out = tmp_path / "deduped"
    ad.apply(cleaned, rl, out)
    part = out / "train" / "code-go" / "part-00000.parquet"
    mtime = part.stat().st_mtime_ns
    s = ad.apply(cleaned, rl, out)
    assert part.stat().st_mtime_ns == mtime
    assert all(p["skipped"] for p in s["parts"])
    assert s["totals"]["removed"] == 1


def test_rerun_redoes_a_changed_output(tmp_path, cleaned, write_remove_list):
    rl = write_remove_list([["code-go", "train", "code-go/part-00000.parquet", 1, "g1"]])
    out = tmp_path / "deduped"
    ad.apply(cleaned, rl, out)
    part = out / "train" / "code-go" / "part-00000.parquet"
    part.write_bytes(b"corrupted")
    s = ad.apply(cleaned, rl, out)
    assert ids(part) == ["g0", "g2", "g3", "g4"]
    assert {p["part"]: p["skipped"] for p in s["parts"] if p["split"] == "train"}["code-go/part-00000.parquet"] is False


def test_stops_on_stale_outputs(tmp_path, cleaned, write_remove_list):
    out = tmp_path / "deduped"
    ad.apply(cleaned, write_remove_list([]), out)
    stale = out / "train" / "old-pack" / "part-00000.parquet"
    stale.parent.mkdir(parents=True)
    stale.write_bytes((out / "train" / "en-dclm" / "part-00000.parquet").read_bytes())
    with pytest.raises(ad.Stop, match="earlier run"):
        ad.apply(cleaned, write_remove_list([], name="again.csv"), out)


def test_train_only(tmp_path, cleaned, write_remove_list):
    import shutil
    shutil.rmtree(cleaned / "heldout")
    s = ad.apply(cleaned, write_remove_list([["code-go", "train", "code-go/part-00000.parquet", 1, "g1"]]),
                 tmp_path / "deduped", splits=("train",))
    assert s["totals"] == {"rows": 11, "removed": 1, "kept": 10}


def test_summary_has_ids_and_hashes_only(tmp_path, cleaned, write_remove_list):
    rl = write_remove_list([["code-go", "train", "code-go/part-00000.parquet", 1, "g1"]])
    out = tmp_path / "deduped"
    ad.apply(cleaned, rl, out)
    text = (out / "apply_dedup_summary.json").read_text(encoding="utf-8")
    assert "synthetic text" not in text
    s = json.loads(text)
    assert s["remove_list"]["sha256"] == sha(rl) and s["remove_list"]["rows"] == 1
    assert len(s["code_sha256"]) == 64
    assert not list(out.rglob("*.tmp"))


def test_cli_exit_code_and_message(tmp_path, cleaned, write_remove_list):
    rl = write_remove_list([["code-go", "heldout", "code-go/part-00000.parquet", 0, "h0"]])
    p = subprocess.run([sys.executable, "-I", str(PIPELINE / "apply_dedup.py"), "--cleaned", str(cleaned),
                        "--remove-list", str(rl), "--out", str(tmp_path / "deduped")], capture_output=True, text=True)
    assert p.returncode == 1 and "held-out" in p.stderr
    ok = write_remove_list([], name="empty.csv")
    p = subprocess.run([sys.executable, "-I", str(PIPELINE / "apply_dedup.py"), "--cleaned", str(cleaned),
                        "--remove-list", str(ok), "--out", str(tmp_path / "deduped2")], capture_output=True, text=True)
    assert p.returncode == 0, p.stderr
