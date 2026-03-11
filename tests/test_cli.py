from pathlib import Path

from coffee_reports.main import main


def test_main_prints_report(monkeypatch, capsys, tmp_path: Path) -> None:
    csv_file = tmp_path / "data.csv"
    csv_file.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Иван,2024-06-01,600,3.0,15,зомби,Математика\n"
        "Иван,2024-06-02,650,2.5,17,зомби,Математика\n"
        "Иван,2024-06-03,700,2.0,18,не выжил,Математика\n"
        "Мария,2024-06-01,100,8.0,3,отл,Математика\n"
        "Мария,2024-06-02,120,8.5,2,отл,Математика\n"
        "Мария,2024-06-03,150,7.5,4,отл,Математика\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "prog",
            "--files",
            str(csv_file),
            "--report",
            "median-coffee",
        ],
    )

    exit_code = main()
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "student" in captured.out
    assert "Иван" in captured.out
    assert "650" in captured.out


def test_main_returns_error_for_unknown_report(monkeypatch, capsys, tmp_path: Path) -> None:
    csv_file = tmp_path / "data.csv"
    csv_file.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Иван,2024-06-01,600,3.0,15,зомби,Математика\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "prog",
            "--files",
            str(csv_file),
            "--report",
            "unknown-report",
        ],
    )

    exit_code = main()
    captured = capsys.readouterr()

    assert exit_code == 1
    assert "Unknown report" in captured.err

def test_main_builds_report_from_multiple_files(monkeypatch, capsys, tmp_path) -> None:
    file1 = tmp_path / "part1.csv"
    file2 = tmp_path / "part2.csv"

    file1.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Иван,2024-06-01,600,3.0,15,зомби,Математика\n"
        "Иван,2024-06-02,650,2.5,17,зомби,Математика\n"
        "Мария,2024-06-01,100,8.0,3,отл,Математика\n",
        encoding="utf-8",
    )
    file2.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Иван,2024-06-03,700,2.0,18,не выжил,Математика\n"
        "Мария,2024-06-02,120,8.5,2,отл,Математика\n"
        "Мария,2024-06-03,150,7.5,4,отл,Математика\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "prog",
            "--files",
            str(file1),
            str(file2),
            "--report",
            "median-coffee",
        ],
    )

    exit_code = main()
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Иван" in captured.out
    assert "650" in captured.out
    assert "Мария" in captured.out
    assert "120" in captured.out