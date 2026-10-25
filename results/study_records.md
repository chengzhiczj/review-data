# Study-level extraction and coding records

One section per primary study. Publication statistics use the cutoff fields. The bibliography fields identify the cited version.

## S01: SyzGPT

Citation key: `zhang2025unlocking`.

Unlocking low frequency syscalls in kernel fuzzing with dependency-based RAG

Cutoff year/type: 2025 / journal.

Cited version: 2025, Proceedings of the ACM on Software Engineering.

DOI: 10.1145/3728913.

### Coding

- **principal contribution**: Discovery
- **lifecycle coverage**: D
- **supporting stage outputs**: None
- **task families**: Test
- **knowledge resources**: Code, Context
- **retrieval components**: SR, GSR
- **integration route**: Workflow
- **repeated conditioning**: True
- **reasoning mode**: HSR
- **contrastive comparison**: False

### Extraction

**Task output summary.** Generates and repairs Syzkaller test seeds for kernel fuzzing. Seed repair changes test inputs rather than vulnerable software.

**Query.** Target low-frequency syscall and dependency chain

**Knowledge unit representation index.** Syz-program corpus; syscall inverted index; dependencies from manuals/Syzlang

**Selection filtering reranking.** Dependency-level program selection; feedback validity filters

**Evidence integration.** Adaptive user/assistant program examples; syntax/execution feedback repair

**Models and roles.** GPT-3.5; GPT-4; Claude-3.5; CodeLlama/Vicuna/Llama-3; tuned CodeLlama-syz

**Baselines.** Syzkaller and six other kernel fuzzers; prompt/dependency ablations

**Evaluation protocol.** 436 low-frequency syscall targets; three Linux LTS kernels; five 24h fuzzing runs; seed validity and crashes

**Benchmarks.** Linux LTS kernels

**Evaluation context.** Linux kernel/Syzkaller

**Evaluation granularity.** Syscall-sequence level

**Reported metrics.** Syntax Valid Rate, Context Effective Rate, Overall Effectiveness Rate, program diversity, code coverage, syscall coverage, crash/vulnerability count, unique bugs, token/time cost

