from __future__ import annotations

from tabulate import tabulate


def render_table(rows: list[dict[str, object]], headers: list[str]) -> str:
    return tabulate(rows, headers="keys", tablefmt="simple")