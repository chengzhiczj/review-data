# Replication materials for the software vulnerability RAG survey

This package accompanies *Retrieval-Augmented Generation for the Software Vulnerability Lifecycle: A Comprehensive Survey*. It contains the 31-study extraction records, coding data, publication metadata, supporting excerpts, and analysis and figure-generation code. The survey manuscript and its LaTeX project are not included.

The review window is 2024 through June 2026. Release date: October 22, 2026. The package reproduces the review's descriptive synthesis. It does not rerun the experiments of the 31 primary systems.

The released code reproduces the coding-based synthesis, descriptive statistics, and figures for the 31 included studies. The documented search strategy, eligibility criteria, and aggregate selection counts are supplied as protocol information in `docs/search_and_screening.md` and `data/search_protocol.json`. The package does not reexecute the original database searches or reconstruct individual screening decisions. The primary systems' retrieval queries in `study_extraction.csv` are distinct from the survey's literature-search queries.

## Quick start

Use Python 3.12 or later. The reference environment used Python 3.14 and the versions in `requirements.txt`. From this directory, run:

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on Linux/macOS:

```bash
source .venv/bin/activate
```

Then install dependencies and reproduce:

```bash
python -m pip install -r requirements.txt
python reproduce.py
```

The analysis uses only packaged inputs. After dependency installation, it does not access the network or require the original workspace. No API key or LLM service is needed. Results are written to `results/`, with PDF and PNG figures in `results/figures/`.

For input validation alone:

```bash
python reproduce.py --check-only
```

To choose a separate output directory:

```bash
python reproduce.py --output ./my_results
```

## Contents

| Location | Contents |
|---|---|
| `data/studies.json` | Master data for all 31 studies, including linked extraction and evaluation evidence |
| `data/study_extraction.csv` | System-level retrieval queries, retrieval units and indexes, filtering/reranking, evidence integration, models and roles, baselines, protocols, benchmarks, contexts, granularities, and metrics |
| `data/study_coding.csv` | Principal contribution, overlapping stage coverage, supporting outputs, task families, resources, retrieval components, integration, repeated conditioning, and reasoning codes |
| `data/publication_metadata.csv` | Study identity, citation keys, cutoff-based publication year/type, current bibliography metadata, DOIs, and source links |
| `data/evaluation_decisions.csv` | 186 study-by-dimension decisions, with status, applicability, rationale, and evidence IDs |
| `data/codebook.json` and `docs/codebook.md` | Operational definitions, coding boundaries, evaluation rules, and denominators |
| `data/data_dictionary.csv` and `docs/data_dictionary.md` | Field definitions and serialization conventions |
| `data/review_method_summary.json` | Reported screening counts, publication policy, quality-assessment protocol, and aggregate quality results |
| `data/search_protocol.json` and `docs/search_and_screening.md` | Documented search blocks, sources, fields, eligibility criteria, aggregate selection flow, and boundaries of the released search/screening records |
| `data/expected_results.json` | Fixed manuscript counts used as independent assertions during validation |
| `evidence/excerpts.jsonl` | 433 deduplicated source excerpts, with study/citation IDs, source hashes, line spans, and uses |
| `evidence/evidence_links.csv` | Links from extraction records and evaluation dimensions to excerpt IDs |
| `evidence/source_index.csv` | Source-text filenames, hashes, and line counts for the 31 primary studies |
| `references/primary_studies.bib` | Exactly the 31 primary-study references |
| `assets/` | Original lifecycle vector illustration and manuscript TikZ source for the selection flow |
| `scripts/` and `reproduce.py` | Validation, descriptive analysis, evidence reports, and figure generation |
| `results/` | Precomputed statistics, CSV exports, readable study/evaluation reports, and nine PDF/PNG figures |
| `MANIFEST.sha256` | Checksums for released inputs, documents, and code |

Running `reproduce.py` requires only the packaged data, code, and illustration asset.

## Statistical conventions

The unit of analysis is one primary study. Principal contribution is exclusive. Lifecycle coverage and task-family, knowledge-resource, retrieval-component, and evaluation labels can overlap. Each study has one principal integration route and one principal reasoning mode. Contrastive comparison is an additional code. Hybrid retrieval also contributes to its sparse and dense components.

Corpus percentages use 31 as their denominator. Functional correctness and post-repair security also use the five studies generating software patches. Test-seed and reproduction-environment repair do not count as software patch generation. A supporting stage output corresponds to a dagger in the manuscript table and need not be an independently evaluated endpoint.