Extraction source locators: [E0001](source_excerpts.md#e0001), [E0002](source_excerpts.md#e0002), [E0003](source_excerpts.md#e0003), [E0004](source_excerpts.md#e0004), [E0005](source_excerpts.md#e0005), [E0006](source_excerpts.md#e0006), [E0007](source_excerpts.md#e0007), [E0008](source_excerpts.md#e0008), [E0009](source_excerpts.md#e0009), [E0010](source_excerpts.md#e0010).

## S02: Vul-RAG

Citation key: `du2024vul`.

Vul-RAG: Enhancing LLM-based vulnerability detection via knowledge-level RAG

Cutoff year/type: 2026 / journal.

Cited version: 2026, ACM Transactions on Software Engineering and Methodology.

DOI: 10.1145/3797277.

### Coding

- **principal contribution**: Discovery
- **lifecycle coverage**: D
- **supporting stage outputs**: None
- **task families**: Identify
- **knowledge resources**: VR, Code
- **retrieval components**: SR
- **integration route**: Context
- **repeated conditioning**: True
- **reasoning mode**: CoT
- **contrastive comparison**: False

### Extraction

**Task output summary.** Produces a vulnerable/non-vulnerable judgment for target code using historical vulnerability knowledge. Historical causes and fixes are retrieval context.

**Query.** Code, abstract purpose, and detailed behavior of target function

**Knowledge unit representation index.** Historical vulnerability knowledge item: code/semantics/cause/fix; lexical documents

**Selection filtering reranking.** BM25 over three query views; candidate deduplication and RRF

**Evidence integration.** Sequential knowledge items; check cause and absence of fix

**Models and roles.** GPT-4o; Claude Sonnet 3.5; Qwen2.5-Coder-32B; DeepSeek-V2; extended experiment includes DeepSeek-R1

**Baselines.** Basic/CoT prompts; code-level RAG; fine-tuned LLMAO

**Evaluation protocol.** PairVul vulnerable/fixed pairs; train/test partition; pairwise evaluation

**Benchmarks.** PairVul

**Evaluation context.** C/C++, Linux kernel

**Evaluation granularity.** Function-pair level

**Reported metrics.** Pairwise Acc., Balanced Prec., Balanced Rec., human knowledge-quality/usability ratings, manual retrieval-failure diagnosis

Extraction source locators: [E0012](source_excerpts.md#e0012), [E0013](source_excerpts.md#e0013), [E0014](source_excerpts.md#e0014), [E0015](source_excerpts.md#e0015), [E0016](source_excerpts.md#e0016), [E0017](source_excerpts.md#e0017), [E0018](source_excerpts.md#e0018).

## S03: RASM-Vul

Citation key: `zhao2026retrieval`.

Retrieval-augmented semantic mapping for vulnerability detection via multi-view code similarity

Cutoff year/type: 2026 / journal.

Cited version: 2026, Electronics.

DOI: 10.3390/electronics15030612.

### Coding

- **principal contribution**: Discovery
- **lifecycle coverage**: D, A
- **supporting stage outputs**: None
- **task families**: Identify, Characterize
- **knowledge resources**: VR, Code
- **retrieval components**: DR, GSR
- **integration route**: Context
- **repeated conditioning**: False
- **reasoning mode**: HSR
- **contrastive comparison**: False

### Extraction

**Task output summary.** Produces vulnerability judgments, suspicious lines or AST paths, and explanations of vulnerability behavior, prerequisites, triggers, and categories.

**Query.** Predicted suspicious lines/AST paths plus target-code behavior summary

**Knowledge unit representation index.** Five vector views: code, AST, knowledge, line changes, AST changes; UniXCoder-base vectors

**Selection filtering reranking.** Dynamic WRRF; LLM reranking; similarity threshold

**Evidence integration.** Predict-then-retrieve; history-supported staged detection

**Models and roles.** DeepSeek-V2.5-1210 KB extraction; DeepSeek-V3/Qwen2.5-72B detection

**Baselines.** CppCheck; FlawFinder; LineVul; SVulD; fine-tuned CodeBERT/UniXCoder/GraphCodeBERT/CodeT5+; DeepSeek

**Evaluation protocol.** PrimeVul paired: 3789/480/435 pairs train/validation/test; KB and variants training only

**Benchmarks.** PrimeVul

**Evaluation context.** C/C++

**Evaluation granularity.** Function-level paired samples

**Reported metrics.** Acc., Prec., Rec., F1, Pair Acc., BERTScore of retrieved evidence against reference vulnerability descriptions

Extraction source locators: [E0024](source_excerpts.md#e0024), [E0025](source_excerpts.md#e0025), [E0026](source_excerpts.md#e0026), [E0027](source_excerpts.md#e0027), [E0028](source_excerpts.md#e0028), [E0029](source_excerpts.md#e0029), [E0030](source_excerpts.md#e0030), [E0031](source_excerpts.md#e0031), [E0032](source_excerpts.md#e0032), [E0033](source_excerpts.md#e0033), [E0034](source_excerpts.md#e0034).

## S04: DeepVulHunter

Citation key: `jiao2025deepvulhunter`.

DeepVulHunter: enhancing the code vulnerability detection capability of LLMs through multi-round analysis

Cutoff year/type: 2025 / journal.

Cited version: 2025, Journal of Intelligent Information Systems.

DOI: 10.1007/s10844-025-00982-0.

### Coding

- **principal contribution**: Discovery
- **lifecycle coverage**: D, A
- **supporting stage outputs**: None
- **task families**: Identify, Characterize
- **knowledge resources**: VR, Code
- **retrieval components**: DR
- **integration route**: Context
- **repeated conditioning**: True
- **reasoning mode**: HSR
- **contrastive comparison**: False

### Extraction

**Task output summary.** Produces similar-code diagnostic analysis, target-code vulnerability analysis, and a final vulnerability judgment.

**Query.** Target function/code snippet

**Knowledge unit representation index.** Big-Vul code functions with CVE descriptions and patches; CodeT5P-110M/FAISS

**Selection filtering reranking.** Normalize embeddings; reject 100% identical matches

**Evidence integration.** Similar-code analysis, target analysis, final validation

**Models and roles.** DeepSeek-V3/R1; Llama-3.1-8B/70B/405B

**Baselines.** LLMVD; CFGNN; GRACE; VulACLLM; standalone same-backbone models

**Evaluation protocol.** 1937 held-out NVD-derived C/C++ snippets (1015 vulnerable/922 safe); retrieved cases with 100% similarity skipped

**Benchmarks.** NVD-derived C/C++ test set

**Evaluation context.** C/C++

**Evaluation granularity.** Snippet/function-level

**Reported metrics.** Acc., Prec., Rec., F1

Extraction source locators: [E0038](source_excerpts.md#e0038), [E0039](source_excerpts.md#e0039), [E0040](source_excerpts.md#e0040), [E0041](source_excerpts.md#e0041), [E0042](source_excerpts.md#e0042), [E0043](source_excerpts.md#e0043), [E0044](source_excerpts.md#e0044), [E0045](source_excerpts.md#e0045).

## S05: CodeRAG

Citation key: `liu2026software`.

Software vulnerability detection via multimodal retrieval and hierarchical decision making

Cutoff year/type: 2026 / journal.

Cited version: 2026, Science of Computer Programming.

DOI: 10.1016/j.scico.2026.103491.

### Coding

- **principal contribution**: Discovery
- **lifecycle coverage**: D, A
- **supporting stage outputs**: None
- **task families**: Identify, Characterize
- **knowledge resources**: Code
- **retrieval components**: SR, DR, HR, GSR
- **integration route**: Context
- **repeated conditioning**: False
- **reasoning mode**: HSR
- **contrastive comparison**: True

### Extraction

**Task output summary.** Produces a VULNERABLE/SAFE judgment, confidence, and a root-cause or risk explanation.

**Query.** Uncertain target function after lightweight screening

**Knowledge unit representation index.** Vulnerable and safe training functions, with embedding, graph, and AST representations.

**Selection filtering reranking.** Dense recall and graph, lexical Jaccard, and AST reranking for uncertain functions.

**Evidence integration.** One vulnerable and one safe demonstration condition the final judgment and explanation.

**Models and roles.** DeepSeek-V3.1-Terminus

**Baselines.** Pure LLM; pure GNN; pure Transformer; without ICL; GRACE published results

**Evaluation protocol.** Devign and Reveal; cases from training only; rerank weights tuned Devign validation, fixed on Reveal; five seeds

**Benchmarks.** Devign, Reveal

**Evaluation context.** C/C++

**Evaluation granularity.** Function/code-sample level

**Reported metrics.** Acc., Prec., Rec., F1, AUC, stage-processing ratio, threshold/retrieval-size sensitivity

Extraction source locators: [E0047](source_excerpts.md#e0047), [E0048](source_excerpts.md#e0048), [E0049](source_excerpts.md#e0049), [E0050](source_excerpts.md#e0050), [E0051](source_excerpts.md#e0051), [E0052](source_excerpts.md#e0052), [E0053](source_excerpts.md#e0053), [E0054](source_excerpts.md#e0054), [E0055](source_excerpts.md#e0055).

## S06: MulVul

Citation key: `wu2026mulvul`.

MulVul: Retrieval-augmented multi-agent code vulnerability detection via cross-model prompt evolution

Cutoff year/type: 2026 / preprint.

Cited version: 2026, Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

DOI: 10.18653/v1/2026.acl-long.391.

### Coding

- **principal contribution**: Discovery
- **lifecycle coverage**: D
- **supporting stage outputs**: None
- **task families**: Identify
- **knowledge resources**: VR, Code
- **retrieval components**: DR
- **integration route**: Workflow
- **repeated conditioning**: False
- **reasoning mode**: MAR
- **contrastive comparison**: True

### Extraction

**Task output summary.** Produces vulnerability-category and CWE predictions through router and detector agents. Supporting explanations are not independently evaluated analysis deliverables.

**Query.** Target-code SCALE representation; category-specific router/detector queries

**Knowledge unit representation index.** Training-set SCALE examples; UniXCoder vectors in FAISS

**Selection filtering reranking.** Global router retrieval; contrastive positives/clean/hard negatives; allocated budgets

**Evidence integration.** Coarse-to-fine router and detectors; evolved role-specific prompts

**Models and roles.** GPT-4o execution; Claude Opus 4.5 prompt evolution

**Baselines.** GPT-4o; LLMVulExp; fine-tuned code models; GNN baselines

**Evaluation protocol.** PrimeVul held-out evaluation; KB from training set; training sample itself excluded during offline prompt evolution

**Benchmarks.** PrimeVul

**Evaluation context.** C/C++

**Evaluation granularity.** Function-level and CWE/category-level

**Reported metrics.** Prec., Rec., F1, category-routing Recall@k, tail/few-shot F1, coverage, Gini coefficient

Extraction source locators: [E0058](source_excerpts.md#e0058), [E0059](source_excerpts.md#e0059), [E0060](source_excerpts.md#e0060), [E0061](source_excerpts.md#e0061), [E0062](source_excerpts.md#e0062), [E0063](source_excerpts.md#e0063).

## S07: HyVD-VP

Citation key: `wang2026fine`.

Fine-tuning a vulnerability-specific large language model for a hybrid software vulnerability detection method

Cutoff year/type: 2025 / journal.

Cited version: 2026, Engineering Applications of Artificial Intelligence.

DOI: 10.1016/j.engappai.2025.113410.

### Coding

- **principal contribution**: Discovery
- **lifecycle coverage**: D, A
- **supporting stage outputs**: None
- **task families**: Identify, Characterize, Verify
- **knowledge resources**: VR, Code
- **retrieval components**: DR, RTR
- **integration route**: Workflow
- **repeated conditioning**: True
- **reasoning mode**: HSR
- **contrastive comparison**: False

### Extraction

**Task output summary.** Produces CWE-to-line findings and generated dynamic tests, traces, and verification results that confirm, refute, or revise static findings.

**Query.** CFG/CPG-derived target chunk and local vulnerability context

**Knowledge unit representation index.** LocalVulDB code/record chunks; vector similarity; CFG/CPG slices

**Selection filtering reranking.** Chunk overlap; top-k=5; cosine; threshold; enabled reranking

**Evidence integration.** Static detector plus PAL-generated sandbox tests; judge aggregation

**Models and roles.** Qwen3-8B default; Qwen2.5-Coder-7B and Seed-Coder-8B compared

**Baselines.** Fortify; SpotBugs; neural/LLM detection baselines; fine-tuning and component ablations

**Evaluation protocol.** Random 8:1:1 split with no sample overlap; short and custom long Java datasets; static/dynamic validation

**Benchmarks.** MegaVul, Juliet Java, custom long-code dataset

**Evaluation context.** Java

**Evaluation granularity.** Function-level and project-level

**Reported metrics.** Acc., Prec., Rec., F1, FPR, FNR, inference time

Extraction source locators: [E0065](source_excerpts.md#e0065), [E0066](source_excerpts.md#e0066), [E0067](source_excerpts.md#e0067), [E0068](source_excerpts.md#e0068), [E0069](source_excerpts.md#e0069), [E0070](source_excerpts.md#e0070), [E0071](source_excerpts.md#e0071), [E0072](source_excerpts.md#e0072).

## S08: KLRAG

Citation key: `liao2025klrag`.

KLRAG: Deep learning library vulnerability detection via knowledge-level RAG

Cutoff year/type: 2025 / conference.

Cited version: 2025, International Conference on Intelligent Computing.

DOI: 10.1007/978-981-96-9958-2_36.

### Coding

- **principal contribution**: Discovery
- **lifecycle coverage**: D
- **supporting stage outputs**: None
- **task families**: Test
- **knowledge resources**: Code, Context
- **retrieval components**: DR
- **integration route**: Context
- **repeated conditioning**: False
- **reasoning mode**: DG
- **contrastive comparison**: False

### Extraction

**Task output summary.** Generates API test sequences for differential fuzzing and discovers crashes or inconsistent behavior. Execution serves the discovery workflow.

**Query.** LLM-generated tested-API functionality and similar APIs

**Knowledge unit representation index.** GitHub issue vulnerability knowledge; text-embedding-v3; Chroma/HNSW

**Selection filtering reranking.** Cosine ANN candidate selection

**Evidence integration.** Role-based knowledge-conditioned API seed generation

**Models and roles.** Qwen2.5-Coder-32B offline KB; DeepSeek-V3 online generation; Qwen-2.5-32B in PaddlePaddle bug-discovery experiment

**Baselines.** TitanFuzz; FuzzGPT; retrieved comparator results from papers

**Evaluation protocol.** PyTorch/TensorFlow/Paddle fuzzing; coverage/valid seeds/bugs

**Benchmarks.** Python DL libraries

**Evaluation context.** PyTorch, TensorFlow, PaddlePaddle

**Evaluation granularity.** API-level

**Reported metrics.** Detected bug count, line/code coverage, API coverage, valid seed rate

Extraction source locators: [E0074](source_excerpts.md#e0074), [E0075](source_excerpts.md#e0075), [E0076](source_excerpts.md#e0076), [E0077](source_excerpts.md#e0077), [E0078](source_excerpts.md#e0078), [E0079](source_excerpts.md#e0079), [E0080](source_excerpts.md#e0080), [E0081](source_excerpts.md#e0081), [E0082](source_excerpts.md#e0082), [E0083](source_excerpts.md#e0083), [E0084](source_excerpts.md#e0084), [E0085](source_excerpts.md#e0085).

## S09: VulRTex

Citation key: `jiang2026vulrtex`.

VulRTex: A Reasoning-Guided Approach to Identify Vulnerabilities from Rich-Text Issue Report

Cutoff year/type: 2026 / journal.

Cited version: 2026, ACM Transactions on Software Engineering and Methodology.

DOI: 10.1145/3801149.

### Coding

- **principal contribution**: Discovery
- **lifecycle coverage**: D, A
- **supporting stage outputs**: None
- **task families**: Identify, Characterize
- **knowledge resources**: VR, Context
- **retrieval components**: SR, GSR
- **integration route**: Context
- **repeated conditioning**: False
- **reasoning mode**: CoT
- **contrastive comparison**: False

### Extraction

**Task output summary.** Produces a vulnerability-related issue decision and a CWE identifier from rich-text issue reports.

**Query.** OCR/CAST-converted rich-text issue report

**Knowledge unit representation index.** Historical vulnerability-associated records and textual reasoning graphs

**Selection filtering reranking.** TF-IDF thresholds for knowledge, graph records and graph selection

**Evidence integration.** Selected reasoning graph generates target-specific guidance prompt

**Models and roles.** LLaMA/GPT-3/GPT-3.5; Qwen2VL/GPT-4o; DeepSeek-R1 variants

**Baselines.** General code/text classifiers; standalone LLM and reasoning baselines; component ablations

**Evaluation protocol.** 973572 issue reports; historical 60% and targets 40%; real-world emerging issue study

**Benchmarks.** GHArchive-based issue report benchmark

**Evaluation context.** GitHub OSS

**Evaluation granularity.** Issue-report level

**Reported metrics.** Issue identification: Prec., Rec., F1, AUROC, AUPRC; CWE-ID prediction: Macro-P, Macro-R, Macro-F1; average time cost

Extraction source locators: [E0087](source_excerpts.md#e0087), [E0088](source_excerpts.md#e0088), [E0089](source_excerpts.md#e0089), [E0090](source_excerpts.md#e0090), [E0091](source_excerpts.md#e0091), [E0092](source_excerpts.md#e0092), [E0093](source_excerpts.md#e0093), [E0094](source_excerpts.md#e0094), [E0095](source_excerpts.md#e0095), [E0096](source_excerpts.md#e0096), [E0097](source_excerpts.md#e0097), [E0098](source_excerpts.md#e0098), [E0099](source_excerpts.md#e0099), [E0100](source_excerpts.md#e0100), [E0101](source_excerpts.md#e0101), [E0102](source_excerpts.md#e0102), [E0103](source_excerpts.md#e0103), [E0104](source_excerpts.md#e0104).

## S10: VoidSight

Citation key: `xiaotian2025collaborative`.

Collaborative Agent Framework for Web Vulnerability Discovery in Source Code

Cutoff year/type: 2025 / conference.

Cited version: 2025, 2025 22nd International Computer Conference on Wavelet Active Media Technology and Information Processing (ICCWAMTIP).

DOI: 10.1109/ICCWAMTIP68645.2025.11352622.

### Coding

- **principal contribution**: Discovery
- **lifecycle coverage**: D, A
- **supporting stage outputs**: None
- **task families**: Identify, Characterize, Verify
- **knowledge resources**: VR, Code, Context
- **retrieval components**: DR
- **integration route**: Workflow
- **repeated conditioning**: True
- **reasoning mode**: MAR
- **contrastive comparison**: False

### Extraction

**Task output summary.** Produces web-code vulnerability findings, data-flow and exploitability analysis, and proofs of vulnerability.

**Query.** Target project source lines

**Knowledge unit representation index.** GHSA vulnerable lines embedded with bge in language-specific FAISS; condensed descriptions and CVE IDs attached as metadata

**Selection filtering reranking.** Similarity thresholds; relaxed fallback; suspicious line shortlist

**Evidence integration.** Retrieval-guided collaborative data-flow and exploitability dialogue

**Models and roles.** GPT-5; DeepSeek-V3.1; Qwen3-Coder-480B-A35B; GLM-4.6

**Baselines.** Embedding variants; standalone/tool agent comparisons

**Evaluation protocol.** 323 nonoverlapping CVE recall cases; confirmed precision/rare-CWE/OOD; 8 real projects

**Benchmarks.** CVEfixes , manually confirmed precision benchmark, OOD rare-CWE test, GitHub web projects

**Evaluation context.** PHP, Python, Java, Go, JavaScript, TypeScript

**Evaluation granularity.** File/line/project-level

**Reported metrics.** Rec., Prec., Acc., Silhouette coefficient, time, dialogue rounds, cost-effectiveness, number of CVEs found

Extraction source locators: [E0106](source_excerpts.md#e0106), [E0107](source_excerpts.md#e0107), [E0108](source_excerpts.md#e0108), [E0109](source_excerpts.md#e0109), [E0110](source_excerpts.md#e0110), [E0111](source_excerpts.md#e0111), [E0112](source_excerpts.md#e0112), [E0113](source_excerpts.md#e0113), [E0114](source_excerpts.md#e0114), [E0115](source_excerpts.md#e0115), [E0116](source_excerpts.md#e0116), [E0117](source_excerpts.md#e0117), [E0118](source_excerpts.md#e0118), [E0119](source_excerpts.md#e0119).

## S11: Argus

Citation key: `liang2026argus`.

Argus: Reorchestrating static analysis via a multi-agent ensemble for full-chain security vulnerability detection

Cutoff year/type: 2026 / preprint.

Cited version: 2026, arXiv preprint arXiv:2604.06633.

### Coding

- **principal contribution**: Discovery
- **lifecycle coverage**: D, A, M
- **supporting stage outputs**: M
- **task families**: Identify, Characterize, Verify, Recommend, Patch
- **knowledge resources**: VR, Code, Context
- **retrieval components**: RTR
- **integration route**: Workflow
- **repeated conditioning**: True
- **reasoning mode**: MAR
- **contrastive comparison**: False

### Extraction

**Task output summary.** Produces repository findings, vulnerable flows, root-cause reports, proofs of concept, and supporting repair recommendations or patches. Mitigation is not a separately evaluated principal endpoint.

**Query.** Project dependency IDs/versions and suspect sinks

**Knowledge unit representation index.** NVD/OSV/GHSA/Snyk and repository/issue/PoC records; CodeQL paths

**Selection filtering reranking.** Relevance, credibility, content-quality scores; primary/fork source priorities

**Evidence integration.** CVE retrieval, PoC/verification, CodeQL/flow-review agents; ReAct/Re3

**Models and roles.** Claude-3.5-Sonnet and Claude-4.5-Sonnet

**Baselines.** CodeQL and IRIS

**Evaluation protocol.** Real Java repository study; sink/path/vulnerability manual evidence and CVE assignments

**Benchmarks.** Seven open-source Java codebases

**Evaluation context.** Java

**Evaluation granularity.** Repository/system-level

**Reported metrics.** Detected sink count, detected vulnerability count, token consumption

Extraction source locators: [E0121](source_excerpts.md#e0121), [E0122](source_excerpts.md#e0122), [E0123](source_excerpts.md#e0123), [E0124](source_excerpts.md#e0124), [E0125](source_excerpts.md#e0125), [E0126](source_excerpts.md#e0126), [E0127](source_excerpts.md#e0127), [E0128](source_excerpts.md#e0128).

## S12: RLV

Citation key: `qiu2026rlv`.

RLV: LLM-based vulnerability detection by retrieving and refining contextual information

Cutoff year/type: 2026 / journal.

Cited version: 2026, Journal of Systems and Software.

DOI: 10.1016/j.jss.2025.112756.

### Coding

- **principal contribution**: Discovery
- **lifecycle coverage**: D
- **supporting stage outputs**: None
- **task families**: Identify
- **knowledge resources**: Code
- **retrieval components**: RTR
- **integration route**: Context
- **repeated conditioning**: False
- **reasoning mode**: CoT
- **contrastive comparison**: False

### Extraction

**Task output summary.** Produces function-level vulnerability classifications. Retrieved callers, callees, types, and generated summaries provide detection context.

**Query.** Target function, user-defined callees/callers/types

**Knowledge unit representation index.** Repository definitions; Tree-sitter; gtags/ctags; generated function summaries

**Selection filtering reranking.** LLM relevance filtering/ranking of callees and types

**Evidence integration.** Structured repository context; understand then reason stepwise

**Models and roles.** DeepSeek-R1

**Baselines.** CodeT5; LineVul; CodeBERT/UniXCoder and newer detectors

**Evaluation protocol.** FFmpeg/QEMU and DiverseVul; 8:1:1 split; training/test deduplication; extra random-split significance runs

**Benchmarks.** FFmpeg+QEMU , DiverseVul

**Evaluation context.** C/C++

**Evaluation granularity.** Function-level with callers/callees/types

**Reported metrics.** Acc., Prec., Rec., F1, cost per LLM call, human summary validity

Extraction source locators: [E0132](source_excerpts.md#e0132), [E0133](source_excerpts.md#e0133), [E0134](source_excerpts.md#e0134), [E0135](source_excerpts.md#e0135), [E0136](source_excerpts.md#e0136).

## S13: DeepDesc

Citation key: `tan2026deepdesc`.

DeepDesc: integrating retrieval-augmented generation with large language models for smart contract vulnerability detection

Cutoff year/type: 2025 / journal.

Cited version: 2026, Empirical Software Engineering.

DOI: 10.1007/s10664-025-10770-7.

### Coding

- **principal contribution**: Discovery
- **lifecycle coverage**: D
- **supporting stage outputs**: None
- **task families**: Identify
- **knowledge resources**: Context
- **retrieval components**: DR
- **integration route**: Feature
- **repeated conditioning**: False
- **reasoning mode**: DG
- **contrastive comparison**: False

### Extraction

**Task output summary.** Produces vulnerability classifications using code features and retrieval-conditioned descriptions. The generated descriptions are classifier inputs.

**Query.** Target smart-contract code

**Knowledge unit representation index.** Audit/report text; BERT vectors in FAISS; generated semantic descriptions

**Selection filtering reranking.** Nearest report retrieval

**Evidence integration.** Retrieved report in description prompt; low-rank bilinear code/text feature fusion

**Models and roles.** GPT-3.5 description generation

**Baselines.** GNN/CNN feature baselines; LLM prompting; GPTLens; GPT-5/Claude/DeepSeek comparison

**Evaluation protocol.** Smart-contract datasets; K-fold cross-validation; detection and description quality

**Benchmarks.** MAB , MUB , Top200 samples

**Evaluation context.** Solidity

**Evaluation granularity.** Function/contract-level

**Reported metrics.** Acc., Prec., Rec., F1, TP/TN/FP/FN, BLEU for code-description quality

Extraction source locators: [E0139](source_excerpts.md#e0139), [E0140](source_excerpts.md#e0140), [E0141](source_excerpts.md#e0141), [E0142](source_excerpts.md#e0142), [E0143](source_excerpts.md#e0143), [E0144](source_excerpts.md#e0144), [E0145](source_excerpts.md#e0145), [E0146](source_excerpts.md#e0146).

## S14: RAG-SmartVuln

Citation key: `nhu2025rag`.

RAG-SmartVuln: Enhancing smart contract vulnerability detection via retrieval-augmented LLMs

Cutoff year/type: 2025 / conference.

Cited version: 2025, 2025 International Conference on Multimedia Analysis and Pattern Recognition (MAPR).

DOI: 10.1109/MAPR67746.2025.11134018.

### Coding

- **principal contribution**: Discovery
- **lifecycle coverage**: D, A, M
- **supporting stage outputs**: M
- **task families**: Identify, Characterize, Recommend
- **knowledge resources**: VR, Code, Context
- **retrieval components**: SR, DR, HR, GSR
- **integration route**: Context
- **repeated conditioning**: True
- **reasoning mode**: CoT
- **contrastive comparison**: False

### Extraction

**Task output summary.** Produces contract vulnerability judgments, root causes, trigger and risk descriptions, and supporting remediation guidance.

**Query.** LLM-extracted contract purpose and behavior

**Knowledge unit representation index.** Functional-semantics/cause/remedy KG; text-embedding-3-large 3072D vectors

**Selection filtering reranking.** Top-30 embedding recall; BM25 lexical reranking; KG paths

**Evidence integration.** Top-k knowledge injected into fine-tuned detector; explanation/fix suggestion

**Models and roles.** Qwen2.5-Coder-14B; Qwen3-14B; DeepSeek-R1-Distill-Llama-8B; GPT-3.5 comparator

**Baselines.** No-RAG same models; Slither; Mythril

**Evaluation protocol.** SolidiFI and SmartBugs-Curated; same-model RAG/non-RAG comparisons; GPT-4o description/fix rubric

**Benchmarks.** SolidiFI-Benchmark , SmartBugs-Curated

**Evaluation context.** Solidity

**Evaluation granularity.** Function/contract-level

**Reported metrics.** Acc., Prec., Rec., F1, rubric-based description/fix quality score

Extraction source locators: [E0150](source_excerpts.md#e0150), [E0151](source_excerpts.md#e0151), [E0152](source_excerpts.md#e0152), [E0153](source_excerpts.md#e0153), [E0154](source_excerpts.md#e0154), [E0155](source_excerpts.md#e0155), [E0156](source_excerpts.md#e0156), [E0157](source_excerpts.md#e0157), [E0158](source_excerpts.md#e0158), [E0159](source_excerpts.md#e0159).

## S15: ParaVul

Citation key: `huang2025paravul`.

ParaVul: A Parallel Large Language Model and Retrieval-Augmented Framework for Smart Contract Vulnerability Detection

Cutoff year/type: 2026 / journal.

Cited version: 2026, IEEE Transactions on Information Forensics and Security.

DOI: 10.1109/TIFS.2026.3694661.

### Coding

- **principal contribution**: Discovery
- **lifecycle coverage**: D, A, M
- **supporting stage outputs**: M
- **task families**: Identify, Characterize, Recommend
- **knowledge resources**: Code
- **retrieval components**: SR, DR, HR
- **integration route**: Feature
- **repeated conditioning**: False
- **reasoning mode**: CoT
- **contrastive comparison**: False

### Extraction

**Task output summary.** Produces contract vulnerability labels and reports describing locations, manifestations, root causes, risks, impacts, and mitigation recommendations.

**Query.** Target contract token/chunk sequence

**Knowledge unit representation index.** Contract vulnerability case corpus; sparse BM25 and dense vector channels

**Selection filtering reranking.** Parallel BM25 and dense retrieval; prediction-vector fusion

**Evidence integration.** Parallel SLoRA LLM detection and retrieval-based neighbor voting. A learned verification module fuses predictions. The CoT reporter consumes the fused result and processed target contract.

**Models and roles.** LLaMA-7B/13B with SLoRA; GPT-4o comparison

**Baselines.** LLM-only; BM25-RAG; dense-RAG; QLoRA/QALoRA variants

**Evaluation protocol.** SC_UEE and ScrawlD; single- and multi-label evaluation

**Benchmarks.** SC_UEE, ScrawlD

**Evaluation context.** Solidity/Ethereum

**Evaluation granularity.** Contract-level

**Reported metrics.** Acc., Prec., Rec., F1, inference time, GPU memory usage

Extraction source locators: [E0163](source_excerpts.md#e0163), [E0164](source_excerpts.md#e0164), [E0165](source_excerpts.md#e0165), [E0166](source_excerpts.md#e0166), [E0167](source_excerpts.md#e0167), [E0168](source_excerpts.md#e0168), [E0169](source_excerpts.md#e0169), [E0170](source_excerpts.md#e0170), [E0171](source_excerpts.md#e0171), [E0172](source_excerpts.md#e0172), [E0173](source_excerpts.md#e0173), [E0174](source_excerpts.md#e0174), [E0175](source_excerpts.md#e0175), [E0176](source_excerpts.md#e0176).

## S16: TaK-Fuzz

Citation key: `khoa2025tak`.

TaK-Fuzz: Transaction-aware Knowledge Smart Contract Fuzzing with Retrieval-Augmented Generation and Language Models

Cutoff year/type: 2025 / conference.

Cited version: 2025, 2025 RIVF International Conference on Computing and Communication Technologies (RIVF).

DOI: 10.1109/RIVF68649.2025.11365172.

### Coding

- **principal contribution**: Discovery
- **lifecycle coverage**: D
- **supporting stage outputs**: None
- **task families**: Test
- **knowledge resources**: VR, Context
- **retrieval components**: DR, GSR
- **integration route**: Context
- **repeated conditioning**: False
- **reasoning mode**: CoT
- **contrastive comparison**: False

### Extraction

**Task output summary.** Generates executable exploit templates, transaction sequences, and fuzzing inputs for vulnerability discovery.

**Query.** Target functions mapped to SWC classes; contract semantics

**Knowledge unit representation index.** SWC/DAppSCAN knowledge chunks; embeddings; function/ABI/transaction constraints

**Selection filtering reranking.** SWC class filtering then semantic score

**Evidence integration.** Context plus contract generates transaction-aware fuzzing templates

**Models and roles.** Gemini-2.5-flash-lite-preview-06-17

**Baselines.** MuFuzz

**Evaluation protocol.** D2 and Soli-Audit 65 contracts each; coverage/recall/resource comparisons

**Benchmarks.** D2 Benchmark , SoliAudit

**Evaluation context.** Solidity/EVM

**Evaluation granularity.** Contract-level

**Reported metrics.** Branch coverage, vulnerability recall, average test cases per contract

Extraction source locators: [E0179](source_excerpts.md#e0179), [E0180](source_excerpts.md#e0180), [E0181](source_excerpts.md#e0181), [E0182](source_excerpts.md#e0182), [E0183](source_excerpts.md#e0183), [E0184](source_excerpts.md#e0184), [E0185](source_excerpts.md#e0185), [E0186](source_excerpts.md#e0186).

## S17: UniFuzz

Citation key: `nhat2025unifuzz`.

UniFuzz: A Unified Fuzzing Framework for Smart Contract Vulnerability Detection with LLMs and Audit Reports

Cutoff year/type: 2025 / conference.

Cited version: 2025, 2025 2nd International Conference On Cryptography And Information Security (VCRIS).

DOI: 10.1109/VCRIS68011.2025.11250519.

### Coding

- **principal contribution**: Discovery
- **lifecycle coverage**: D
- **supporting stage outputs**: None
- **task families**: Test
- **knowledge resources**: Context
- **retrieval components**: DR
- **integration route**: Workflow
- **repeated conditioning**: True
- **reasoning mode**: MAR
- **contrastive comparison**: False

### Extraction

**Task output summary.** Generates transaction sequences and parameters and reports fuzzing discoveries. External expert confirmation is part of evaluation.

**Query.** Function context for parameters and transaction sequence

**Knowledge unit representation index.** Audit report chunks; FAISS vector store

**Selection filtering reranking.** Top-k cosine-similarity chunks

**Evidence integration.** Static/data-flow/semantic context plus RAG; code/input/feedback agents

**Models and roles.** Gemini-1.5-flash

**Baselines.** Existing smart-contract fuzzers

**Evaluation protocol.** SoliAudit and Etherscan; single/cross-contract campaigns; manual vulnerability validation

**Benchmarks.** SoliAudit, Etherscan

**Evaluation context.** Solidity/EVM

**Evaluation granularity.** Contract-level

**Reported metrics.** Code coverage, branch coverage, detection accuracy, validated vulnerability count

Extraction source locators: [E0189](source_excerpts.md#e0189), [E0190](source_excerpts.md#e0190), [E0191](source_excerpts.md#e0191), [E0192](source_excerpts.md#e0192), [E0193](source_excerpts.md#e0193), [E0194](source_excerpts.md#e0194).

## S18: DSS

Citation key: `wang2025llm`.

LLM Assisted Dual-View Awareness Framework for Smart Contract Vulnerability Detection

Cutoff year/type: 2025 / conference.

Cited version: 2025, 2025 IEEE 36th International Symposium on Software Reliability Engineering (ISSRE).

DOI: 10.1109/ISSRE66568.2025.00022.

### Coding

- **principal contribution**: Discovery
- **lifecycle coverage**: D
- **supporting stage outputs**: None
- **task families**: Identify
- **knowledge resources**: VR, Code, Context
- **retrieval components**: DR, GSR
- **integration route**: Feature
- **repeated conditioning**: False
- **reasoning mode**: CoT
- **contrastive comparison**: False

### Extraction

**Task output summary.** Produces a vulnerable/secure classification by fusing structural features with semantic features derived from an LLM report.

**Query.** Target smart-contract feature patterns

**Knowledge unit representation index.** Vulnerability snippets/patterns; cosine similarity; contract graph features

**Selection filtering reranking.** Feature-pattern matching with cosine similarity

**Evidence integration.** LLM semantic report and GNN structural features; co-attention

**Models and roles.** GPT-4o and DeepSeek-R1

**Baselines.** Peculiar; GPTLens; LLM-SmartAudit; GNNs; TF-IDF/BM25 retrieval ablations

**Evaluation protocol.** ESC and Qian et al. smart-contract data; 8:2 train/test; classifier metrics and retrieval/feature ablations

**Benchmarks.** Ethereum Smart Contracts, Smart-Contract-Dataset

**Evaluation context.** Solidity/Ethereum

**Evaluation granularity.** Function/contract-level

**Reported metrics.** Acc., Prec., Rec., F1, detection time, monetary cost

Extraction source locators: [E0197](source_excerpts.md#e0197), [E0198](source_excerpts.md#e0198), [E0199](source_excerpts.md#e0199), [E0200](source_excerpts.md#e0200), [E0201](source_excerpts.md#e0201), [E0202](source_excerpts.md#e0202), [E0203](source_excerpts.md#e0203), [E0204](source_excerpts.md#e0204), [E0205](source_excerpts.md#e0205), [E0206](source_excerpts.md#e0206), [E0207](source_excerpts.md#e0207).

## S19: ORACAL

Citation key: `dai2026oracal`.

ORACAL: A Robust and Explainable Multimodal Framework for Smart Contract Vulnerability Detection with Causal Graph Enrichment

Cutoff year/type: 2026 / preprint.

Cited version: 2026, arXiv preprint arXiv:2603.28128.

### Coding

- **principal contribution**: Discovery
- **lifecycle coverage**: D, A
- **supporting stage outputs**: None
- **task families**: Identify, Characterize
- **knowledge resources**: VR, Context
- **retrieval components**: DR, GSR
- **integration route**: Feature
- **repeated conditioning**: False
- **reasoning mode**: CoT
- **contrastive comparison**: False

### Extraction

**Task output summary.** Produces multilabel vulnerability predictions, explanatory subgraphs, triggering statements, and root-cause or path evidence.

**Query.** Textual critical node/edge/subgraph context

**Knowledge unit representation index.** Solidity/EVM and audit-document chunks, represented with bge embeddings in Milvus.

**Selection filtering reranking.** Top-10 recall followed by cross-encoder reranking to retain three passages.

**Evidence integration.** Retrieved passages support node/edge semantic enrichment before learned feature fusion.

**Models and roles.** Gemini 3 Flash (gemini-3-flash-preview)

**Baselines.** No-enrichment and causal/feature ablations; existing graph/contract detectors

**Evaluation protocol.** 80:20 multilabel-stratified SoliAudit/CGT; DAppSCAN and LLMAV OOD only; address dedup; five runs

**Benchmarks.** SoliAudit , CGT Weakness , DAppSCAN , LLMAV

**Evaluation context.** Solidity

**Evaluation granularity.** Contract-level graph and explanation

**Reported metrics.** Acc./Jaccard, Prec., Rec., F1, Attack Success Rate (ASR), Mean Statement Precision (MSP), Mean Statement Recall (MSR), Mean Intersection over Union (MIoU), inference time

Extraction source locators: [E0210](source_excerpts.md#e0210), [E0211](source_excerpts.md#e0211), [E0212](source_excerpts.md#e0212), [E0213](source_excerpts.md#e0213), [E0214](source_excerpts.md#e0214), [E0215](source_excerpts.md#e0215), [E0216](source_excerpts.md#e0216), [E0217](source_excerpts.md#e0217), [E0218](source_excerpts.md#e0218), [E0219](source_excerpts.md#e0219), [E0220](source_excerpts.md#e0220), [E0221](source_excerpts.md#e0221), [E0222](source_excerpts.md#e0222), [E0223](source_excerpts.md#e0223), [E0224](source_excerpts.md#e0224), [E0225](source_excerpts.md#e0225), [E0226](source_excerpts.md#e0226).

## S25: SmartAuditFlow

Citation key: `wei2025smartauditflow`.

SmartAuditFlow: A dynamic plan-execute framework for advanced smart contract security analysis

Cutoff year/type: 2025 / journal.

Cited version: 2026, ACM Transactions on Software Engineering and Methodology.

DOI: 10.1145/3785364.

### Coding

- **principal contribution**: Discovery
- **lifecycle coverage**: D, A, M
- **supporting stage outputs**: M
- **task families**: Identify, Characterize, Verify, Recommend
- **knowledge resources**: VR, Context
- **retrieval components**: DR
- **integration route**: Workflow
- **repeated conditioning**: True
- **reasoning mode**: MAR
- **contrastive comparison**: False

### Extraction

**Task output summary.** Produces validated audit findings, locations, severity, business impact, exploitability and root-cause analysis, and mitigation recommendations.

**Query.** Audit task/contract security query

**Knowledge unit representation index.** Security-document chunks of 512 tokens with 128-token overlap, encoded with Sentence-BERT.

**Selection filtering reranking.** Top-5 cosine matches, threshold 0.72 with a 0.68 fallback, and optional MMR (λ=0.7).

**Evidence integration.** Retrieved context with source metadata supports audit planning and execution alongside static evidence and validator feedback.

**Models and roles.** GPT-4o default; Gemini-2.5-Pro/Claude-3.7-Sonnet/DeepSeek-V3 tested

**Baselines.** Traditional analyzers; instruction and reasoning LLMs; no-RAG/static/plan ablations

**Evaluation protocol.** SmartBugs-Curated; Code4rena; Sherlock; 13-CVE/DeFi validation; accuracy/ranking/cost

**Benchmarks.** Standard Vulnerability Set, SmartBugs-Curated, Code4rena, Sherlock, CVE Set

**Evaluation context.** Solidity, audit reports, CVE records

**Evaluation granularity.** Contract/project/finding level

**Reported metrics.** Precision, Recall, F1, Top-N accuracy, MRR, MAP, average outputs, average steps, cost, execution time

Extraction source locators: [E0230](source_excerpts.md#e0230), [E0231](source_excerpts.md#e0231), [E0232](source_excerpts.md#e0232), [E0233](source_excerpts.md#e0233), [E0234](source_excerpts.md#e0234), [E0235](source_excerpts.md#e0235), [E0236](source_excerpts.md#e0236), [E0237](source_excerpts.md#e0237).

## S20: ReVul-CoT

Citation key: `chen2026revul`.

ReVul-CoT: Towards effective software vulnerability assessment with retrieval-augmented generation and chain-of-thought prompting

Cutoff year/type: 2026 / journal.

Cited version: 2026, Journal of Systems and Software.

DOI: 10.1016/j.jss.2026.112855.

### Coding

- **principal contribution**: Analysis
- **lifecycle coverage**: A
- **supporting stage outputs**: None
- **task families**: Characterize
- **knowledge resources**: VR, Code
- **retrieval components**: DR
- **integration route**: Context
- **repeated conditioning**: False
- **reasoning mode**: CoT
- **contrastive comparison**: False

### Extraction

**Task output summary.** Produces CVSS v3 severity classes and reasoning about exploitability, impact, attack vectors, privileges, and CWE context.

**Query.** Target code and CVE description

**Knowledge unit representation index.** Historical code+description+severity records; CodeBERT and CoSENT embeddings

**Selection filtering reranking.** Weighted bimodal similarity; top-k examples

**Evidence integration.** Dynamic few-shot CoT using CWE/CVSS/impact/exploitability examples

**Models and roles.** DeepSeek-V3.1; GLM-4.5; Gemini-2.5-Pro; Qwen3-Coder-30B-A3B-Instruct

**Baselines.** Code-based, description-based and bimodal severity classifiers

**Evaluation protocol.** Stratified 80% knowledge/10% validation/10% test; index only knowledge partition; Macro-F1/MCC

**Benchmarks.** MegaVul

**Evaluation context.** CVE-linked vulnerability records

**Evaluation granularity.** CVE/code-record level

**Reported metrics.** Acc., F1, MCC, token usage

Extraction source locators: [E0241](source_excerpts.md#e0241), [E0242](source_excerpts.md#e0242), [E0243](source_excerpts.md#e0243), [E0244](source_excerpts.md#e0244), [E0245](source_excerpts.md#e0245), [E0246](source_excerpts.md#e0246), [E0247](source_excerpts.md#e0247), [E0248](source_excerpts.md#e0248), [E0249](source_excerpts.md#e0249), [E0250](source_excerpts.md#e0250), [E0251](source_excerpts.md#e0251), [E0252](source_excerpts.md#e0252), [E0253](source_excerpts.md#e0253), [E0254](source_excerpts.md#e0254), [E0255](source_excerpts.md#e0255), [E0256](source_excerpts.md#e0256), [E0257](source_excerpts.md#e0257), [E0258](source_excerpts.md#e0258), [E0259](source_excerpts.md#e0259), [E0260](source_excerpts.md#e0260).

## S21: ChatNVD

Citation key: `chopra2026chatnvd`.

ChatNVD: Advancing cybersecurity vulnerability assessment with large language models

Cutoff year/type: 2026 / journal.

Cited version: 2026, IEEE Access.

DOI: 10.1109/ACCESS.2026.3659205.

### Coding

- **principal contribution**: Analysis
- **lifecycle coverage**: A
- **supporting stage outputs**: None
- **task families**: Characterize
- **knowledge resources**: VR
- **retrieval components**: SR
- **integration route**: Context
- **repeated conditioning**: False
- **reasoning mode**: DG
- **contrastive comparison**: False

### Extraction

**Task output summary.** Answers vulnerability questions using NVD descriptions, dates, exploitability, impact, and severity information.

**Query.** User vulnerability question

**Knowledge unit representation index.** NVD JSON text chunks; TF-IDF index

**Selection filtering reranking.** TF-IDF similarity; dedup/record cleanup

**Evidence integration.** Shared grounded query+context prompt across models

**Models and roles.** GPT-4o-mini; Llama-3; Gemini-1.5-Pro

**Baselines.** Same fixed retrieval pipeline across LLMs; embedding technique comparisons

**Evaluation protocol.** Curated question batches; factual/error/omission/cost metrics

**Benchmarks.** NVD-derived QA benchmark

**Evaluation context.** CVE/NVD records

**Evaluation granularity.** Question-level

**Reported metrics.** Accuracy by batch/question type, hallucination rate, omission rate, processing failure/error rate, cost per correct answer, efficiency score

Extraction source locators: [E0263](source_excerpts.md#e0263), [E0264](source_excerpts.md#e0264), [E0265](source_excerpts.md#e0265), [E0266](source_excerpts.md#e0266), [E0267](source_excerpts.md#e0267), [E0268](source_excerpts.md#e0268), [E0269](source_excerpts.md#e0269), [E0270](source_excerpts.md#e0270), [E0271](source_excerpts.md#e0271).

## S22: ProveRAG

Citation key: `fayyazi2025proverag`.

ProveRAG: Provenance-driven vulnerability analysis with automated retrieval-augmented LLMs

Cutoff year/type: 2025 / journal.

Cited version: 2025, IEEE Access.

DOI: 10.1109/ACCESS.2025.3638251.

### Coding

- **principal contribution**: Analysis
- **lifecycle coverage**: A, M
- **supporting stage outputs**: M
- **task families**: Characterize, Recommend
- **knowledge resources**: VR, Context
- **retrieval components**: DR, RTR
- **integration route**: Context
- **repeated conditioning**: True
- **reasoning mode**: HSR
- **contrastive comparison**: False

### Extraction

**Task output summary.** Produces exploitation and mitigation answers, rationales, source provenance, and self-critique for a specified CVE.

**Query.** CVE ID plus exploitation or mitigation question

**Knowledge unit representation index.** NVD, CWE, and linked source documents, summarized for answers and embedded as raw chunks for provenance.

**Selection filtering reranking.** Source traversal for answer context and dense top-10 raw-chunk retrieval for provenance assessment.

**Evidence integration.** Summaries condition exploitation/mitigation answers. Raw chunks condition subsequent self-critique.

**Models and roles.** GPT-4o-mini; Llama-3.1-8B comparison

**Baselines.** Prompt-only; vector-chunking retrieval; summary/retrieval variants

**Evaluation protocol.** 482 critical 2024 CVEs; exploitation/mitigation QA and TP/FP/FN provenance

**Benchmarks.** Critical 2024 CVE benchmark

**Evaluation context.** CVE/NVD/CWE records

**Evaluation granularity.** CVE-document level

**Reported metrics.** LLM self-critique TP/FP/FN, accuracy/TP rate for exploitation and mitigation, response–evidence ROUGE-L and cosine similarity, guardrail/refusal count

Extraction source locators: [E0275](source_excerpts.md#e0275), [E0276](source_excerpts.md#e0276), [E0277](source_excerpts.md#e0277), [E0278](source_excerpts.md#e0278), [E0279](source_excerpts.md#e0279), [E0280](source_excerpts.md#e0280), [E0281](source_excerpts.md#e0281), [E0282](source_excerpts.md#e0282), [E0283](source_excerpts.md#e0283), [E0284](source_excerpts.md#e0284), [E0285](source_excerpts.md#e0285), [E0286](source_excerpts.md#e0286), [E0287](source_excerpts.md#e0287), [E0288](source_excerpts.md#e0288), [E0289](source_excerpts.md#e0289), [E0290](source_excerpts.md#e0290), [E0291](source_excerpts.md#e0291), [E0292](source_excerpts.md#e0292), [E0293](source_excerpts.md#e0293), [E0294](source_excerpts.md#e0294), [E0295](source_excerpts.md#e0295), [E0296](source_excerpts.md#e0296), [E0297](source_excerpts.md#e0297), [E0298](source_excerpts.md#e0298), [E0299](source_excerpts.md#e0299), [E0300](source_excerpts.md#e0300), [E0301](source_excerpts.md#e0301), [E0302](source_excerpts.md#e0302).

## S23: VDM-IOG

Citation key: `yu2026vdm`.

VDM-IOG, a framework of inference on graph in retrieval-augmented generation for vulnerability description mapping

Cutoff year/type: 2026 / journal.

Cited version: 2026, Cybersecurity.

DOI: 10.1186/s42400-025-00413-1.

### Coding

- **principal contribution**: Analysis
- **lifecycle coverage**: A
- **supporting stage outputs**: None
- **task families**: Characterize
- **knowledge resources**: VR, Context
- **retrieval components**: GSR
- **integration route**: Workflow
- **repeated conditioning**: True
- **reasoning mode**: GR
- **contrastive comparison**: False

### Extraction

**Task output summary.** Maps CVEs to MITRE ATT&CK techniques and produces exploitation and impact descriptions with structured answers and reasons.

**Query.** Entities/questions derived from CVE description

**Knowledge unit representation index.** VDM-M/ATT&CK knowledge graph; entity/relation records

**Selection filtering reranking.** Iterative depth-first graph query; LLM path scoring/reflection

**Evidence integration.** Identification→querying→scoring→questioning→reflection

**Models and roles.** GPT-3.5/GPT-4/GPT-4o; Llama3-8B/70B; Mistral/GLM variants

**Baselines.** Plain/CoT/self-consistency; vector LlamaIndex; DATER/LLM-KG/ToG; NER baselines

**Evaluation protocol.** 2018 mapping samples; 1247 NER; comparison dataset 8:1:1; manual cleaned labels

**Benchmarks.** CVE database, named-entity recognition (NER), and comparison datasets

**Evaluation context.** CVE/MITRE ATT

**Evaluation granularity.** CK

**Reported metrics.** Precision, Recall, Micro-F1, Macro-F1, NER Precision, NER Recall, NER F1

Extraction source locators: [E0306](source_excerpts.md#e0306), [E0307](source_excerpts.md#e0307), [E0308](source_excerpts.md#e0308), [E0309](source_excerpts.md#e0309), [E0310](source_excerpts.md#e0310), [E0311](source_excerpts.md#e0311), [E0312](source_excerpts.md#e0312), [E0313](source_excerpts.md#e0313).

## S24: CRVA-TGRAG

Citation key: `zhou2026tug`.

Tug-of-War within A Decade: Conflict Resolution in Vulnerability Analysis via Teacher-Guided Retrieval-Augmented Generations

Cutoff year/type: 2026 / preprint.

Cited version: 2026, arXiv preprint arXiv:2604.14172.

### Coding

- **principal contribution**: Analysis
- **lifecycle coverage**: A
- **supporting stage outputs**: None
- **task families**: Characterize
- **knowledge resources**: VR
- **retrieval components**: SR, DR, HR
- **integration route**: Context
- **repeated conditioning**: False
- **reasoning mode**: DG
- **contrastive comparison**: False

### Extraction

**Task output summary.** Produces conflict-resolved CVE answers and updated information, including old and new values and change descriptions.

**Query.** User CVE question with conflicting historical/new knowledge

**Knowledge unit representation index.** Official CVE/NVD parent documents; semantic subchunks; BM25 and vector index

**Selection filtering reranking.** Parent-document/semantic chunking; weighted vector (0.25) and BM25 (0.75) ensemble; synonym/subquestion query variants

**Evidence integration.** Stage I retrieval/augmentation; Stage II preference optimization and answer generation

**Models and roles.** DPO-Llama3-8B and DPO-Mistral-8B; GPT-4o-mini in no-DPO RAG variant

**Baselines.** No-prompt/prompt-only Claude-3.5-Haiku and Gemini-2.0-Flash-Exp; naive RAG; no-DPO variant

**Evaluation protocol.** CVE knowledge-conflict QA; RAGAS context/faithfulness and lexical answer metrics

**Benchmarks.** CVE knowledge-conflict dataset from official CVE GitHub data and NVD API

**Evaluation context.** CVE/NVD records

**Evaluation granularity.** CVE-document level

**Reported metrics.** Answer correctness, answer relevance, answer similarity, faithfulness, context precision, context recall, BLEU, ROUGE-L

Extraction source locators: [E0317](source_excerpts.md#e0317), [E0318](source_excerpts.md#e0318), [E0319](source_excerpts.md#e0319), [E0320](source_excerpts.md#e0320), [E0321](source_excerpts.md#e0321), [E0322](source_excerpts.md#e0322), [E0323](source_excerpts.md#e0323), [E0324](source_excerpts.md#e0324), [E0325](source_excerpts.md#e0325), [E0326](source_excerpts.md#e0326), [E0327](source_excerpts.md#e0327), [E0328](source_excerpts.md#e0328), [E0329](source_excerpts.md#e0329), [E0330](source_excerpts.md#e0330), [E0331](source_excerpts.md#e0331), [E0332](source_excerpts.md#e0332), [E0333](source_excerpts.md#e0333), [E0334](source_excerpts.md#e0334), [E0335](source_excerpts.md#e0335), [E0336](source_excerpts.md#e0336), [E0337](source_excerpts.md#e0337).

## S26: RAR

Citation key: `lotfi2025automated`.

Automated vulnerability validation and verification: A large language model approach

Cutoff year/type: 2025 / preprint.

Cited version: 2025, arXiv preprint arXiv:2509.24037.

### Coding

- **principal contribution**: Analysis
- **lifecycle coverage**: A
- **supporting stage outputs**: None
- **task families**: Characterize, Verify
- **knowledge resources**: VR, Code, Context
- **retrieval components**: RTR
- **integration route**: Workflow
- **repeated conditioning**: True
- **reasoning mode**: HSR
- **contrastive comparison**: False

### Extraction

**Task output summary.** Produces vulnerability representations, container environments, exploit scripts, test cases, execution logs, and reproduction results for known CVEs. Iterative repair changes reproduction artifacts.

**Query.** CVE ID/description, referenced sources and missing reproduction requirements

**Knowledge unit representation index.** CVE links, commits, PoCs/blogs/advisories; web/file tools

**Selection filtering reranking.** Reference traversal; iterative failure-driven environment/PoC correction

**Evidence integration.** Condition extraction→Docker environment→PoC execution→repair loop

**Models and roles.** GPT-4o default; DeepSeek-V3/Qwen3/Llama-3.3/Gemini comparisons

**Baselines.** Alternative LLMs and pipeline component/reproduction comparisons

**Evaluation protocol.** 102 CVEs from 55 projects/9 languages; 71 reproduced; executable container validation

**Benchmarks.** Multi-language CVE reproduction benchmark

**Evaluation context.** Multi-language OSS

**Evaluation granularity.** CVE/project/container-level

**Reported metrics.** Reproduction success rate, failure rate, step-level success/failure rate, iteration count, execution time

Extraction source locators: [E0344](source_excerpts.md#e0344), [E0345](source_excerpts.md#e0345), [E0346](source_excerpts.md#e0346), [E0347](source_excerpts.md#e0347), [E0348](source_excerpts.md#e0348), [E0349](source_excerpts.md#e0349), [E0350](source_excerpts.md#e0350), [E0351](source_excerpts.md#e0351), [E0352](source_excerpts.md#e0352), [E0353](source_excerpts.md#e0353).

## S31: VulLibGen

Citation key: `chen2024vullibgen`.

VulLibGen: Generating names of vulnerability-affected packages via a large language model

Cutoff year/type: 2024 / conference.

Cited version: 2024, Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).

DOI: 10.18653/v1/2024.acl-long.527.

### Coding

- **principal contribution**: Analysis
- **lifecycle coverage**: A
- **supporting stage outputs**: None
- **task families**: Characterize
- **knowledge resources**: Context
- **retrieval components**: SR
- **integration route**: Context
- **repeated conditioning**: False
- **reasoning mode**: DG
- **contrastive comparison**: False

### Extraction

**Task output summary.** Maps known vulnerability descriptions to affected software packages using retrieved package documentation and local name correction.

**Query.** Vulnerability description within a specified ecosystem

**Knowledge unit representation index.** Package names and descriptions within the target ecosystem.

**Selection filtering reranking.** TF-IDF recall followed by BERT reranking of 512 candidates.

**Evidence integration.** Selected package descriptions condition name generation, followed by local name correction.

**Models and roles.** GPT-3.5-turbo; GPT-4-1106-preview; Llama/Vicuna 7B/13B

**Baselines.** FastXML; LightXML; Chronos; VulLibMiner; non-RAG/SFT/ICL variants

**Evaluation protocol.** 9570 GitHub Advisory vulnerabilities (Java2789/JS3193/Python2237/Go1351); chronological 3:1:1; Precision/Recall@k; 34 accepted advisory links

**Benchmarks.** VulLib and GHSA-derived JavaScript, Python, and Go records

**Evaluation context.** Maven, npm, PyPI, Go

**Evaluation granularity.** Vulnerability-record level

**Reported metrics.** Precision@k, Recall@k, F1@k (k=1,2,3), runtime, accepted advisory corrections

Extraction source locators: [E0356](source_excerpts.md#e0356), [E0357](source_excerpts.md#e0357), [E0358](source_excerpts.md#e0358), [E0359](source_excerpts.md#e0359), [E0360](source_excerpts.md#e0360), [E0361](source_excerpts.md#e0361), [E0362](source_excerpts.md#e0362), [E0363](source_excerpts.md#e0363).

## S27: MR-LLM

Citation key: `amoah2025explainable`.

Explainable Recommendation of Software Vulnerability Repair Based on Metadata Retrieval and Multifaceted LLMs

Cutoff year/type: 2025 / journal.

Cited version: 2025, Machine Learning and Knowledge Extraction.

DOI: 10.3390/make7040149.

### Coding

- **principal contribution**: Mitigation
- **lifecycle coverage**: D, A, M
- **supporting stage outputs**: D, A
- **task families**: Identify, Characterize, Recommend, Patch
- **knowledge resources**: VR, Code
- **retrieval components**: SR, DR, HR
- **integration route**: Context
- **repeated conditioning**: False
- **reasoning mode**: HSR
- **contrastive comparison**: False

### Extraction

**Task output summary.** Produces repair recommendations and code fixes, with supporting vulnerability locations, issue descriptions, and root-cause information.

**Query.** Target vulnerable code and CWE/CVE identifiers

**Knowledge unit representation index.** Vulnerable/fixed code and CWE/CVE fields, with sparse and dense representations.

**Selection filtering reranking.** Vanilla, metadata-aware, and field-segmented retrieval configurations.

**Evidence integration.** Retrieved repair examples and chunk-level analyses condition code repair and recommendations.

**Models and roles.** GPT-4o; Llama3-8B-Instruct; Mixtral-8x7B; CodeLlama-34B

**Baselines.** Zero-shot same backbones; vanilla retrieval; prior repair methods; exact/reference metrics

**Evaluation protocol.** CWE/BigVul/CVEfixes; static-analysis repair assessment and LLM-judge rubrics

**Benchmarks.** BigVul, CVEfixes

**Evaluation context.** C/C++ and multi-language

**Evaluation granularity.** Snippet/file-level

**Reported metrics.** CodeBLEU, chrF, RUBY, EM, manual retrieval/repair inspection, fixed-file and resolved-issue rates, LLM-as-judge scores

Extraction source locators: [E0366](source_excerpts.md#e0366), [E0367](source_excerpts.md#e0367), [E0368](source_excerpts.md#e0368), [E0369](source_excerpts.md#e0369), [E0370](source_excerpts.md#e0370), [E0371](source_excerpts.md#e0371), [E0372](source_excerpts.md#e0372), [E0373](source_excerpts.md#e0373), [E0374](source_excerpts.md#e0374), [E0375](source_excerpts.md#e0375), [E0376](source_excerpts.md#e0376), [E0377](source_excerpts.md#e0377), [E0378](source_excerpts.md#e0378), [E0379](source_excerpts.md#e0379), [E0380](source_excerpts.md#e0380), [E0381](source_excerpts.md#e0381), [E0382](source_excerpts.md#e0382), [E0383](source_excerpts.md#e0383).

## S28: SCPatcher

Citation key: `li2026scpatcher`.

SCPatcher: Automated Smart Contract Code Repair via Retrieval-Augmented Generation and Knowledge Graph

Cutoff year/type: 2026 / preprint.

Cited version: 2026, Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering.

DOI: 10.1145/3803437.3805558.

### Coding

- **principal contribution**: Mitigation
- **lifecycle coverage**: M
- **supporting stage outputs**: None
- **task families**: Patch
- **knowledge resources**: Code
- **retrieval components**: DR, GSR
- **integration route**: Workflow
- **repeated conditioning**: True
- **reasoning mode**: HSR
- **contrastive comparison**: False

### Extraction

**Task output summary.** Generates and refines smart-contract patches and reports compilation and Slither-based repair outcomes.

**Query.** Vulnerable function vector and signature constraints

**Knowledge unit representation index.** Contract functions and their relations, with CodeBERT representations.

**Selection filtering reranking.** Top-50 semantic neighbors, signature compatibility, usage-based trust, and clone-diversity filtering.

**Evidence integration.** Selected repair knowledge conditions patch generation, followed by compilation and static-check feedback.

**Models and roles.** DeepSeek-V3

**Baselines.** DirectFix; LogicRepair; SelfRefine; standard RAG

**Evaluation protocol.** 200 contracts; hash dedup against 5000 KB; compilation and Slither-based elimination, not functional equivalence

**Benchmarks.** Smart contract repair test set

**Evaluation context.** Solidity

**Evaluation granularity.** Contract/function-level

**Reported metrics.** CPR, ERR, ORR, fixed-contract count

Extraction source locators: [E0391](source_excerpts.md#e0391), [E0392](source_excerpts.md#e0392), [E0393](source_excerpts.md#e0393), [E0394](source_excerpts.md#e0394), [E0395](source_excerpts.md#e0395), [E0396](source_excerpts.md#e0396), [E0397](source_excerpts.md#e0397), [E0398](source_excerpts.md#e0398), [E0399](source_excerpts.md#e0399), [E0400](source_excerpts.md#e0400).

## S29: PailGen

Citation key: `shao2026fix`.

Fix pattern-aware vulnerability patch generation via in-context learning

Cutoff year/type: 2026 / journal.

Cited version: 2026, ACM Transactions on Software Engineering and Methodology.

DOI: 10.1145/3796512.

### Coding

- **principal contribution**: Mitigation
- **lifecycle coverage**: M
- **supporting stage outputs**: None
- **task families**: Patch
- **knowledge resources**: Code
- **retrieval components**: SR, DR, HR
- **integration route**: Context
- **repeated conditioning**: False
- **reasoning mode**: DG
- **contrastive comparison**: False

### Extraction

**Task output summary.** Generates and purifies patch diffs using retrieved vulnerable-fixed function pairs and mined AST edit patterns.

**Query.** Target vulnerable function

**Knowledge unit representation index.** Vulnerable–fixed function pairs, indexed with BM25 and a CodeT5-initialized, fine-tuned dense passage retriever.

**Selection filtering reranking.** The target vulnerable function supplies the query. Weighted BM25 and dense scores rank historical repair pairs.

**Evidence integration.** Target code and its AST are combined with retrieved patch diffs and mined edit patterns to generate a patch diff.

**Models and roles.** DeepSeek-Coder-V2; GPT-3.5; CodeLlama/Magicoder/CodeGeeX/DeepSeek-Coder variants

**Baselines.** TFix; VRepair; VulRepair; VulMaster; VQM; prompt/LoRA/code LM baselines

**Evaluation protocol.** Dedup BigVul/CVEfixes; random splits there and D2A; chronological post-backbone CVED; CWEVAL functional/security tests

**Benchmarks.** BigVul, CVEfixes, D2A, CVED, CWEVAL-BENCH, ReposVul

**Evaluation context.** C/C++, Python

**Evaluation granularity.** Function-level repair

**Reported metrics.** EM, BLEU, CodeBLEU, func@k, func-sec@k, expert-rated retrieval failure, retrieved-case cosine similarity, patch performance under retrieval corruption

Extraction source locators: [E0404](source_excerpts.md#e0404), [E0405](source_excerpts.md#e0405), [E0406](source_excerpts.md#e0406), [E0407](source_excerpts.md#e0407), [E0408](source_excerpts.md#e0408), [E0409](source_excerpts.md#e0409), [E0410](source_excerpts.md#e0410), [E0411](source_excerpts.md#e0411), [E0412](source_excerpts.md#e0412), [E0413](source_excerpts.md#e0413).

## S30: AutoPatch

Citation key: `seo2025autopatch`.

AutoPatch: Multi-agent framework for patching real-world CVE vulnerabilities

Cutoff year/type: 2025 / preprint.

Cited version: 2025, arXiv preprint arXiv:2505.04195.

### Coding

- **principal contribution**: Mitigation
- **lifecycle coverage**: D, A, M
- **supporting stage outputs**: None
- **task families**: Identify, Characterize, Verify, Patch
- **knowledge resources**: VR, Code, Context
- **retrieval components**: SR, DR, HR, GSR
- **integration route**: Workflow
- **repeated conditioning**: True
- **reasoning mode**: MAR
- **contrastive comparison**: False

### Extraction

**Task output summary.** Matches target code to CVEs, verifies vulnerability presence, explains causes, generates patched code, and revisits it through verifier feedback.

**Query.** Target-code lexical/context/data-flow features

**Knowledge unit representation index.** CVE vulnerable/fixed code and descriptions; context vectors; DFG symbols

**Selection filtering reranking.** Keyword/Jaccard/fuzzy plus cosine plus DFG-symbol unified trainable score

**Evidence integration.** CVE matching, vulnerability verification, and patch generation. One-shot CoT prompting and verifier feedback condition subsequent generation.

**Models and roles.** CodeLlama-13B; DeepSeek-Coder-V2-Lite; DeepSeek-R1-32B; GPT-4o; o3-mini

**Baselines.** Zero-shot same backbones; VSP; transformed-code robustness variants

**Evaluation protocol.** 75 recent high-severity CVEs; 525 reimplemented snippets (375 in code-reimplementation evaluation); 70:15:15 similarity-model split; verifier and patch accuracy

**Benchmarks.** Recent high-severity CVE benchmark

**Evaluation context.** Linux kernel, Chromium, and related C/C++ systems

**Evaluation granularity.** Snippet/CVE-level

**Reported metrics.** CVE matching accuracy, vulnerability verification accuracy/F1, joint CoT+vulnerability accuracy/F1, patch accuracy, patch-verification loop count, cost

Extraction source locators: [E0419](source_excerpts.md#e0419), [E0420](source_excerpts.md#e0420), [E0421](source_excerpts.md#e0421), [E0422](source_excerpts.md#e0422), [E0423](source_excerpts.md#e0423), [E0424](source_excerpts.md#e0424), [E0425](source_excerpts.md#e0425), [E0426](source_excerpts.md#e0426), [E0427](source_excerpts.md#e0427), [E0428](source_excerpts.md#e0428), [E0429](source_excerpts.md#e0429).
