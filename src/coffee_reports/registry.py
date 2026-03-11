from __future__ import annotations

from .report_base import Report
from .reports.median_coffee import MedianCoffeeReport


def get_report(report_name: str) -> Report:
    reports: dict[str, type[Report]] = {
        MedianCoffeeReport.name: MedianCoffeeReport,
    }

    try:
        return reports[report_name]()
    except KeyError as error:
        available = ", ".join(sorted(reports))
        raise ValueError(
            f"Unknown report: {report_name}. Available reports: {available}"
        ) from error