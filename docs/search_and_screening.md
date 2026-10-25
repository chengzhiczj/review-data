# Literature search and screening protocol

This document transcribes the search and screening protocol reported in the survey. It is protocol information prepared for this package, rather than a contemporaneous database export or record-level decision log.

## Scope of the released code

The code reproduces the coding-based synthesis, descriptive statistics, and figures for the 31 included studies. The package also provides the documented search strategy, eligibility criteria, and aggregate selection counts. It does not reexecute the original database searches or reconstruct individual screening decisions. Screening was conducted by researchers, so the package does not claim an automated screening implementation.

## Sources, period, and fields

Searches were conducted in June 2026 for the 2024-June 2026 window. The eight sources were ACM Digital Library, IEEE Xplore, ScienceDirect, SpringerLink, Wiley Online Library, arXiv, Scopus, Web of Science.

Scopus and Web of Science used titles, abstracts, and keywords. arXiv used separate phrase searches over titles and abstracts. Other sources used the closest available advanced-search fields. Syntax was adapted to the source.

## Documented search concept blocks

Combine the RAG mechanism block, software vulnerability domain block, and one lifecycle-stage task block with AND. The expressions below are the concept blocks documented in the paper. They are not timestamped verbatim query logs for each database.

### RAG mechanism

```text
"retrieval-augmented" OR "retrieval augmented" OR "retrieval-augmented generation" OR "retrieval augmented generation" OR "retrieval-enhanced generation" OR "retrieval-grounded generation" OR "knowledge-augmented generation" OR "knowledge-grounded generation" OR "retrieval-augmented LLM*" OR "RAG-based" OR "RAG-enhanced" OR (RAG AND (LLM* OR "large language model*"))
```

### Software vulnerability domain

```text
"software secur*" OR software OR code OR program* OR "source code" OR "smart contract*" OR blockchain OR vulnerab* OR weakness* OR "security flaw*" OR CVE OR CWE OR NVD OR CVSS OR SWC OR OWASP
```

### Vulnerability Discovery

```text
"vulnerability detect*" OR "vulnerability discover*" OR "weakness detect*" OR "security flaw detect*" OR "static analy*" OR "dynamic analy*" OR fuzz* OR "fuzz test*" OR "seed generat*" OR "security audit*" OR "code audit*" OR "audit report*" OR "smart contract audit*"
```

### Vulnerability Analysis

```text
"vulnerability analys*" OR "vulnerability assessment" OR "vulnerability classification" OR "root-cause analys*" OR "severity assessment" OR "risk assessment" OR "impact analys*" OR exploitabilit* OR CVSS OR "CWE map*" OR "SWC map*" OR "OWASP map*" OR "ATT&CK map*" OR "vulnerability validat*" OR "vulnerability reproduc*" OR "exploit generat*" OR "exploit verif*"
```

### Vulnerability Mitigation

```text
"vulnerability mitigat*" OR "vulnerability remediat*" OR "security remediat*" OR "vulnerability repair" OR "security repair" OR "repair recommendation*" OR "vulnerability patch*" OR "security patch*" OR "security fix*" OR "patch generat*" OR "patch validat*" OR "repair validat*" OR "mitigation guideline*"
```

## Selection and eligibility

Duplicate identification used titles, authors, years, venues, DOIs, and URLs. The most complete study version was retained. Two reviewers independently screened candidates. Title/abstract/keyword screening preceded full-text eligibility and quality assessment. Each excluded study contributed one primary exclusion reason to the aggregate flow. Backward and forward snowballing used the same eligibility and quality criteria.

### Inclusion criteria

- **IC1**: The study uses task-specific retrieved evidence, or information explicitly derived from it, to condition a generative component within an implemented software vulnerability workflow, under the review's operational RAG definition.
- **IC2**: The study addresses at least one task within Vulnerability Discovery, Vulnerability Analysis, or Vulnerability Mitigation.
- **IC3**: The study investigates software-related security artifacts, such as source code, smart contracts, patches, repositories, vulnerability reports, issue reports, security advisories, CVE/CWE/NVD records, or other software vulnerability knowledge sources.
- **IC4**: The study proposes and implements a concrete RAG-based method, system, framework, or workflow for a software vulnerability lifecycle task. The retrieval-to-generation dependency must be documented as part of the implemented vulnerability workflow, including task-specific retrieved demonstrations or evidence-derived features.
- **IC5**: The study reports sufficient information to identify the target task, the role of retrieval or external knowledge, and the experimental or case-analysis setting.
- **IC6**: The study is a peer-reviewed primary publication or preprint represented by an English-language version published or publicly released between 2024 and the search cutoff in June 2026, and its full text is accessible.

### Exclusion criteria

- **EC1**: The study does not implement a task-specific retrieval-to-generation dependency within a software vulnerability workflow, or uses external knowledge only as background material.
- **EC2**: The abbreviation “RAG” refers to a meaning other than Retrieval-Augmented Generation.
- **EC3**: The study focuses on general cybersecurity, hardware security, network defense, medical safety, policy compliance, or other domains without directly addressing software vulnerability discovery, analysis, or mitigation.
- **EC4**: The study investigates RAG systems themselves as the object of study, such as hallucination analysis, retriever evaluation, or prompt studies, rather than applying RAG to a software vulnerability task.
- **EC5**: The study only mentions or evaluates generic RAG without implementing and describing its retrieval-to-generation dependency for a software vulnerability output.
- **EC6**: The publication is a survey, review, tutorial, editorial, keynote, poster abstract, position paper, or another non-primary work.
- **EC7**: The study is a duplicate, superseded version, or preliminary version of another included paper; in such cases, the most complete formally available version is retained.
- **EC8**: The full text is inaccessible, or the available metadata and content are insufficient to determine relevance and extract the required study information.
- **EC9**: The study is not written in English.

## Reported aggregate selection counts

| Step | Count |
|---|---:|
| database records | 3914 |
| duplicates removed | 677 |
| unique records | 3237 |
| title abstract excluded | 3128 |
| database full text | 109 |
| full text excluded | 82 |
| database included | 27 |
| snowball candidates | 10 |
| snowball included | 4 |
| final included | 31 |

These are the aggregate counts reported in the survey, not counts recomputed from original database exports. The final study inventory is available in `data/publication_metadata.csv`. The quality-assessment protocol and reported aggregates are documented in `docs/quality_assessment.md`.

## Record boundaries

Original database exports, timestamped source-specific query logs, record-level duplicate decisions, and individual screening logs are outside this release. No candidate records, exclusion decisions, or reviewer votes are generated from aggregate counts. The `query` field in `study_extraction.csv` describes each primary system's evidence-retrieval query, not the survey's literature-search query.
