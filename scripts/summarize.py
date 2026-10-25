"""Recompute the review's descriptive statistics from the release data."""
from collections import Counter
from pathlib import Path

from .common import (DIMENSIONS, FAMILIES, INTEGRATION, REASONING, RESOURCES,
                     RETRIEVAL, STAGES, STAGE_CODES, coding_record,
                     evaluation_records, extraction_record, publication_record,
                     write_csv, write_json)


def summarize(studies):
    n = len(studies)
    coding = [s['coding'] for s in studies]
    counts = lambda field, labels: {label: sum(label in c[field] for c in coding) for label in labels}
    matrix = lambda field, labels: [[sum(c['principal_contribution'] == stage and label in c[field]
                                       for c in coding) for label in labels] for stage in STAGES]
    patch = [s for s in studies if 'Patch' in s['coding']['task_families']]
    evaluation = {}
    for dimension in DIMENSIONS:
        positive = [s for s in studies if s['evaluation'][dimension]['reported_assessment']]
        record = {'count': len(positive), 'denominator': n, 'percent': round(100 * len(positive) / n, 1),
                  'studies': [s['name'] for s in positive]}
        if dimension in ['functional_correctness', 'post_repair_security']:
            record.update(patch_denominator=len(patch), patch_percent=round(100 * len(positive) / len(patch), 1))
        evaluation[dimension] = record
    judged = [s['name'] for s in studies if s['evaluation']['retrieval_relevance']['reported_assessment']
              and s['evaluation']['retrieval_relevance']['status'] != 'similarity_proxy']
    tool_checks = [s['name'] for s in studies if s['evaluation']['post_repair_security']['status']
                   in ['static_analysis', 'execution_tests']]
    return {
        'n': n,
        'publication_years': dict(sorted(Counter(str(s['publication']['review_year']) for s in studies).items())),
        'publication_types': {kind: sum(s['publication']['review_publication_type'] == kind for s in studies)
                              for kind in ['journal', 'conference', 'preprint']},
        'principal': {stage: sum(c['principal_contribution'] == stage for c in coding) for stage in STAGES},
        'coverage': counts('lifecycle_coverage', STAGE_CODES),
        'stage_cardinality': {str(k): sum(len(c['lifecycle_coverage']) == k for c in coding) for k in [1, 2, 3]},
        'cross_stage': sum(len(c['lifecycle_coverage']) > 1 for c in coding),
        'task_families': counts('task_families', FAMILIES),
        'resources': counts('knowledge_resources', RESOURCES),
        'retrieval': counts('retrieval_components', RETRIEVAL),
        'integration': {route: sum(c['integration_route'] == route for c in coding) for route in INTEGRATION},
        'reasoning': {mode: sum(c['reasoning_mode'] == mode for c in coding) for mode in REASONING},
        'contrastive_comparison': sum(c['contrastive_comparison'] for c in coding),
        'repeated_conditioning': sum(c['repeated_conditioning'] for c in coding),
        'task_matrix': matrix('task_families', FAMILIES),
        'resource_matrix': matrix('knowledge_resources', RESOURCES),
        'retrieval_matrix': matrix('retrieval_components', RETRIEVAL),
        'integration_matrix': [[sum(c['principal_contribution'] == stage and c['integration_route'] == route
                                     for c in coding) for route in INTEGRATION] for stage in STAGES],
        'reasoning_matrix': [[sum(c['principal_contribution'] == stage and
                                 (c['contrastive_comparison'] if mode == 'CR' else c['reasoning_mode'] == mode)
                                 for c in coding) for mode in REASONING + ['CR']] for stage in STAGES],
        'evaluation': evaluation,
        'retrieval_with_judgment_or_gold_match': judged,
        'post_repair_security_tool_or_test': tool_checks,
        'patch_studies': [s['name'] for s in patch],
    }


def export_results(studies, output):
    output = Path(output)
    stats = summarize(studies)
    write_json(output / 'statistics.json', stats)
    write_csv(output / 'study_coding.csv', [coding_record(s) for s in studies])
    write_csv(output / 'study_extraction.csv', [extraction_record(s) for s in studies])
    write_csv(output / 'publication_metadata.csv', [publication_record(s) for s in studies])
    write_csv(output / 'evaluation_decisions.csv', evaluation_records(studies))
    rows = []
    for category in ['publication_years', 'publication_types', 'principal', 'coverage', 'task_families',
                     'resources', 'retrieval', 'integration', 'reasoning']:
        rows.extend({'dimension': category, 'code': code, 'count': count,
                     'denominator': stats['n'], 'percent': round(100 * count / stats['n'], 1)}
                    for code, count in stats[category].items())
    for field in ['cross_stage', 'contrastive_comparison', 'repeated_conditioning']:
        rows.append({'dimension': field, 'code': field, 'count': stats[field],
                     'denominator': stats['n'], 'percent': round(100 * stats[field] / stats['n'], 1)})
    write_csv(output / 'summary_counts.csv', rows)
    write_csv(output / 'evaluation_coverage.csv', [{'dimension': dimension, **record}
              for dimension, record in stats['evaluation'].items()],
              ['dimension', 'count', 'denominator', 'percent', 'studies', 'patch_denominator', 'patch_percent'])
    for filename, labels, key in [
        ('task_families.csv', FAMILIES, 'task_matrix'),
        ('knowledge_resources.csv', RESOURCES, 'resource_matrix'),
        ('retrieval_components.csv', RETRIEVAL, 'retrieval_matrix'),
        ('integration_routes.csv', INTEGRATION, 'integration_matrix'),
        ('reasoning_modes.csv', REASONING + ['CR'], 'reasoning_matrix'),
    ]:
        write_csv(output / 'figure_data' / filename,
                  [{'principal_contribution': stage, **dict(zip(labels, values))}
                   for stage, values in zip(STAGES, stats[key])])
    write_csv(output / 'figure_data/lifecycle_distribution.csv',
              [{'stage': stage, 'principal_count': stats['principal'][stage],
                'coverage_count': stats['coverage'][code], 'denominator': stats['n']}
               for stage, code in zip(STAGES, STAGE_CODES)])
    markdown = ['# Recomputed descriptive results', '', '| Dimension | Count | Corpus denominator |',
                '|---|---:|---:|']
    markdown.extend(f"| {row['dimension']}: {row['code']} | {row['count']} | {row['denominator']} |" for row in rows)
    markdown += ['', 'Repair measures also use the five Patch-family studies as the applicable denominator.', '']
    (output / 'summary.md').write_text('\n'.join(markdown), encoding='utf-8')
    lines = [r'\begin{tabular}{lrr}', r'\hline', r'Dimension & Count & Denominator \\', r'\hline']
    lines += [row['dimension'].replace('_', r'\_') + ': ' + row['code'].replace('_', r'\_') +
              f" & {row['count']} & {row['denominator']}" + r' \\' for row in rows]
    lines += [r'\hline', r'\end{tabular}', '']
    (output / 'summary_counts.tex').write_text('\n'.join(lines), encoding='utf-8')
    return stats