`not_reported` means the reviewed text did not report a qualifying assessment. It does not establish that a system lacks that capability. `not_applicable` is used for the two repair dimensions in non-Patch studies. Similarity-based proxies remain distinguishable from human/reference judgments and static, execution-based, or model-only validation.

Expected core results are:

| Measure | Counts |
|---|---|
| Principal contribution: Discovery, Analysis, Mitigation | 20, 7, 4 |
| Non-exclusive coverage: Discovery, Analysis, Mitigation | 22, 20, 9 |
| Cross-stage studies | 14 |
| Retrieval: SR, DR, HR, GSR, RTR | 12, 22, 7, 11, 5 |
| Integration: Context, Workflow, Feature | 16, 11, 4 |
| Publication years: 2024, 2025, 2026 | 1, 15, 15 |
| Publication types at cutoff: journal, conference, preprint | 17, 7, 7 |
| Evaluation: retrieval relevance, context recall, provenance, claim faithfulness, functional correctness, post-repair security | 6, 1, 1, 1, 1, 4 |

## Publication metadata

`review_year` and `review_publication_type` reproduce the manuscript's June 2026 cutoff policy. If a formal publication was available by that cutoff, its year is used, including journal early access. Otherwise the initial arXiv submission year is used. `bibliography_year`, `bibliography_entry_type`, and `venue` describe the version cited in the current bibliography. These fields can differ when a study was formally published after the cutoff. Subsequent bibliography updates do not change the cutoff-based counts automatically.

Stable study IDs preserve the original review IDs rather than publication order. Join records using `study_id` or `citation_key` rather than CSV row position.

## Evidence and quality records

Extraction locators and evaluation decisions link to `evidence/excerpts.jsonl`. Each excerpt preserves the original extracted-text line span and identifies its source text by SHA-256. Evaluation excerpts were checked against the existing primary-text audit. Full publisher PDFs and complete primary-study text dumps are not redistributed. The publication links identify the primary papers. Line numbers refer to the indexed text extraction, so re-extracting a PDF with different software can produce different line positions.

The quality-assessment checklist and manuscript-reported aggregate scores are supplied in `data/review_method_summary.json` and `docs/quality_assessment.md`. Individual reviewer scores, the full screening-decision log, and kappa inputs are not reconstructed from those aggregates. The extractability coding and the 186 evaluation decisions are separate data products.

## Figures

Six data-driven figures are recomputed directly from the 31-study master data:

- `pub_year`: publication years under the cutoff policy.
- `pub_venue_type`: publication types at the cutoff.
- `pie_distribution`: principal contribution versus overlapping stage coverage. The manuscript's historical filename is retained, although the figure is a bar chart.
- `task_taxonomy`: task-family counts grouped by principal contribution.
- `knowledge_bar`: resource counts grouped by principal contribution.
- `rag_settings_heatmap`: retrieval, integration, and reasoning counts grouped by principal contribution.

`rag_pipeline` is drawn from the documented conceptual framework. `study_selection_flow` uses the reported aggregate selection counts. The lifecycle illustration is supplied as the original vector PDF and copied to the output, with its PNG rendered from that asset. Regenerated figures reproduce the data and framework; minor rendering and layout differences can occur across platforms. The extracted TikZ flow is supplied as a figure source fragment. Reproduction uses its Python equivalent and does not require the survey's LaTeX project.

## Validation and maintenance

Validation checks the release checksums, the unique 31-study inventory, legal codes, stage/task consistency, denominators, all fixed summary counts, evidence links, CSV exports, the primary-study bibliography, and the illustration asset. Run results are saved to `results/validation.json`. The released inputs were aligned with the survey during package preparation; runtime validation does not require the manuscript.

The CSV files in `data/` are spreadsheet-friendly views of the master JSON. Analysis reads the JSON. If deliberately making a new release, update the master, corresponding CSV views, and expected results together, then regenerate input checksums:

```bash
python -m scripts.export_data
python -m scripts.manifest --write
python reproduce.py
```

Keep the originally received package unchanged when verifying its integrity. `results/` is excluded from the input manifest because it is regenerated by the scripts. The supplied release run is documented in `docs/reproduction_check.json`.

Package documentation and data are UTF-8. All paths are relative to this directory. The source preparation used to assemble this release is described in `docs/release_snapshot.json`; running the released analysis requires no author-workspace preparation scripts.
