"""Regenerate six coded-data charts, the RAG diagram, and the screening flow.

The lifecycle illustration is supplied as the author's original static vector
asset and is copied without alteration. All outputs stay inside the requested
result directory; manuscript assets are never overwritten.
"""
from pathlib import Path
import shutil

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np
import pymupdf

from .common import FAMILIES, INTEGRATION, REASONING, RETRIEVAL, ROOT, STAGES, load_json

COLORS = ['#0072B2', '#E69F00', '#009E73']
STYLE = {'font.family': 'DejaVu Sans', 'font.size': 10, 'pdf.fonttype': 42,
         'axes.spines.top': False, 'axes.spines.right': False}
PDF_METADATA = {'Creator': 'Software vulnerability RAG SLR replication package',
                'CreationDate': None, 'ModDate': None}


def save(fig, out, name, tight=True, dpi=180):
    options = {'bbox_inches': 'tight'} if tight else {}
    fig.savefig(Path(out) / (name + '.pdf'), metadata=PDF_METADATA, **options)
    fig.savefig(Path(out) / (name + '.png'), dpi=dpi, **options)
    plt.close(fig)


def publication(stats, out):
    years = sorted(stats['publication_years'])
    counts = [stats['publication_years'][year] for year in years]
    fig, ax = plt.subplots(figsize=(6.2, 3.3))
    bars = ax.bar(np.arange(len(years)), counts, width=.58, color=COLORS[0])
    ax.bar_label(bars, padding=3)
    ax.set_xticks(np.arange(len(years)), years)
    ax.set_ylabel('Number of studies')
    ax.set_ylim(0, max(counts) + 4)
    ax.set_yticks(range(0, max(counts) + 5, 5))
    fig.tight_layout()
    save(fig, out, 'pub_year')

    counts = [stats['publication_types'][key] for key in ['journal', 'conference', 'preprint']]
    fig, ax = plt.subplots(figsize=(5.8, 2.7))
    bars = ax.barh(['Journal', 'Conference', 'Preprint'], counts, color=COLORS)
    ax.bar_label(bars, labels=[f'{value} ({100 * value / stats["n"]:.1f}%)' for value in counts], padding=5)
    ax.set_xlim(0, 21)
    ax.set_xlabel('Number of studies')
    ax.invert_yaxis()
    fig.tight_layout()
    save(fig, out, 'pub_venue_type')


def lifecycle_distribution(stats, out):
    fig, ax = plt.subplots(figsize=(6.3, 3.6))
    y, height = np.arange(3), .32
    principal = [stats['principal'][stage] for stage in STAGES]
    coverage = [stats['coverage'][code] for code in ['D', 'A', 'M']]
    for offset, counts, label, color in [(-height / 2, principal, 'Principal contribution', COLORS[0]),
                                         (height / 2, coverage, 'Non-exclusive coverage', COLORS[1])]:
        bars = ax.barh(y + offset, counts, height, label=label, color=color)
        ax.bar_label(bars, labels=[f'{value}/{stats["n"]} ({100 * value / stats["n"]:.1f}%)' for value in counts],
                     padding=4, fontsize=9)
    ax.set_yticks(y, STAGES)
    ax.set_xlim(0, 32)
    ax.set_xticks([0, 10, 20, 30])
    ax.set_xlabel('Number of studies')
    ax.invert_yaxis()
    ax.legend(frameon=False, loc='lower right')
    fig.tight_layout()
    save(fig, out, 'pie_distribution')


def knowledge_resources(stats, out):
    fig, ax = plt.subplots(figsize=(6.2, 3.6))
    x, bottom = np.arange(3), np.zeros(3)
    for stage, counts, color in zip(STAGES, stats['resource_matrix'], COLORS):
        bars = ax.bar(x, counts, .6, bottom=bottom, label=stage, color=color)
        ax.bar_label(bars, labels=[str(value) if value else '' for value in counts],
                     label_type='center', color='white')
        bottom += np.asarray(counts)
    ax.set_xticks(x, ['Reference (VR)', 'Code', 'Context / procedure'])
    ax.set_ylabel('Number of studies')
    ax.set_ylim(0, 26)
    ax.legend(frameon=False, loc='upper right')
    fig.tight_layout()
    save(fig, out, 'knowledge_bar')


