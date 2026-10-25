"""Build readable study records and a linked six-dimension evidence report."""
from pathlib import Path
import json

from .common import DIMENSIONS, ROOT


def evidence_links(ids):
    return ', '.join(f'[{eid}](source_excerpts.md#{eid.lower()})' for eid in ids) or 'Not applicable'


def render_reports(studies, output):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    excerpts = [json.loads(line) for line in
                (ROOT / 'evidence/excerpts.jsonl').read_text(encoding='utf-8').splitlines()]
    evidence = ['# Primary-text evidence excerpts', '',
                'Line ranges are one-based and inclusive in the hashed source text listed in `evidence/source_index.csv`.', '']
    for e in excerpts:
        evidence += [f'<a id="{e["evidence_id"].lower()}"></a>', '',
                     f'## {e["evidence_id"]}: {e["study_id"]} / {e["citation_key"]}', '',
                     f'Source: `{e["text_filename"]}`, lines {e["start_line"]}-{e["end_line"]}.', '',
                     'Uses: ' + ', '.join(e['purposes']) + '.', '',
                     '```text', e['text'], '```', '']
    (output / 'source_excerpts.md').write_text('\n'.join(evidence), encoding='utf-8')
    records = ['# Study-level extraction and coding records', '',
               'One section per primary study. Publication statistics use the cutoff fields. '
               'The bibliography fields identify the cited version.', '']
    audit = ['# Six-dimension evaluation audit', '',
             'The unit is one reported evaluation per study and dimension. '
             '`not_reported` does not imply the absence of a system capability. '
             'Repair dimensions apply to the five Patch-family studies. Similarity proxies remain explicitly labeled.', '',
             '| Study | Retrieval relevance | Context recall | Provenance | Claim faithfulness | Functional correctness | Post-repair security |',
             '|---|---|---|---|---|---|---|']
    for s in studies:
        statuses = [s['evaluation'][d]['status'] for d in DIMENSIONS]
        audit.append('| ' + ' | '.join([f'[{s["name"]}](#{s["study_id"].lower()})', *statuses]) + ' |')
    for s in studies:
        records += [f'## {s["study_id"]}: {s["name"]}', '',
                    f'Citation key: `{s["citation_key"]}`.', '', s['publication']['title'], '',
                    f"Cutoff year/type: {s['publication']['review_year']} / {s['publication']['review_publication_type']}.", '',
                    f"Cited version: {s['publication']['bibliography_year']}, {s['publication']['venue']}.", '']
        if s['publication']['doi']:
            records += ['DOI: ' + s['publication']['doi'] + '.', '']
        records += ['### Coding', '']
        for field, value in s['coding'].items():
            rendered = ', '.join(value) if isinstance(value, list) else str(value)
            records.append(f'- **{field.replace("_", " ")}**: {rendered or "None"}')
        records += ['', '### Extraction', '']
        for field, value in s['extraction'].items():
            records += [f'**{field.replace("_", " ").capitalize()}.** {value}', '']
        records += ['Extraction source locators: ' + evidence_links(s['source_evidence_ids']) + '.', '']
        audit += ['', f'<a id="{s["study_id"].lower()}"></a>', '', f'## {s["study_id"]}: {s["name"]}', '']
        for dimension in DIMENSIONS:
            item = s['evaluation'][dimension]
            audit += [f'### {dimension}', '',
                      f"Status: `{item['status']}`. Reported assessment: {item['reported_assessment']}. Applicable: {item['applicable']}.", '',
                      item['reason'], '', 'Evidence: ' + evidence_links(item['evidence_ids']) + '.', '']
    (output / 'study_records.md').write_text('\n'.join(records), encoding='utf-8')
    (output / 'evaluation_audit.md').write_text('\n'.join(audit), encoding='utf-8')
