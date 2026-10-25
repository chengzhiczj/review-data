# Coding manual

These definitions document the codes released with the current manuscript.

One study contributes one principal stage, one integration route, and one principal reasoning mode. Stage coverage, task families, resources, retrieval components, and evaluation dimensions can overlap. Intermediate context is distinguished from delivered target-task outputs.

## Task families

- **Identify**: Vulnerability decisions, categories, or locations.
- **Test**: Generated test inputs, seeds, templates, or transaction/API sequences used for discovery.
- **Characterize**: Delivered vulnerability descriptions, causes, impact or severity assessments, mappings, and explanatory reports.
- **Verify**: Delivered verification, reproduction, or exploitability results for a reported vulnerability.
- **Recommend**: Actionable mitigation guidance; executable code changes are not required.
- **Patch**: Generated edits to vulnerable software. Validation is coded independently.

## Knowledge resources

- **VR**: Vulnerability Reference Resources: retrieved standardized vulnerability records, categories, or taxonomies.
- **Code**: Code-Centric Resources: code, patches, test artifacts, and program structures or relations.
- **Context**: Contextual and Procedural Knowledge: retrieved reports, issues, advisories, manuals, documentation, and procedures.

## Retrieval components

- **SR**: Sparse or lexical retrieval, including BM25 and TF-IDF.
- **DR**: Dense similarity retrieval over learned vector representations.
- **HR**: Combined lexical and dense selection in the reported workflow; also count its SR and DR components.
- **GSR**: Graph or structure-aware evidence selection.
- **RTR**: Repository, tool, or source lookup that conditions generation.

## Integration routes

- **Context**: Retrieved evidence conditions a principal generative solver whose output is used directly as a decision, answer, task artifact, or security-tool input. Same-model sequential prompting is included.
- **Workflow**: Retrieved evidence is coordinated through specialized agents, or grounded outputs interact with executable validators/fuzzers or a graph-query tool in a feedback/control loop that governs subsequent inference. A one-way generated-seed-to-fuzzer handoff alone remains Context.
- **Feature**: Generated descriptions/semantic enrichments or RAG predictions are integrated into learned feature/prediction fusion for the final task decision.

## Reasoning modes

- **CoT**: Chain-of-thought reasoning
- **GR**: Graph-query inference
- **HSR**: Hierarchical or staged reasoning
- **MAR**: Multi-agent reasoning
- **DG**: Direct generation

## Evaluation dimensions

- **retrieval_relevance**: Relevance or correctness of selected external evidence or CVE matches. Downstream task scores and operational ranking scores alone do not qualify.
- **context_recall**: Coverage of reference-answer claims or required evidence by the retrieved context. Classification, routing, package prediction, and source-code localization recall do not qualify.
- **provenance**: An evaluated relation between a generated output and its attributed source evidence. Merely displaying source links does not qualify. Similarity-based alignment is recorded as a proxy.
- **claim_faithfulness**: Support for individual generated claims in the supplied retrieval context. Overall answer correctness, reference similarity, or a holistic quality rubric alone does not qualify.
- **functional_correctness**: Execution of functional or regression tests on generated vulnerability patches. Compilation, reference matching, and an LLM quality judgment alone do not qualify.
- **post_repair_security**: Reported security checks of generated patched software. Static analysis, execution tests, and model-only verification are distinguished. Confirming the original vulnerability or an exploit does not qualify.

## Supporting stage outputs

Covered stages marked with a dagger in the manuscript; these are supporting outputs rather than the principal evaluation endpoint.

## Repeated conditioning

At inference, retrieved evidence or generated task artifacts are revisited in additional knowledge-item checks, analysis/critique, or execution/verification feedback. Offline KB mining, query construction/reranking, independent parallel chunks, and static preprocessing do not qualify.

## Principal reasoning rule

One principal mode per study. MAR for specialized-agent decision coordination; GR for explicit knowledge-graph path inference; HSR for task-specific staged decisions or generate/verify/refine; CoT for explicit stepwise reasoning within a contextual solver; DG for direct generation without those online reasoning architectures. Under Feature, DG describes the generative component, and Feature records the final learned decision.

## Contrastive comparison

Orthogonal evidence contrast: retrieved vulnerable, benign, or hard-negative alternatives are explicitly compared in target-task reasoning. It is not contrastive embedding training.

## Evaluation counting

Count a reported assessment with actual results for the dimension. Separate human/reference judgments from similarity-only proxies. Functional tests and post-repair security use all 31 and the five Patch-output studies as denominators.

## Evaluation missingness

Not reported describes an absent explicit evaluation in the reviewed text, not an absent system capability.

## Denominators and status codes

All corpus percentages use 31 studies. Functional correctness and post-repair security additionally use the five Patch-family studies. A study can contribute to more than one dimension. `not_reported` means no qualifying evaluation was reported in the reviewed text. It does not establish that the system lacks the capability. `not_applicable` identifies a non-Patch study for the two repair dimensions. Similarity proxies count as reported assessments but remain identifiable separately from human, reference-based, static, execution, or model-only checks.

- `retrieval_relevance`: `context_precision`, `gold_cve_match`, `human_diagnostic`, `human_sample`, `not_reported`, `similarity_proxy`
- `context_recall`: `not_reported`, `reference_claim_coverage`
- `provenance`: `not_reported`, `similarity_proxy`
- `claim_faithfulness`: `claim_context_support`, `not_reported`
- `functional_correctness`: `execution_tests`, `not_applicable`, `not_reported`
- `post_repair_security`: `execution_tests`, `llm_verifier`, `not_applicable`, `not_reported`, `static_analysis`

## Important coding boundaries

- HR also records its sparse and dense components. A cross-encoder reranker alone does not establish dense nearest-neighbor retrieval.
- Use of a graph or AST as prompt context alone does not establish graph-aware retrieval.
- Retrieval corpus contents do not by themselves establish delivered Analysis or Mitigation outputs.
- Fuzzer-input or reproduction-environment repair does not count as a software Patch output.
- Publication type at the search cutoff is independent of later bibliography updates.
