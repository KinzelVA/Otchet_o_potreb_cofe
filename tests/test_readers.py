from pathlib import Path

import pytest

from coffee_reports.readers import read_csv_files


def test_read_csv_files_reads_multiple_files(tmp_path: Path) -> None:
    file1 = tmp_path / "part1.csv"
    file2 = tmp_path / "part2.csv"

    file1.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Алексей,2024-06-01,450,4.5,12,норм,Математика\n",
        encoding="utf-8",
    )
    file2.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Дарья,2024-06-01,200,7.0,6,отл,Математика\n",
        encoding="utf-8",
    )

    rows = read_csv_files([str(file1), str(file2)])

    assert len(rows) == 2
    assert rows[0]["student"] == "Алексей"
    assert rows[1]["student"] == "Дарья"


def test_read_csv_files_raises_for_missing_file(tmp_path: Path) -> None:
    missing_file = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError):
        read_csv_files([str(missing_file)])