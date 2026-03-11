from __future__ import annotations

import sys

from .cli import build_parser
from .readers import read_csv_files
from .registry import get_report
from .renderers import render_table


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        rows = read_csv_files(args.files)
        report = get_report(args.report)
        result = report.build(rows)
        print(render_table(result, report.headers()))
        return 0
    except (FileNotFoundError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())