def task_taxonomy(stats, out):
    matrix = np.asarray(stats['task_matrix'])
    fig, ax = plt.subplots(figsize=(7.0, 2.8))
    ax.imshow(matrix, cmap='Blues', vmin=0, vmax=16, aspect='auto')
    ax.set_xticks(range(len(FAMILIES)), FAMILIES, rotation=35, ha='right')
    ax.set_yticks(range(3), STAGES)
    for (i, j), value in np.ndenumerate(matrix):
        ax.text(j, i, str(value), ha='center', va='center', color='white' if value >= 9 else 'black', fontsize=12)
    ax.set_title('Non-exclusive task-family counts', fontsize=12)
    ax.spines[:].set_visible(False)
    fig.tight_layout()
    save(fig, out, 'task_taxonomy', dpi=300)


def rag_settings(stats, out):
    groups = [(RETRIEVAL, 'Retrieval components', stats['retrieval_matrix']),
              (INTEGRATION, 'Principal integration', stats['integration_matrix']),
              (REASONING + ['CR'], 'Reasoning mode / contrast', stats['reasoning_matrix'])]
    fig, axes = plt.subplots(1, 3, figsize=(13, 3.4), gridspec_kw={'width_ratios': [5, 3, 6]})
    for index, (ax, (labels, title, matrix)) in enumerate(zip(axes, groups)):
        matrix = np.asarray(matrix)
        ax.imshow(matrix, cmap='Blues', vmin=0, vmax=14, aspect='auto')
        ax.set_xticks(range(len(labels)), labels, rotation=35, ha='right')
        ax.set_yticks(range(3), STAGES if index == 0 else ['', '', ''])
        ax.set_title(title)
        for (i, j), value in np.ndenumerate(matrix):
            ax.text(j, i, str(value), ha='center', va='center', color='white' if value >= 8 else 'black')
        ax.spines[:].set_visible(False)
    fig.tight_layout()
    save(fig, out, 'rag_settings_heatmap')


def rag_framework(out):
    fig = plt.figure(figsize=(3.44, 5.10))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis('off')
    left, right, center = .035, .875, .455
    panels = [
        (.785, .192, '#0072B2', '#EEF6FB', '1  External knowledge',
         ['Vulnerability records and taxonomies', 'Code, patches, and program relations',
          'Reports, advisories, and documentation']),
        (.525, .214, '#0072B2', '#EEF6FB', '2  Task-specific evidence selection',
         ['Query: code, question, or intermediate state', 'Lexical / dense / hybrid retrieval',
          'Graph, repository, or tool-based lookup', 'Filtering and reranking, where implemented']),
        (.265, .214, '#E69F00', '#FFF7E8', '3  Evidence integration and reasoning',
         ['Contextual generation / workflow integration', 'Feature/model integration',
          'Direct, chain-of-thought, graph,', 'staged, or multi-agent generation']),
        (.023, .196, '#009E73', '#EDF8F4', '4  Lifecycle outputs',
         ['Discovery: findings and test inputs', 'Analysis: characterization and verification',
          'Mitigation: recommendations and patches']),
    ]
    artists = []
    for bottom, height, edge, fill, title, lines in panels:
        ax.add_patch(FancyBboxPatch((left, bottom), right - left, height,
                     boxstyle='round,pad=0.008,rounding_size=0.012', linewidth=.85, edgecolor=edge, facecolor=fill))
        artists.append(ax.text(left + .027, bottom + height - .030, title, fontsize=8.3,
                               fontweight='bold', va='center', color='#263238'))
        artists.append(ax.text(left + .027, bottom + height - .073, '\n'.join(lines), fontsize=7.9,
                               va='top', linespacing=1.48, color='#263238'))
    for lower, upper in [(.739, .785), (.479, .525), (.219, .265)]:
        ax.add_patch(FancyArrowPatch((center, upper - .008), (center, lower + .008),
                     arrowstyle='-|>', mutation_scale=10, lw=1.0, color='#455A64'))
    ax.plot([right + .008, .920, .920], [.121, .121, .628],
            color='#607D8B', lw=.9, linestyle=(0, (3, 2)))
    ax.add_patch(FancyArrowPatch((.920, .628), (right + .008, .628), arrowstyle='-|>',
                 mutation_scale=9, color='#607D8B', lw=.9, linestyle=(0, (3, 2))))
    artists.append(ax.text(.965, .371, 'Optional evidence / validation feedback', rotation=90,
                           ha='center', va='center', fontsize=7.6, color='#455A64'))
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    for artist in artists:
        box = artist.get_window_extent(renderer)
        if not (fig.bbox.contains(box.x0, box.y0) and fig.bbox.contains(box.x1, box.y1)):
            raise ValueError('Diagram text extends beyond the canvas: ' + artist.get_text())
    save(fig, out, 'rag_pipeline', tight=False, dpi=300)


