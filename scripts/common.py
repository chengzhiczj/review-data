"""Shared schema, file handling, and manuscript-table readers."""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
STAGES = ['Discovery', 'Analysis', 'Mitigation']
STAGE_CODES = ['D', 'A', 'M']
FAMILIES = ['Identify', 'Test', 'Characterize', 'Verify', 'Recommend', 'Patch']
FAMILY_STAGE = dict(zip(FAMILIES, ['D', 'D', 'A', 'A', 'M', 'M']))
RESOURCES = ['VR', 'Code', 'Context']
RETRIEVAL = ['SR', 'DR', 'HR', 'GSR', 'RTR']
INTEGRATION = ['Context', 'Workflow', 'Feature']
REASONING = ['CoT', 'GR', 'HSR', 'MAR', 'DG']
DIMENSIONS = ['retrieval_relevance', 'context_recall', 'provenance',
              'claim_faithfulness', 'functional_correctness', 'post_repair_security']


def load_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def write_csv(path, rows, fields=None):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if fields is None:
        fields = list(rows[0]) if rows else []
    with path.open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: '; '.join(str(x) for x in value) if isinstance(value, list)
                             else value for key, value in row.items()})


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_studies(root=ROOT):
    return load_json(Path(root) / 'data/studies.json')['studies']


def plain_latex(text):
    from pylatexenc.latex2text import LatexNodes2Text
    text = re.sub(r'\\(?:cite\w*|ref|label)\{[^}]*\}', '', text)
    return re.sub(r'\s+', ' ', LatexNodes2Text().latex_to_text(text)).strip()


def manuscript_tables(text):
    tables = {}
    for match in re.finditer(r'\\begin\{(table\*?)\}[\s\S]*?\\end\{\1\}', text):
        label = re.search(r'\\label\{([^}]+)\}', match[0])
        if label:
            tables[label[1]] = match[0]
    return tables


def study_cells(table, name, key):
    prefix = name + r'~\cite{' + key + '}'
    pattern = r'(?m)^' + re.escape(prefix) + r'\s*&([\s\S]*?)\\\\'
    matches = list(re.finditer(pattern, table))
    if len(matches) != 1:
        raise ValueError('Expected one table row for ' + name)
    return [cell.strip() for cell in matches[0][1].split('&')]


def publication_record(study):
    return {'study_id': study['study_id'], 'study': study['name'], 'citation_key': study['citation_key'],
            **study['publication']}


def coding_record(study):
    return {'study_id': study['study_id'], 'study': study['name'], 'citation_key': study['citation_key'],
            **study['coding']}


def extraction_record(study):
    return {'study_id': study['study_id'], 'study': study['name'], 'citation_key': study['citation_key'],
            **study['extraction']}


def evaluation_records(studies):
    return [{'study_id': s['study_id'], 'study': s['name'], 'citation_key': s['citation_key'],
             'dimension': dimension, **s['evaluation'][dimension]}
            for s in studies for dimension in DIMENSIONS]
