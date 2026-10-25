"""Validate the release and regenerate its CSV tables, statistics, and figures."""
from pathlib import Path
import argparse
import json
import sys

from scripts.common import ROOT, read_studies, write_json
from scripts.summarize import export_results
from scripts.validate import validate
from scripts.reports import render_reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only', action='store_true', help='Validate inputs without regenerating figures.')
    parser.add_argument('--output', type=Path, default=ROOT / 'results', help='Result directory, default: results/.')
    args = parser.parse_args()
    report = validate()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if not report['passed']:
        return 1
    if args.check_only:
        return 0
    studies = read_studies()
    stats = export_results(studies, args.output)
    render_reports(studies, args.output)
    from scripts.plot_figures import generate_all
    generated = generate_all(studies, stats, args.output / 'figures')
    write_json(args.output / 'validation.json', report)
    print('Recomputed all 31 studies and', len(generated), 'figure PDFs.')
    print('Results:', args.output.resolve())
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