def review_flow(out):
    method = load_json(ROOT / 'data/review_method_summary.json')
    flow = method['screening_flow']
    fig, ax = plt.subplots(figsize=(8.5, 8.4))
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis('off')
    centers = [.92, .78, .64, .50, .32, .10]
    boxes = [
        ('Records identified through\ndatabase searching', flow['database_records']),
        ('Records after duplicate removal', flow['unique_records']),
        ('Title, abstract, and keyword screening', flow['unique_records']),
        ('Full-text studies assessed', flow['database_full_text']),
        ('Studies included from database search', flow['database_included']),
        ('Final primary studies included', flow['final_included']),
    ]
    for y, (label, count) in zip(centers, boxes):
        ax.add_patch(FancyBboxPatch((.03, y - .043), .55, .086,
                     boxstyle='round,pad=0.01', edgecolor='#455A64', facecolor='#F4F7F8'))
        ax.text(.305, y, label + f'\n(n = {count:,})', ha='center', va='center', fontsize=10)
    for high, low in zip(centers[:-1], centers[1:]):
        ax.annotate('', xy=(.305, low + .055), xytext=(.305, high - .055),
                    arrowprops={'arrowstyle': '->', 'color': '#455A64'})
    for y, count in [(.64, flow['title_abstract_excluded']), (.50, flow['full_text_excluded'])]:
        ax.add_patch(FancyBboxPatch((.67, y - .035), .28, .07, boxstyle='round,pad=0.01',
                     edgecolor='#607D8B', facecolor='white'))
        ax.text(.81, y, f'Excluded\n(n = {count:,})', ha='center', va='center')
        ax.annotate('', xy=(.66, y), xytext=(.59, y), arrowprops={'arrowstyle': '->'})
    ax.add_patch(FancyBboxPatch((.66, .23), .30, .15, boxstyle='round,pad=0.01',
                 edgecolor='#607D8B', facecolor='white'))
    ax.text(.81, .305, 'Additional snowballing\ncandidates\n'
            f"Examined: {flow['snowball_candidates']}\nIncluded: {flow['snowball_included']}",
            ha='center', va='center', fontsize=9)
    ax.annotate('', xy=(.59, .10), xytext=(.81, .22),
                arrowprops={'arrowstyle': '->', 'connectionstyle': 'angle,angleA=-90,angleB=0,rad=0'})
    save(fig, out, 'study_selection_flow', dpi=220)


def lifecycle_asset(out):
    destination = Path(out) / 'lifecycle.pdf'
    shutil.copyfile(ROOT / 'assets/lifecycle.pdf', destination)
    document = pymupdf.open(destination)
    document[0].get_pixmap(matrix=pymupdf.Matrix(2, 2), alpha=False).save(Path(out) / 'lifecycle.png')


def generate_all(studies, stats, out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    with plt.rc_context(STYLE):
        publication(stats, out)
        lifecycle_distribution(stats, out)
        knowledge_resources(stats, out)
        task_taxonomy(stats, out)
        rag_settings(stats, out)
        rag_framework(out)
        review_flow(out)
        lifecycle_asset(out)
    return sorted(path.name for path in out.glob('*.pdf'))
