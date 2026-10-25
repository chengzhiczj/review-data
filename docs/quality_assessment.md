# Reported quality-assessment protocol and aggregates

Source: the current manuscript. These values are reported aggregates, not values recomputed from study-level reviewer score sheets.

| ID | Dimension | Criterion |
|---|---|---|
| QA1 | Problem definition and scope | The study clearly defines the software vulnerability task, target artifact, research objective, and intended output. |
| QA2 | Knowledge-source design | The study describes the retrieved knowledge source(s), their provenance, construction or curation process, and unit of retrieval, as well as their temporal scope where applicable. |
| QA3 | Retrieval strategy | The study reports the query formulation, retriever or representation method, indexing approach, and retrieval depth, together with any applicable filtering or reranking mechanisms. |
| QA4 | Evidence integration and reasoning | The study explains how retrieved evidence is incorporated into prompts, models, graphs, tools, agents, or iterative reasoning processes, and how this evidence contributes to the final task output. |
| QA5 | Experimental or case-study design | The study reports the dataset or target system, selection or data-splitting procedure, experimental environment, and evaluation protocol in sufficient detail to support the interpretation of the results. |
| QA6 | Baselines and ablation studies | The study compares the proposed method with meaningful baselines and, where applicable, reports ablation studies involving the no-retrieval setting, retriever, reranker, fusion mechanism, or backbone model. |
| QA7 | Evaluation and validation | The study employs task-appropriate evaluation metrics and reports sufficient results, including functional, security-oriented, or execution-based validation where required by the task. |
| QA8 | Reproducibility information | The study reports the models, key prompts or agent roles, retrieval corpus, implementation details, and tool configurations, and indicates the availability of code, data, or other research artifacts where applicable. |
| QA9 | Limitations and threats to validity | The study discusses relevant limitations, failure cases, threats to validity, security risks, deployment constraints, or important assumptions. |
| QA10 | Reporting transparency | The study provides sufficient information to determine the centrality of RAG to the proposed method, its relevance to software vulnerability lifecycle tasks, and the required data-extraction fields without requiring unsupported inferences by the reviewers. |

Each item uses scores 10, 7, 4, or 1. The manuscript reports a 65-point threshold with independent assessment and consensus resolution. For the 31 included studies it reports scores of 67-97, median 82, and mean 81.3. Incomplete reporting counts are QA6: 21, QA2: 18, and QA3: 17. Reported pre-consensus binary agreement for the 109 database full-text candidates is kappa = 0.81.

The shared study-level extraction and coding data are distinct from the original reviewer quality-score sheets and screening decisions. This release does not create individual score rows or reconstruct kappa inputs from aggregate values.
