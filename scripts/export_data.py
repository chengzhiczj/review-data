"""Refresh the four spreadsheet views after intentionally editing the master JSON.

This command is for preparing a new release, not for verifying the original.
It does not change the manuscript assertions or input checksum manifest.
"""
from .common import (ROOT, coding_record, evaluation_records, extraction_record,
                     publication_record, read_studies, write_csv)


def export():
    studies = read_studies()
    for filename, rows in [
        ('study_coding.csv', [coding_record(s) for s in studies]),
        ('study_extraction.csv', [extraction_record(s) for s in studies]),
        ('publication_metadata.csv', [publication_record(s) for s in studies]),
        ('evaluation_decisions.csv', evaluation_records(studies)),
    ]:
        write_csv(ROOT / 'data' / filename, rows)
    print('Refreshed four data CSV views from data/studies.json.')


if __name__ == '__main__':
    export()
