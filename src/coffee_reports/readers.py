from __future__ import annotations

import csv
from pathlib import Path


def read_csv_files(file_paths: list[str]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    for file_path in file_paths:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        with path.open("r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            rows.extend(reader)

    return rows