from __future__ import annotations

from collections import defaultdict
from statistics import median
from typing import Iterable

from coffee_reports.report_base import Report


class MedianCoffeeReport(Report):
    name = "median-coffee"

    def build(self, rows: Iterable[dict[str, str]]) -> list[dict[str, object]]:
        grouped: dict[str, list[int]] = defaultdict(list)

        for row in rows:
            student = row["student"]
            coffee_spent = int(row["coffee_spent"])
            grouped[student].append(coffee_spent)

        result = [
            {
                "student": student,
                "median_coffee_spent": float(median(spent_values)),
            }
            for student, spent_values in grouped.items()
        ]

        result.sort(key=lambda item: item["median_coffee_spent"], reverse=True)
        return result

    def headers(self) -> list[str]:
        return ["student", "median_coffee_spent"]