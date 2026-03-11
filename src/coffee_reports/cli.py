from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build reports from CSV files with students session data."
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to CSV files.",
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Report name to build.",
    )
    return parser