"""Validate release assertions, record coding, evidence, and file integrity."""
from pathlib import Path
import csv
import json
import re

from .common import (DIMENSIONS, FAMILIES, FAMILY_STAGE, INTEGRATION, REASONING,
                     RESOURCES, RETRIEVAL, ROOT, STAGES, coding_record, load_json,
                     evaluation_records, extraction_record, publication_record,
                     read_studies, sha256)
from .summarize import summarize


def verify_manifest(root=ROOT):
    root = Path(root)
    errors = []
    for line in (root / 'MANIFEST.sha256').read_text(encoding='utf-8').splitlines():
        expected, relative = line.split('  ', 1)
        path = root / relative
        if not path.is_file() or sha256(path) != expected:
            errors.append('File checksum mismatch: ' + relative)
    return errors


def validate(root=ROOT):
    root = Path(root)
    studies = read_studies(root)
    errors = verify_manifest(root)
    def require(condition, message):
        if not condition:
            errors.append(message)
    require(len(studies) == 31, 'Expected 31 studies')
    for field in ['study_id', 'name', 'citation_key']:
        require(len({s[field] for s in studies}) == len(studies), 'Duplicate ' + field)
    for filename, rows in [
        ('study_coding.csv', [coding_record(s) for s in studies]),
        ('study_extraction.csv', [extraction_record(s) for s in studies]),
        ('publication_metadata.csv', [publication_record(s) for s in studies]),
        ('evaluation_decisions.csv', evaluation_records(studies)),
    ]:
        with (root / 'data' / filename).open(encoding='utf-8-sig', newline='') as stream:
            actual_rows = list(csv.DictReader(stream))
        serialized = [{key: '; '.join(str(x) for x in value) if isinstance(value, list) else str(value)
                       for key, value in row.items()} for row in rows]
        require(actual_rows == serialized, 'CSV/master mismatch: ' + filename)
    expected = load_json(root / 'data/expected_results.json')
    stats = summarize(studies)
    for field, value in expected.items():
        actual = stats[field]
        if field == 'evaluation':
            actual = {dimension: record['count'] for dimension, record in actual.items()}
        require(actual == value, 'Manuscript count mismatch: ' + field)
    excerpt_rows = [json.loads(line) for line in (root / 'evidence/excerpts.jsonl').read_text(encoding='utf-8').splitlines()]
    excerpts = {item['evidence_id']: item for item in excerpt_rows}
    require(len(excerpts) == len(excerpt_rows), 'Duplicate evidence ID')
    with (root / 'evidence/source_index.csv').open(encoding='utf-8-sig', newline='') as stream:
        source_index = {item['source_id']: item for item in csv.DictReader(stream)}
    codebook = load_json(root / 'data/codebook.json')
    for s in studies:
        name, key, c = s['name'], s['citation_key'], s['coding']
        require(c['principal_contribution'] in STAGES, 'Invalid principal stage: ' + name)
        require(set(c['task_families']) <= set(FAMILIES), 'Invalid task family: ' + name)
        require(set(c['lifecycle_coverage']) == {FAMILY_STAGE[f] for f in c['task_families']}, 'Stage/output mismatch: ' + name)
        require(set(c['supporting_stage_outputs']) <= set(c['lifecycle_coverage']), 'Invalid supporting stage: ' + name)
        require(set(c['knowledge_resources']) <= set(RESOURCES), 'Invalid resource: ' + name)
        require(set(c['retrieval_components']) <= set(RETRIEVAL), 'Invalid retrieval label: ' + name)
        require('HR' not in c['retrieval_components'] or {'SR', 'DR'} <= set(c['retrieval_components']), 'Hybrid components missing: ' + name)
        require(c['integration_route'] in INTEGRATION and c['reasoning_mode'] in REASONING, 'Invalid integration or reasoning: ' + name)
        require(isinstance(c['repeated_conditioning'], bool) and isinstance(c['contrastive_comparison'], bool), 'Invalid Boolean coding: ' + name)
        require(s['publication']['review_year'] in [2024, 2025, 2026], 'Review year outside window: ' + name)
        require(s['publication']['review_publication_type'] in ['journal', 'conference', 'preprint'], 'Invalid publication type: ' + name)
        require(set(s['evaluation']) == set(DIMENSIONS), 'Missing evaluation dimension: ' + name)
        patch = 'Patch' in c['task_families']
        for dimension, item in s['evaluation'].items():
            require(item['status'] in codebook['evaluation_statuses'][dimension], 'Invalid evaluation status: ' + name)
            require(item['reported_assessment'] == (item['status'] not in ['not_reported', 'not_applicable']), 'Assessment/status mismatch: ' + name + '/' + dimension)
            if dimension in ['functional_correctness', 'post_repair_security']:
                require(item['applicable'] == patch and (item['status'] == 'not_applicable') == (not patch), 'Repair denominator mismatch: ' + name)
            for evidence_id in item['evidence_ids']:
                require(evidence_id in excerpts and excerpts[evidence_id]['study_id'] == s['study_id'], 'Invalid evaluation evidence: ' + name)
        for evidence_id in s['source_evidence_ids']:
            require(evidence_id in excerpts and excerpts[evidence_id]['study_id'] == s['study_id'], 'Invalid extraction evidence: ' + name)
    primary_keys = set(re.findall(r'(?m)^@\w+\s*\{\s*([^,\s]+)', (root / 'references/primary_studies.bib').read_text(encoding='utf-8')))
    require(primary_keys == {s['citation_key'] for s in studies}, 'Primary bibliography must contain exactly the 31 study keys')
    require(not (root / 'manuscript').exists(), 'The shared data package must not contain a manuscript folder')
    require((root / 'assets/lifecycle.pdf').is_file(), 'Missing lifecycle illustration asset')
    for item in excerpts.values():
        require(item['start_line'] >= 1 and item['end_line'] >= item['start_line'] and bool(item['text'].strip()), 'Invalid excerpt span')
        source = source_index.get(item['source_id'], {})
        require(source.get('study_id') == item['study_id'] and source.get('sha256') == item['source_sha256'], 'Excerpt/source-index mismatch')
        require(len(item['text'].split('\n')) == item['end_line'] - item['start_line'] + 1, 'Excerpt line-count mismatch: ' + item['evidence_id'])
    method = load_json(root / 'data/review_method_summary.json')
    flow = method['screening_flow']
    require(flow['database_records'] - flow['duplicates_removed'] == flow['unique_records'], 'Deduplication flow mismatch')
    require(flow['unique_records'] - flow['title_abstract_excluded'] == flow['database_full_text'], 'Abstract screening flow mismatch')
    require(flow['database_full_text'] - flow['full_text_excluded'] == flow['database_included'], 'Full-text flow mismatch')
    require(flow['database_included'] + flow['snowball_included'] == flow['final_included'] == len(studies), 'Final inclusion flow mismatch')
    protocol = load_json(root / 'data/search_protocol.json')
    require(protocol['reported_screening_flow'] == flow, 'Search-protocol aggregate counts mismatch')
    require(protocol['search_period'] == method['review_cutoff'], 'Search-protocol cutoff mismatch')
    require(len(protocol['sources']) == 8 and len(protocol['concept_blocks']) == 5, 'Incomplete documented search protocol')
    for field, prefix, count in [('inclusion_criteria', 'IC', 6), ('exclusion_criteria', 'EC', 9)]:
        require([row['id'] for row in protocol['screening'][field]] == [prefix + str(i) for i in range(1, count + 1)], 'Eligibility-criterion inventory mismatch')
    return {'passed': not errors, 'studies': len(studies), 'evaluation_decisions': len(studies) * len(DIMENSIONS),
            'source_excerpts': len(excerpts), 'primary_references': len(primary_keys), 'errors': errors}


if __name__ == '__main__':
    report = validate()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report['passed'] else 1)
