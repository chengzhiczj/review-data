# Six-dimension evaluation audit

The unit is one reported evaluation per study and dimension. `not_reported` does not imply the absence of a system capability. Repair dimensions apply to the five Patch-family studies. Similarity proxies remain explicitly labeled.

| Study | Retrieval relevance | Context recall | Provenance | Claim faithfulness | Functional correctness | Post-repair security |
|---|---|---|---|---|---|---|
| [SyzGPT](#s01) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [Vul-RAG](#s02) | human_diagnostic | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [RASM-Vul](#s03) | similarity_proxy | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [DeepVulHunter](#s04) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [CodeRAG](#s05) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [MulVul](#s06) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [HyVD-VP](#s07) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [KLRAG](#s08) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [VulRTex](#s09) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [VoidSight](#s10) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [Argus](#s11) | not_reported | not_reported | not_reported | not_reported | not_reported | not_reported |
| [RLV](#s12) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [DeepDesc](#s13) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [RAG-SmartVuln](#s14) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [ParaVul](#s15) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [TaK-Fuzz](#s16) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [UniFuzz](#s17) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [DSS](#s18) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [ORACAL](#s19) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [SmartAuditFlow](#s25) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [ReVul-CoT](#s20) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [ChatNVD](#s21) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [ProveRAG](#s22) | not_reported | not_reported | similarity_proxy | not_reported | not_applicable | not_applicable |
| [VDM-IOG](#s23) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [CRVA-TGRAG](#s24) | context_precision | reference_claim_coverage | not_reported | claim_context_support | not_applicable | not_applicable |
| [RAR](#s26) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [VulLibGen](#s31) | not_reported | not_reported | not_reported | not_reported | not_applicable | not_applicable |
| [MR-LLM](#s27) | human_sample | not_reported | not_reported | not_reported | not_reported | static_analysis |
| [SCPatcher](#s28) | not_reported | not_reported | not_reported | not_reported | not_reported | static_analysis |
| [PailGen](#s29) | human_sample | not_reported | not_reported | not_reported | execution_tests | execution_tests |
| [AutoPatch](#s30) | gold_cve_match | not_reported | not_reported | not_reported | not_reported | llm_verifier |

<a id="s01"></a>

## S01: SyzGPT

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Evaluation measures generated fuzzing-seed validity, context effectiveness, diversity, coverage, and discovered bugs. Context Effective Rate concerns generated syscall execution, not recall of retrieved reference evidence.

Evidence: [E0011](source_excerpts.md#e0011).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Evaluation measures generated fuzzing-seed validity, context effectiveness, diversity, coverage, and discovered bugs. Context Effective Rate concerns generated syscall execution, not recall of retrieved reference evidence.

Evidence: [E0011](source_excerpts.md#e0011).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Evaluation measures generated fuzzing-seed validity, context effectiveness, diversity, coverage, and discovered bugs. Context Effective Rate concerns generated syscall execution, not recall of retrieved reference evidence.

Evidence: [E0011](source_excerpts.md#e0011).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Evaluation measures generated fuzzing-seed validity, context effectiveness, diversity, coverage, and discovered bugs. Context Effective Rate concerns generated syscall execution, not recall of retrieved reference evidence.

Evidence: [E0011](source_excerpts.md#e0011).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Evaluation measures generated fuzzing-seed validity, context effectiveness, diversity, coverage, and discovered bugs. Context Effective Rate concerns generated syscall execution, not recall of retrieved reference evidence.

Evidence: [E0011](source_excerpts.md#e0011).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Evaluation measures generated fuzzing-seed validity, context effectiveness, diversity, coverage, and discovered bugs. Context Effective Rate concerns generated syscall execution, not recall of retrieved reference evidence.

Evidence: [E0011](source_excerpts.md#e0011).


<a id="s02"></a>

## S02: Vul-RAG

### retrieval_relevance

Status: `human_diagnostic`. Reported assessment: True. Applicable: True.

Manual attribution of irrelevant retrieval in 60 sampled FP/FN cases. This is failure-conditioned diagnosis, not whole-test-set retrieval precision. Table 8 and the FP prose contain inconsistent counts, so those detailed counts are not used in the synthesis.

Evidence: [E0019](source_excerpts.md#e0019), [E0020](source_excerpts.md#e0020).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Pairwise/balanced detection, developer usability, and manual failure analysis are reported. Knowledge helpfulness/preciseness ratings are holistic and do not test claim-level entailment. The failure analysis is conditioned on FP/FN cases.

Evidence: [E0021](source_excerpts.md#e0021), [E0022](source_excerpts.md#e0022), [E0023](source_excerpts.md#e0023).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Pairwise/balanced detection, developer usability, and manual failure analysis are reported. Knowledge helpfulness/preciseness ratings are holistic and do not test claim-level entailment. The failure analysis is conditioned on FP/FN cases.

Evidence: [E0021](source_excerpts.md#e0021), [E0022](source_excerpts.md#e0022), [E0023](source_excerpts.md#e0023).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Pairwise/balanced detection, developer usability, and manual failure analysis are reported. Knowledge helpfulness/preciseness ratings are holistic and do not test claim-level entailment. The failure analysis is conditioned on FP/FN cases.

Evidence: [E0021](source_excerpts.md#e0021), [E0022](source_excerpts.md#e0022), [E0023](source_excerpts.md#e0023).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Pairwise/balanced detection, developer usability, and manual failure analysis are reported. Knowledge helpfulness/preciseness ratings are holistic and do not test claim-level entailment. The failure analysis is conditioned on FP/FN cases.

Evidence: [E0021](source_excerpts.md#e0021), [E0022](source_excerpts.md#e0022), [E0023](source_excerpts.md#e0023).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Pairwise/balanced detection, developer usability, and manual failure analysis are reported. Knowledge helpfulness/preciseness ratings are holistic and do not test claim-level entailment. The failure analysis is conditioned on FP/FN cases.

Evidence: [E0021](source_excerpts.md#e0021), [E0022](source_excerpts.md#e0022), [E0023](source_excerpts.md#e0023).


<a id="s03"></a>

## S03: RASM-Vul

### retrieval_relevance

Status: `similarity_proxy`. Reported assessment: True. Applicable: True.

BERTScore between retrieved knowledge and reference vulnerability descriptions, with reported aggregate scores. No independently labeled relevance rate is supplied.

Evidence: [E0035](source_excerpts.md#e0035).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Main scores concern detection. BERTScore compares retrieved material with reference vulnerability descriptions and is a semantic proxy. Knowledge-base extraction checks and code-variant consistency checks concern preparation artifacts, not target-output source attribution or patch testing.

Evidence: [E0036](source_excerpts.md#e0036), [E0035](source_excerpts.md#e0035), [E0037](source_excerpts.md#e0037).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Main scores concern detection. BERTScore compares retrieved material with reference vulnerability descriptions and is a semantic proxy. Knowledge-base extraction checks and code-variant consistency checks concern preparation artifacts, not target-output source attribution or patch testing.

Evidence: [E0036](source_excerpts.md#e0036), [E0035](source_excerpts.md#e0035), [E0037](source_excerpts.md#e0037).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Main scores concern detection. BERTScore compares retrieved material with reference vulnerability descriptions and is a semantic proxy. Knowledge-base extraction checks and code-variant consistency checks concern preparation artifacts, not target-output source attribution or patch testing.

Evidence: [E0036](source_excerpts.md#e0036), [E0035](source_excerpts.md#e0035), [E0037](source_excerpts.md#e0037).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Main scores concern detection. BERTScore compares retrieved material with reference vulnerability descriptions and is a semantic proxy. Knowledge-base extraction checks and code-variant consistency checks concern preparation artifacts, not target-output source attribution or patch testing.

Evidence: [E0036](source_excerpts.md#e0036), [E0035](source_excerpts.md#e0035), [E0037](source_excerpts.md#e0037).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Main scores concern detection. BERTScore compares retrieved material with reference vulnerability descriptions and is a semantic proxy. Knowledge-base extraction checks and code-variant consistency checks concern preparation artifacts, not target-output source attribution or patch testing.

Evidence: [E0036](source_excerpts.md#e0036), [E0035](source_excerpts.md#e0035), [E0037](source_excerpts.md#e0037).


<a id="s04"></a>

## S04: DeepVulHunter

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Accuracy, precision, recall, and F1 concern vulnerability classification. Internal evaluator-agent decisions are not an independent reported evidence-quality endpoint.

Evidence: [E0046](source_excerpts.md#e0046).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Accuracy, precision, recall, and F1 concern vulnerability classification. Internal evaluator-agent decisions are not an independent reported evidence-quality endpoint.

Evidence: [E0046](source_excerpts.md#e0046).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Accuracy, precision, recall, and F1 concern vulnerability classification. Internal evaluator-agent decisions are not an independent reported evidence-quality endpoint.

Evidence: [E0046](source_excerpts.md#e0046).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Accuracy, precision, recall, and F1 concern vulnerability classification. Internal evaluator-agent decisions are not an independent reported evidence-quality endpoint.

Evidence: [E0046](source_excerpts.md#e0046).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Accuracy, precision, recall, and F1 concern vulnerability classification. Internal evaluator-agent decisions are not an independent reported evidence-quality endpoint.

Evidence: [E0046](source_excerpts.md#e0046).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Accuracy, precision, recall, and F1 concern vulnerability classification. Internal evaluator-agent decisions are not an independent reported evidence-quality endpoint.

Evidence: [E0046](source_excerpts.md#e0046).


<a id="s05"></a>

## S05: CodeRAG

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

The AUC concerns the initial classifier and the remaining measures concern final detection or sensitivity to retrieval size/thresholds. They do not label the selected external cases for relevance.

Evidence: [E0056](source_excerpts.md#e0056), [E0057](source_excerpts.md#e0057).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

The AUC concerns the initial classifier and the remaining measures concern final detection or sensitivity to retrieval size/thresholds. They do not label the selected external cases for relevance.

Evidence: [E0056](source_excerpts.md#e0056), [E0057](source_excerpts.md#e0057).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

The AUC concerns the initial classifier and the remaining measures concern final detection or sensitivity to retrieval size/thresholds. They do not label the selected external cases for relevance.

Evidence: [E0056](source_excerpts.md#e0056), [E0057](source_excerpts.md#e0057).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

The AUC concerns the initial classifier and the remaining measures concern final detection or sensitivity to retrieval size/thresholds. They do not label the selected external cases for relevance.

Evidence: [E0056](source_excerpts.md#e0056), [E0057](source_excerpts.md#e0057).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. The AUC concerns the initial classifier and the remaining measures concern final detection or sensitivity to retrieval size/thresholds. They do not label the selected external cases for relevance.

Evidence: [E0056](source_excerpts.md#e0056), [E0057](source_excerpts.md#e0057).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. The AUC concerns the initial classifier and the remaining measures concern final detection or sensitivity to retrieval size/thresholds. They do not label the selected external cases for relevance.

Evidence: [E0056](source_excerpts.md#e0056), [E0057](source_excerpts.md#e0057).


<a id="s06"></a>

## S06: MulVul

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Macro detection scores and category-router Recall@k concern vulnerability labels/CWE routes. They do not measure coverage of reference claims by retrieved documents.

Evidence: [E0064](source_excerpts.md#e0064).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Macro detection scores and category-router Recall@k concern vulnerability labels/CWE routes. They do not measure coverage of reference claims by retrieved documents.

Evidence: [E0064](source_excerpts.md#e0064).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Macro detection scores and category-router Recall@k concern vulnerability labels/CWE routes. They do not measure coverage of reference claims by retrieved documents.

Evidence: [E0064](source_excerpts.md#e0064).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Macro detection scores and category-router Recall@k concern vulnerability labels/CWE routes. They do not measure coverage of reference claims by retrieved documents.

Evidence: [E0064](source_excerpts.md#e0064).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Macro detection scores and category-router Recall@k concern vulnerability labels/CWE routes. They do not measure coverage of reference claims by retrieved documents.

Evidence: [E0064](source_excerpts.md#e0064).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Macro detection scores and category-router Recall@k concern vulnerability labels/CWE routes. They do not measure coverage of reference claims by retrieved documents.

Evidence: [E0064](source_excerpts.md#e0064).


<a id="s07"></a>

## S07: HyVD-VP

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Classification results and RAG hyperparameter experiments concern downstream detection. Sandbox confirmation concerns original findings, not generated vulnerability patches.

Evidence: [E0073](source_excerpts.md#e0073).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Classification results and RAG hyperparameter experiments concern downstream detection. Sandbox confirmation concerns original findings, not generated vulnerability patches.

Evidence: [E0073](source_excerpts.md#e0073).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Classification results and RAG hyperparameter experiments concern downstream detection. Sandbox confirmation concerns original findings, not generated vulnerability patches.

Evidence: [E0073](source_excerpts.md#e0073).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Classification results and RAG hyperparameter experiments concern downstream detection. Sandbox confirmation concerns original findings, not generated vulnerability patches.

Evidence: [E0073](source_excerpts.md#e0073).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Classification results and RAG hyperparameter experiments concern downstream detection. Sandbox confirmation concerns original findings, not generated vulnerability patches.

Evidence: [E0073](source_excerpts.md#e0073).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Classification results and RAG hyperparameter experiments concern downstream detection. Sandbox confirmation concerns original findings, not generated vulnerability patches.

Evidence: [E0073](source_excerpts.md#e0073).


<a id="s08"></a>

## S08: KLRAG

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Bug counts, code/API coverage, and valid generated seeds evaluate fuzzing. Repairing a generated test program is not repairing the vulnerable software.

Evidence: [E0086](source_excerpts.md#e0086).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Bug counts, code/API coverage, and valid generated seeds evaluate fuzzing. Repairing a generated test program is not repairing the vulnerable software.

Evidence: [E0086](source_excerpts.md#e0086).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Bug counts, code/API coverage, and valid generated seeds evaluate fuzzing. Repairing a generated test program is not repairing the vulnerable software.

Evidence: [E0086](source_excerpts.md#e0086).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Bug counts, code/API coverage, and valid generated seeds evaluate fuzzing. Repairing a generated test program is not repairing the vulnerable software.

Evidence: [E0086](source_excerpts.md#e0086).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Bug counts, code/API coverage, and valid generated seeds evaluate fuzzing. Repairing a generated test program is not repairing the vulnerable software.

Evidence: [E0086](source_excerpts.md#e0086).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Bug counts, code/API coverage, and valid generated seeds evaluate fuzzing. Repairing a generated test program is not repairing the vulnerable software.

Evidence: [E0086](source_excerpts.md#e0086).


<a id="s09"></a>

## S09: VulRTex

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

The evaluation concerns issue-report identification and CWE prediction. IR denotes issue report. The classification and CWE metrics do not evaluate external-evidence recall.

Evidence: [E0105](source_excerpts.md#e0105).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

The evaluation concerns issue-report identification and CWE prediction. IR denotes issue report. The classification and CWE metrics do not evaluate external-evidence recall.

Evidence: [E0105](source_excerpts.md#e0105).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

The evaluation concerns issue-report identification and CWE prediction. IR denotes issue report. The classification and CWE metrics do not evaluate external-evidence recall.

Evidence: [E0105](source_excerpts.md#e0105).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

The evaluation concerns issue-report identification and CWE prediction. IR denotes issue report. The classification and CWE metrics do not evaluate external-evidence recall.

Evidence: [E0105](source_excerpts.md#e0105).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. The evaluation concerns issue-report identification and CWE prediction. IR denotes issue report. The classification and CWE metrics do not evaluate external-evidence recall.

Evidence: [E0105](source_excerpts.md#e0105).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. The evaluation concerns issue-report identification and CWE prediction. IR denotes issue report. The classification and CWE metrics do not evaluate external-evidence recall.

Evidence: [E0105](source_excerpts.md#e0105).


<a id="s10"></a>

## S10: VoidSight

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Recall evaluates vulnerable target-code screening, and the silhouette coefficient evaluates clustering. Neither directly tests relevance or reference-evidence coverage of selected external context.

Evidence: [E0120](source_excerpts.md#e0120).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Recall evaluates vulnerable target-code screening, and the silhouette coefficient evaluates clustering. Neither directly tests relevance or reference-evidence coverage of selected external context.

Evidence: [E0120](source_excerpts.md#e0120).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Recall evaluates vulnerable target-code screening, and the silhouette coefficient evaluates clustering. Neither directly tests relevance or reference-evidence coverage of selected external context.

Evidence: [E0120](source_excerpts.md#e0120).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Recall evaluates vulnerable target-code screening, and the silhouette coefficient evaluates clustering. Neither directly tests relevance or reference-evidence coverage of selected external context.

Evidence: [E0120](source_excerpts.md#e0120).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Recall evaluates vulnerable target-code screening, and the silhouette coefficient evaluates clustering. Neither directly tests relevance or reference-evidence coverage of selected external context.

Evidence: [E0120](source_excerpts.md#e0120).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Recall evaluates vulnerable target-code screening, and the silhouette coefficient evaluates clustering. Neither directly tests relevance or reference-evidence coverage of selected external context.

Evidence: [E0120](source_excerpts.md#e0120).


<a id="s11"></a>

## S11: Argus

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Relevance/credibility/content scores implement retrieval filtering. Reported evaluation concerns sinks, vulnerability findings, and tokens. PoC execution verifies original vulnerabilities. Supporting patches are generated, but no patch-level regression or post-repair security results are reported.

Evidence: [E0129](source_excerpts.md#e0129), [E0130](source_excerpts.md#e0130), [E0131](source_excerpts.md#e0131).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Relevance/credibility/content scores implement retrieval filtering. Reported evaluation concerns sinks, vulnerability findings, and tokens. PoC execution verifies original vulnerabilities. Supporting patches are generated, but no patch-level regression or post-repair security results are reported.

Evidence: [E0129](source_excerpts.md#e0129), [E0130](source_excerpts.md#e0130), [E0131](source_excerpts.md#e0131).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Relevance/credibility/content scores implement retrieval filtering. Reported evaluation concerns sinks, vulnerability findings, and tokens. PoC execution verifies original vulnerabilities. Supporting patches are generated, but no patch-level regression or post-repair security results are reported.

Evidence: [E0129](source_excerpts.md#e0129), [E0130](source_excerpts.md#e0130), [E0131](source_excerpts.md#e0131).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Relevance/credibility/content scores implement retrieval filtering. Reported evaluation concerns sinks, vulnerability findings, and tokens. PoC execution verifies original vulnerabilities. Supporting patches are generated, but no patch-level regression or post-repair security results are reported.

Evidence: [E0129](source_excerpts.md#e0129), [E0130](source_excerpts.md#e0130), [E0131](source_excerpts.md#e0131).

### functional_correctness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Relevance/credibility/content scores implement retrieval filtering. Reported evaluation concerns sinks, vulnerability findings, and tokens. PoC execution verifies original vulnerabilities. Supporting patches are generated, but no patch-level regression or post-repair security results are reported.

Evidence: [E0129](source_excerpts.md#e0129), [E0130](source_excerpts.md#e0130), [E0131](source_excerpts.md#e0131).

### post_repair_security

Status: `not_reported`. Reported assessment: False. Applicable: True.

Relevance/credibility/content scores implement retrieval filtering. Reported evaluation concerns sinks, vulnerability findings, and tokens. PoC execution verifies original vulnerabilities. Supporting patches are generated, but no patch-level regression or post-repair security results are reported.

Evidence: [E0129](source_excerpts.md#e0129), [E0130](source_excerpts.md#e0130), [E0131](source_excerpts.md#e0131).


<a id="s12"></a>

## S12: RLV

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Detection is assessed quantitatively, and programmers judge function summaries holistically for accurate purpose/functionality. This does not check individual generated claims against retrieved evidence.

Evidence: [E0137](source_excerpts.md#e0137), [E0138](source_excerpts.md#e0138).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Detection is assessed quantitatively, and programmers judge function summaries holistically for accurate purpose/functionality. This does not check individual generated claims against retrieved evidence.

Evidence: [E0137](source_excerpts.md#e0137), [E0138](source_excerpts.md#e0138).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Detection is assessed quantitatively, and programmers judge function summaries holistically for accurate purpose/functionality. This does not check individual generated claims against retrieved evidence.

Evidence: [E0137](source_excerpts.md#e0137), [E0138](source_excerpts.md#e0138).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Detection is assessed quantitatively, and programmers judge function summaries holistically for accurate purpose/functionality. This does not check individual generated claims against retrieved evidence.

Evidence: [E0137](source_excerpts.md#e0137), [E0138](source_excerpts.md#e0138).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Detection is assessed quantitatively, and programmers judge function summaries holistically for accurate purpose/functionality. This does not check individual generated claims against retrieved evidence.

Evidence: [E0137](source_excerpts.md#e0137), [E0138](source_excerpts.md#e0138).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Detection is assessed quantitatively, and programmers judge function summaries holistically for accurate purpose/functionality. This does not check individual generated claims against retrieved evidence.

Evidence: [E0137](source_excerpts.md#e0137), [E0138](source_excerpts.md#e0138).


<a id="s13"></a>

## S13: DeepDesc

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Detection and BLEU-based description quality are reported. Statement alignment and line-level precision/recall are proposed future evaluations, not reported grounding results.

Evidence: [E0147](source_excerpts.md#e0147), [E0148](source_excerpts.md#e0148), [E0149](source_excerpts.md#e0149).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Detection and BLEU-based description quality are reported. Statement alignment and line-level precision/recall are proposed future evaluations, not reported grounding results.

Evidence: [E0147](source_excerpts.md#e0147), [E0148](source_excerpts.md#e0148), [E0149](source_excerpts.md#e0149).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Detection and BLEU-based description quality are reported. Statement alignment and line-level precision/recall are proposed future evaluations, not reported grounding results.

Evidence: [E0147](source_excerpts.md#e0147), [E0148](source_excerpts.md#e0148), [E0149](source_excerpts.md#e0149).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Detection and BLEU-based description quality are reported. Statement alignment and line-level precision/recall are proposed future evaluations, not reported grounding results.

Evidence: [E0147](source_excerpts.md#e0147), [E0148](source_excerpts.md#e0148), [E0149](source_excerpts.md#e0149).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Detection and BLEU-based description quality are reported. Statement alignment and line-level precision/recall are proposed future evaluations, not reported grounding results.

Evidence: [E0147](source_excerpts.md#e0147), [E0148](source_excerpts.md#e0148), [E0149](source_excerpts.md#e0149).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Detection and BLEU-based description quality are reported. Statement alignment and line-level precision/recall are proposed future evaluations, not reported grounding results.

Evidence: [E0147](source_excerpts.md#e0147), [E0148](source_excerpts.md#e0148), [E0149](source_excerpts.md#e0149).


<a id="s14"></a>

## S14: RAG-SmartVuln

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

A GPT-4o rubric scores generated descriptions and fix guidance overall. Mythril validates historical repairs while constructing the knowledge base. No target-software Patch output is coded for this study.

Evidence: [E0160](source_excerpts.md#e0160), [E0161](source_excerpts.md#e0161), [E0162](source_excerpts.md#e0162).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

A GPT-4o rubric scores generated descriptions and fix guidance overall. Mythril validates historical repairs while constructing the knowledge base. No target-software Patch output is coded for this study.

Evidence: [E0160](source_excerpts.md#e0160), [E0161](source_excerpts.md#e0161), [E0162](source_excerpts.md#e0162).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

A GPT-4o rubric scores generated descriptions and fix guidance overall. Mythril validates historical repairs while constructing the knowledge base. No target-software Patch output is coded for this study.

Evidence: [E0160](source_excerpts.md#e0160), [E0161](source_excerpts.md#e0161), [E0162](source_excerpts.md#e0162).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

A GPT-4o rubric scores generated descriptions and fix guidance overall. Mythril validates historical repairs while constructing the knowledge base. No target-software Patch output is coded for this study.

Evidence: [E0160](source_excerpts.md#e0160), [E0161](source_excerpts.md#e0161), [E0162](source_excerpts.md#e0162).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. A GPT-4o rubric scores generated descriptions and fix guidance overall. Mythril validates historical repairs while constructing the knowledge base. No target-software Patch output is coded for this study.

Evidence: [E0160](source_excerpts.md#e0160), [E0161](source_excerpts.md#e0161), [E0162](source_excerpts.md#e0162).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. A GPT-4o rubric scores generated descriptions and fix guidance overall. Mythril validates historical repairs while constructing the knowledge base. No target-software Patch output is coded for this study.

Evidence: [E0160](source_excerpts.md#e0160), [E0161](source_excerpts.md#e0161), [E0162](source_excerpts.md#e0162).


<a id="s15"></a>

## S15: ParaVul

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Branch comparisons measure vulnerability classification. Traceability is described as a stored report attribute without reported source-attribution accuracy. CoT reports are not scored for individual claim support.

Evidence: [E0177](source_excerpts.md#e0177), [E0178](source_excerpts.md#e0178).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Branch comparisons measure vulnerability classification. Traceability is described as a stored report attribute without reported source-attribution accuracy. CoT reports are not scored for individual claim support.

Evidence: [E0177](source_excerpts.md#e0177), [E0178](source_excerpts.md#e0178).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Branch comparisons measure vulnerability classification. Traceability is described as a stored report attribute without reported source-attribution accuracy. CoT reports are not scored for individual claim support.

Evidence: [E0177](source_excerpts.md#e0177), [E0178](source_excerpts.md#e0178).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Branch comparisons measure vulnerability classification. Traceability is described as a stored report attribute without reported source-attribution accuracy. CoT reports are not scored for individual claim support.

Evidence: [E0177](source_excerpts.md#e0177), [E0178](source_excerpts.md#e0178).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Branch comparisons measure vulnerability classification. Traceability is described as a stored report attribute without reported source-attribution accuracy. CoT reports are not scored for individual claim support.

Evidence: [E0177](source_excerpts.md#e0177), [E0178](source_excerpts.md#e0178).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Branch comparisons measure vulnerability classification. Traceability is described as a stored report attribute without reported source-attribution accuracy. CoT reports are not scored for individual claim support.

Evidence: [E0177](source_excerpts.md#e0177), [E0178](source_excerpts.md#e0178).


<a id="s16"></a>

## S16: TaK-Fuzz

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Branch coverage, vulnerability recall, and test-case count concern fuzzing and original contract vulnerabilities, not retrieved-context recall or target-software repair.

Evidence: [E0187](source_excerpts.md#e0187), [E0188](source_excerpts.md#e0188).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Branch coverage, vulnerability recall, and test-case count concern fuzzing and original contract vulnerabilities, not retrieved-context recall or target-software repair.

Evidence: [E0187](source_excerpts.md#e0187), [E0188](source_excerpts.md#e0188).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Branch coverage, vulnerability recall, and test-case count concern fuzzing and original contract vulnerabilities, not retrieved-context recall or target-software repair.

Evidence: [E0187](source_excerpts.md#e0187), [E0188](source_excerpts.md#e0188).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Branch coverage, vulnerability recall, and test-case count concern fuzzing and original contract vulnerabilities, not retrieved-context recall or target-software repair.

Evidence: [E0187](source_excerpts.md#e0187), [E0188](source_excerpts.md#e0188).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Branch coverage, vulnerability recall, and test-case count concern fuzzing and original contract vulnerabilities, not retrieved-context recall or target-software repair.

Evidence: [E0187](source_excerpts.md#e0187), [E0188](source_excerpts.md#e0188).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Branch coverage, vulnerability recall, and test-case count concern fuzzing and original contract vulnerabilities, not retrieved-context recall or target-software repair.

Evidence: [E0187](source_excerpts.md#e0187), [E0188](source_excerpts.md#e0188).


<a id="s17"></a>

## S17: UniFuzz

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Code/branch coverage and detection accuracy concern fuzzing. Expert confirmation concerns detected original vulnerabilities, not a patch-security endpoint.

Evidence: [E0195](source_excerpts.md#e0195), [E0196](source_excerpts.md#e0196).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Code/branch coverage and detection accuracy concern fuzzing. Expert confirmation concerns detected original vulnerabilities, not a patch-security endpoint.

Evidence: [E0195](source_excerpts.md#e0195), [E0196](source_excerpts.md#e0196).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Code/branch coverage and detection accuracy concern fuzzing. Expert confirmation concerns detected original vulnerabilities, not a patch-security endpoint.

Evidence: [E0195](source_excerpts.md#e0195), [E0196](source_excerpts.md#e0196).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Code/branch coverage and detection accuracy concern fuzzing. Expert confirmation concerns detected original vulnerabilities, not a patch-security endpoint.

Evidence: [E0195](source_excerpts.md#e0195), [E0196](source_excerpts.md#e0196).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Code/branch coverage and detection accuracy concern fuzzing. Expert confirmation concerns detected original vulnerabilities, not a patch-security endpoint.

Evidence: [E0195](source_excerpts.md#e0195), [E0196](source_excerpts.md#e0196).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Code/branch coverage and detection accuracy concern fuzzing. Expert confirmation concerns detected original vulnerabilities, not a patch-security endpoint.

Evidence: [E0195](source_excerpts.md#e0195), [E0196](source_excerpts.md#e0196).


<a id="s18"></a>

## S18: DSS

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Accuracy, recall, precision, and F1 evaluate classification, including comparisons of retrieval algorithms. Retriever comparisons through final detection scores are component-effect tests, not direct retrieval relevance.

Evidence: [E0208](source_excerpts.md#e0208), [E0209](source_excerpts.md#e0209).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Accuracy, recall, precision, and F1 evaluate classification, including comparisons of retrieval algorithms. Retriever comparisons through final detection scores are component-effect tests, not direct retrieval relevance.

Evidence: [E0208](source_excerpts.md#e0208), [E0209](source_excerpts.md#e0209).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Accuracy, recall, precision, and F1 evaluate classification, including comparisons of retrieval algorithms. Retriever comparisons through final detection scores are component-effect tests, not direct retrieval relevance.

Evidence: [E0208](source_excerpts.md#e0208), [E0209](source_excerpts.md#e0209).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Accuracy, recall, precision, and F1 evaluate classification, including comparisons of retrieval algorithms. Retriever comparisons through final detection scores are component-effect tests, not direct retrieval relevance.

Evidence: [E0208](source_excerpts.md#e0208), [E0209](source_excerpts.md#e0209).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Accuracy, recall, precision, and F1 evaluate classification, including comparisons of retrieval algorithms. Retriever comparisons through final detection scores are component-effect tests, not direct retrieval relevance.

Evidence: [E0208](source_excerpts.md#e0208), [E0209](source_excerpts.md#e0209).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Accuracy, recall, precision, and F1 evaluate classification, including comparisons of retrieval algorithms. Retriever comparisons through final detection scores are component-effect tests, not direct retrieval relevance.

Evidence: [E0208](source_excerpts.md#e0208), [E0209](source_excerpts.md#e0209).


<a id="s19"></a>

## S19: ORACAL

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

MSP/MSR/MIoU compare important graph nodes/source-code lines with vulnerability-triggering paths. Statements are code statements, not atomic generated prose claims. Faithfulness of RAG-generated semantic descriptions is explicitly a future-work item.

Evidence: [E0227](source_excerpts.md#e0227), [E0228](source_excerpts.md#e0228), [E0229](source_excerpts.md#e0229).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

MSP/MSR/MIoU compare important graph nodes/source-code lines with vulnerability-triggering paths. Statements are code statements, not atomic generated prose claims. Faithfulness of RAG-generated semantic descriptions is explicitly a future-work item.

Evidence: [E0227](source_excerpts.md#e0227), [E0228](source_excerpts.md#e0228), [E0229](source_excerpts.md#e0229).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

MSP/MSR/MIoU compare important graph nodes/source-code lines with vulnerability-triggering paths. Statements are code statements, not atomic generated prose claims. Faithfulness of RAG-generated semantic descriptions is explicitly a future-work item.

Evidence: [E0227](source_excerpts.md#e0227), [E0228](source_excerpts.md#e0228), [E0229](source_excerpts.md#e0229).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

MSP/MSR/MIoU compare important graph nodes/source-code lines with vulnerability-triggering paths. Statements are code statements, not atomic generated prose claims. Faithfulness of RAG-generated semantic descriptions is explicitly a future-work item.

Evidence: [E0227](source_excerpts.md#e0227), [E0228](source_excerpts.md#e0228), [E0229](source_excerpts.md#e0229).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. MSP/MSR/MIoU compare important graph nodes/source-code lines with vulnerability-triggering paths. Statements are code statements, not atomic generated prose claims. Faithfulness of RAG-generated semantic descriptions is explicitly a future-work item.

Evidence: [E0227](source_excerpts.md#e0227), [E0228](source_excerpts.md#e0228), [E0229](source_excerpts.md#e0229).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. MSP/MSR/MIoU compare important graph nodes/source-code lines with vulnerability-triggering paths. Statements are code statements, not atomic generated prose claims. Faithfulness of RAG-generated semantic descriptions is explicitly a future-work item.

Evidence: [E0227](source_excerpts.md#e0227), [E0228](source_excerpts.md#e0228), [E0229](source_excerpts.md#e0229).


<a id="s25"></a>

## S25: SmartAuditFlow

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Top-N, MRR, MAP, and conventional scores rank or classify final vulnerability findings. The LLM audit evaluator compares findings to vulnerability ground truth, not retrieved documents to relevance labels.

Evidence: [E0238](source_excerpts.md#e0238), [E0239](source_excerpts.md#e0239), [E0240](source_excerpts.md#e0240).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Top-N, MRR, MAP, and conventional scores rank or classify final vulnerability findings. The LLM audit evaluator compares findings to vulnerability ground truth, not retrieved documents to relevance labels.

Evidence: [E0238](source_excerpts.md#e0238), [E0239](source_excerpts.md#e0239), [E0240](source_excerpts.md#e0240).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Top-N, MRR, MAP, and conventional scores rank or classify final vulnerability findings. The LLM audit evaluator compares findings to vulnerability ground truth, not retrieved documents to relevance labels.

Evidence: [E0238](source_excerpts.md#e0238), [E0239](source_excerpts.md#e0239), [E0240](source_excerpts.md#e0240).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Top-N, MRR, MAP, and conventional scores rank or classify final vulnerability findings. The LLM audit evaluator compares findings to vulnerability ground truth, not retrieved documents to relevance labels.

Evidence: [E0238](source_excerpts.md#e0238), [E0239](source_excerpts.md#e0239), [E0240](source_excerpts.md#e0240).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Top-N, MRR, MAP, and conventional scores rank or classify final vulnerability findings. The LLM audit evaluator compares findings to vulnerability ground truth, not retrieved documents to relevance labels.

Evidence: [E0238](source_excerpts.md#e0238), [E0239](source_excerpts.md#e0239), [E0240](source_excerpts.md#e0240).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Top-N, MRR, MAP, and conventional scores rank or classify final vulnerability findings. The LLM audit evaluator compares findings to vulnerability ground truth, not retrieved documents to relevance labels.

Evidence: [E0238](source_excerpts.md#e0238), [E0239](source_excerpts.md#e0239), [E0240](source_excerpts.md#e0240).


<a id="s20"></a>

## S20: ReVul-CoT

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Severity Accuracy/Macro-F1/MCC and modality/retrieval/CoT ablations evaluate severity prediction. No separate evidence-relevance or claim-support endpoint is reported.

Evidence: [E0261](source_excerpts.md#e0261), [E0262](source_excerpts.md#e0262).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Severity Accuracy/Macro-F1/MCC and modality/retrieval/CoT ablations evaluate severity prediction. No separate evidence-relevance or claim-support endpoint is reported.

Evidence: [E0261](source_excerpts.md#e0261), [E0262](source_excerpts.md#e0262).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Severity Accuracy/Macro-F1/MCC and modality/retrieval/CoT ablations evaluate severity prediction. No separate evidence-relevance or claim-support endpoint is reported.

Evidence: [E0261](source_excerpts.md#e0261), [E0262](source_excerpts.md#e0262).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Severity Accuracy/Macro-F1/MCC and modality/retrieval/CoT ablations evaluate severity prediction. No separate evidence-relevance or claim-support endpoint is reported.

Evidence: [E0261](source_excerpts.md#e0261), [E0262](source_excerpts.md#e0262).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Severity Accuracy/Macro-F1/MCC and modality/retrieval/CoT ablations evaluate severity prediction. No separate evidence-relevance or claim-support endpoint is reported.

Evidence: [E0261](source_excerpts.md#e0261), [E0262](source_excerpts.md#e0262).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Severity Accuracy/Macro-F1/MCC and modality/retrieval/CoT ablations evaluate severity prediction. No separate evidence-relevance or claim-support endpoint is reported.

Evidence: [E0261](source_excerpts.md#e0261), [E0262](source_excerpts.md#e0262).


<a id="s21"></a>

## S21: ChatNVD

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Accuracy, hallucination, omission, and failure are scored against NVD answer fields. These are answer-level correctness measures, without a separate retrieved-context recall, explicit source-attribution score, or claim-by-claim entailment protocol.

Evidence: [E0272](source_excerpts.md#e0272), [E0273](source_excerpts.md#e0273), [E0274](source_excerpts.md#e0274).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Accuracy, hallucination, omission, and failure are scored against NVD answer fields. These are answer-level correctness measures, without a separate retrieved-context recall, explicit source-attribution score, or claim-by-claim entailment protocol.

Evidence: [E0272](source_excerpts.md#e0272), [E0273](source_excerpts.md#e0273), [E0274](source_excerpts.md#e0274).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Accuracy, hallucination, omission, and failure are scored against NVD answer fields. These are answer-level correctness measures, without a separate retrieved-context recall, explicit source-attribution score, or claim-by-claim entailment protocol.

Evidence: [E0272](source_excerpts.md#e0272), [E0273](source_excerpts.md#e0273), [E0274](source_excerpts.md#e0274).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Accuracy, hallucination, omission, and failure are scored against NVD answer fields. These are answer-level correctness measures, without a separate retrieved-context recall, explicit source-attribution score, or claim-by-claim entailment protocol.

Evidence: [E0272](source_excerpts.md#e0272), [E0273](source_excerpts.md#e0273), [E0274](source_excerpts.md#e0274).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Accuracy, hallucination, omission, and failure are scored against NVD answer fields. These are answer-level correctness measures, without a separate retrieved-context recall, explicit source-attribution score, or claim-by-claim entailment protocol.

Evidence: [E0272](source_excerpts.md#e0272), [E0273](source_excerpts.md#e0273), [E0274](source_excerpts.md#e0274).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Accuracy, hallucination, omission, and failure are scored against NVD answer fields. These are answer-level correctness measures, without a separate retrieved-context recall, explicit source-attribution score, or claim-by-claim entailment protocol.

Evidence: [E0272](source_excerpts.md#e0272), [E0273](source_excerpts.md#e0273), [E0274](source_excerpts.md#e0274).


<a id="s22"></a>

## S22: ProveRAG

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Self-critique supplies TP/FP/FN values with rationale and provenance. Provenance quality uses response-to-evidence ROUGE-L/cosine. FN labels are answer/response diagnoses and do not compute coverage of reference claims in retrieved context.

Evidence: [E0303](source_excerpts.md#e0303), [E0304](source_excerpts.md#e0304), [E0305](source_excerpts.md#e0305).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Self-critique supplies TP/FP/FN values with rationale and provenance. Provenance quality uses response-to-evidence ROUGE-L/cosine. FN labels are answer/response diagnoses and do not compute coverage of reference claims in retrieved context.

Evidence: [E0303](source_excerpts.md#e0303), [E0304](source_excerpts.md#e0304), [E0305](source_excerpts.md#e0305).

### provenance

Status: `similarity_proxy`. Reported assessment: True. Applicable: True.

Reported ROUGE-L and embedding cosine compare generated responses with provenance evidence, alongside LLM self-critique. This evaluates response/evidence alignment by proxy, not independently annotated claim-level source entailment.

Evidence: [E0303](source_excerpts.md#e0303), [E0305](source_excerpts.md#e0305).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Self-critique supplies TP/FP/FN values with rationale and provenance. Provenance quality uses response-to-evidence ROUGE-L/cosine. FN labels are answer/response diagnoses and do not compute coverage of reference claims in retrieved context.

Evidence: [E0303](source_excerpts.md#e0303), [E0304](source_excerpts.md#e0304), [E0305](source_excerpts.md#e0305).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Self-critique supplies TP/FP/FN values with rationale and provenance. Provenance quality uses response-to-evidence ROUGE-L/cosine. FN labels are answer/response diagnoses and do not compute coverage of reference claims in retrieved context.

Evidence: [E0303](source_excerpts.md#e0303), [E0304](source_excerpts.md#e0304), [E0305](source_excerpts.md#e0305).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Self-critique supplies TP/FP/FN values with rationale and provenance. Provenance quality uses response-to-evidence ROUGE-L/cosine. FN labels are answer/response diagnoses and do not compute coverage of reference claims in retrieved context.

Evidence: [E0303](source_excerpts.md#e0303), [E0304](source_excerpts.md#e0304), [E0305](source_excerpts.md#e0305).


<a id="s23"></a>

## S23: VDM-IOG

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Precision/recall/F1 evaluate ATT&CK mapping and named entities. Non-existent technique IDs and graph constraints address output validity, not explicit claim-to-source attribution or retrieval-context recall.

Evidence: [E0314](source_excerpts.md#e0314), [E0315](source_excerpts.md#e0315), [E0316](source_excerpts.md#e0316).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Precision/recall/F1 evaluate ATT&CK mapping and named entities. Non-existent technique IDs and graph constraints address output validity, not explicit claim-to-source attribution or retrieval-context recall.

Evidence: [E0314](source_excerpts.md#e0314), [E0315](source_excerpts.md#e0315), [E0316](source_excerpts.md#e0316).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Precision/recall/F1 evaluate ATT&CK mapping and named entities. Non-existent technique IDs and graph constraints address output validity, not explicit claim-to-source attribution or retrieval-context recall.

Evidence: [E0314](source_excerpts.md#e0314), [E0315](source_excerpts.md#e0315), [E0316](source_excerpts.md#e0316).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Precision/recall/F1 evaluate ATT&CK mapping and named entities. Non-existent technique IDs and graph constraints address output validity, not explicit claim-to-source attribution or retrieval-context recall.

Evidence: [E0314](source_excerpts.md#e0314), [E0315](source_excerpts.md#e0315), [E0316](source_excerpts.md#e0316).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Precision/recall/F1 evaluate ATT&CK mapping and named entities. Non-existent technique IDs and graph constraints address output validity, not explicit claim-to-source attribution or retrieval-context recall.

Evidence: [E0314](source_excerpts.md#e0314), [E0315](source_excerpts.md#e0315), [E0316](source_excerpts.md#e0316).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Precision/recall/F1 evaluate ATT&CK mapping and named entities. Non-existent technique IDs and graph constraints address output validity, not explicit claim-to-source attribution or retrieval-context recall.

Evidence: [E0314](source_excerpts.md#e0314), [E0315](source_excerpts.md#e0315), [E0316](source_excerpts.md#e0316).


<a id="s24"></a>

## S24: CRVA-TGRAG

### retrieval_relevance

Status: `context_precision`. Reported assessment: True. Applicable: True.

Context precision ranks relevant retrieved chunks and is reported for RAG configurations.

Evidence: [E0338](source_excerpts.md#e0338), [E0339](source_excerpts.md#e0339).

### context_recall

Status: `reference_claim_coverage`. Reported assessment: True. Applicable: True.

The fraction of reference-answer claims supported by the retrieved context is defined and reported.

Evidence: [E0340](source_excerpts.md#e0340), [E0339](source_excerpts.md#e0339).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

RAG-specific context precision, reference-claim context recall, and generated-claim faithfulness are explicitly defined and reported in Table 1. Claim support is evaluated against the supplied context, without a separate citation/source-attribution endpoint.

Evidence: [E0341](source_excerpts.md#e0341), [E0342](source_excerpts.md#e0342), [E0339](source_excerpts.md#e0339).

### claim_faithfulness

Status: `claim_context_support`. Reported assessment: True. Applicable: True.

The fraction of generated answer claims inferable from the given context is defined and reported.

Evidence: [E0343](source_excerpts.md#e0343), [E0339](source_excerpts.md#e0339).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. RAG-specific context precision, reference-claim context recall, and generated-claim faithfulness are explicitly defined and reported in Table 1. Claim support is evaluated against the supplied context, without a separate citation/source-attribution endpoint.

Evidence: [E0341](source_excerpts.md#e0341), [E0342](source_excerpts.md#e0342), [E0339](source_excerpts.md#e0339).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. RAG-specific context precision, reference-claim context recall, and generated-claim faithfulness are explicitly defined and reported in Table 1. Claim support is evaluated against the supplied context, without a separate citation/source-attribution endpoint.

Evidence: [E0341](source_excerpts.md#e0341), [E0342](source_excerpts.md#e0342), [E0339](source_excerpts.md#e0339).


<a id="s26"></a>

## S26: RAR

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Execution and human assistance validate reproduced exploits. Corrections concern environments or exploit scripts, not patched vulnerable software, and therefore do not enter patch-level functional/security denominators.

Evidence: [E0354](source_excerpts.md#e0354), [E0355](source_excerpts.md#e0355).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Execution and human assistance validate reproduced exploits. Corrections concern environments or exploit scripts, not patched vulnerable software, and therefore do not enter patch-level functional/security denominators.

Evidence: [E0354](source_excerpts.md#e0354), [E0355](source_excerpts.md#e0355).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Execution and human assistance validate reproduced exploits. Corrections concern environments or exploit scripts, not patched vulnerable software, and therefore do not enter patch-level functional/security denominators.

Evidence: [E0354](source_excerpts.md#e0354), [E0355](source_excerpts.md#e0355).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Execution and human assistance validate reproduced exploits. Corrections concern environments or exploit scripts, not patched vulnerable software, and therefore do not enter patch-level functional/security denominators.

Evidence: [E0354](source_excerpts.md#e0354), [E0355](source_excerpts.md#e0355).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Execution and human assistance validate reproduced exploits. Corrections concern environments or exploit scripts, not patched vulnerable software, and therefore do not enter patch-level functional/security denominators.

Evidence: [E0354](source_excerpts.md#e0354), [E0355](source_excerpts.md#e0355).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Execution and human assistance validate reproduced exploits. Corrections concern environments or exploit scripts, not patched vulnerable software, and therefore do not enter patch-level functional/security denominators.

Evidence: [E0354](source_excerpts.md#e0354), [E0355](source_excerpts.md#e0355).


<a id="s31"></a>

## S31: VulLibGen

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Precision@k/Recall@k/F1@k evaluate generated affected-package names. They do not score the relevance or coverage of retrieved documentation.

Evidence: [E0364](source_excerpts.md#e0364), [E0365](source_excerpts.md#e0365).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Precision@k/Recall@k/F1@k evaluate generated affected-package names. They do not score the relevance or coverage of retrieved documentation.

Evidence: [E0364](source_excerpts.md#e0364), [E0365](source_excerpts.md#e0365).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Precision@k/Recall@k/F1@k evaluate generated affected-package names. They do not score the relevance or coverage of retrieved documentation.

Evidence: [E0364](source_excerpts.md#e0364), [E0365](source_excerpts.md#e0365).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Precision@k/Recall@k/F1@k evaluate generated affected-package names. They do not score the relevance or coverage of retrieved documentation.

Evidence: [E0364](source_excerpts.md#e0364), [E0365](source_excerpts.md#e0365).

### functional_correctness

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Precision@k/Recall@k/F1@k evaluate generated affected-package names. They do not score the relevance or coverage of retrieved documentation.

Evidence: [E0364](source_excerpts.md#e0364), [E0365](source_excerpts.md#e0365).

### post_repair_security

Status: `not_applicable`. Reported assessment: False. Applicable: False.

No target-software Patch output. Precision@k/Recall@k/F1@k evaluate generated affected-package names. They do not score the relevance or coverage of retrieved documentation.

Evidence: [E0364](source_excerpts.md#e0364), [E0365](source_excerpts.md#e0365).


<a id="s27"></a>

## S27: MR-LLM

### retrieval_relevance

Status: `human_sample`. Reported assessment: True. Applicable: True.

Manual inspection of 900 sampled items reports accurate/inaccurate retrieval together with relevance/actionability of generated repairs. This is a joint sampled diagnostic rather than a standalone ranked-retrieval benchmark.

Evidence: [E0384](source_excerpts.md#e0384).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Sampled manual inspection jointly categorizes retrieval accuracy and repair relevance. Completeness/correctness are holistic recommendation rubrics, not reference-claim context recall or claim-level entailment. Snyk evaluates repairs, while the paper explicitly states that executable functional tests are infeasible in its snippet setting.

Evidence: [E0385](source_excerpts.md#e0385), [E0386](source_excerpts.md#e0386), [E0387](source_excerpts.md#e0387), [E0388](source_excerpts.md#e0388).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Sampled manual inspection jointly categorizes retrieval accuracy and repair relevance. Completeness/correctness are holistic recommendation rubrics, not reference-claim context recall or claim-level entailment. Snyk evaluates repairs, while the paper explicitly states that executable functional tests are infeasible in its snippet setting.

Evidence: [E0385](source_excerpts.md#e0385), [E0386](source_excerpts.md#e0386), [E0387](source_excerpts.md#e0387), [E0388](source_excerpts.md#e0388).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Sampled manual inspection jointly categorizes retrieval accuracy and repair relevance. Completeness/correctness are holistic recommendation rubrics, not reference-claim context recall or claim-level entailment. Snyk evaluates repairs, while the paper explicitly states that executable functional tests are infeasible in its snippet setting.

Evidence: [E0385](source_excerpts.md#e0385), [E0386](source_excerpts.md#e0386), [E0387](source_excerpts.md#e0387), [E0388](source_excerpts.md#e0388).

### functional_correctness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Sampled manual inspection jointly categorizes retrieval accuracy and repair relevance. Completeness/correctness are holistic recommendation rubrics, not reference-claim context recall or claim-level entailment. Snyk evaluates repairs, while the paper explicitly states that executable functional tests are infeasible in its snippet setting.

Evidence: [E0385](source_excerpts.md#e0385), [E0386](source_excerpts.md#e0386), [E0387](source_excerpts.md#e0387), [E0388](source_excerpts.md#e0388).

### post_repair_security

Status: `static_analysis`. Reported assessment: True. Applicable: True.

Snyk scans vulnerable and generated repaired snippets. Table 2 reports fixed-file and resolved-issue counts.

Evidence: [E0389](source_excerpts.md#e0389), [E0390](source_excerpts.md#e0390).


<a id="s28"></a>

## S28: SCPatcher

### retrieval_relevance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Compilation and Slither-based repair rates are reported. The paper states that repair means static mitigation and does not guarantee behavioral/function correctness. Dynamic execution/test cases are future work.

Evidence: [E0401](source_excerpts.md#e0401), [E0402](source_excerpts.md#e0402), [E0403](source_excerpts.md#e0403).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Compilation and Slither-based repair rates are reported. The paper states that repair means static mitigation and does not guarantee behavioral/function correctness. Dynamic execution/test cases are future work.

Evidence: [E0401](source_excerpts.md#e0401), [E0402](source_excerpts.md#e0402), [E0403](source_excerpts.md#e0403).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Compilation and Slither-based repair rates are reported. The paper states that repair means static mitigation and does not guarantee behavioral/function correctness. Dynamic execution/test cases are future work.

Evidence: [E0401](source_excerpts.md#e0401), [E0402](source_excerpts.md#e0402), [E0403](source_excerpts.md#e0403).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Compilation and Slither-based repair rates are reported. The paper states that repair means static mitigation and does not guarantee behavioral/function correctness. Dynamic execution/test cases are future work.

Evidence: [E0401](source_excerpts.md#e0401), [E0402](source_excerpts.md#e0402), [E0403](source_excerpts.md#e0403).

### functional_correctness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Compilation and Slither-based repair rates are reported. The paper states that repair means static mitigation and does not guarantee behavioral/function correctness. Dynamic execution/test cases are future work.

Evidence: [E0401](source_excerpts.md#e0401), [E0402](source_excerpts.md#e0402), [E0403](source_excerpts.md#e0403).

### post_repair_security

Status: `static_analysis`. Reported assessment: True. Applicable: True.

Slither validates generated repairs, reported as effective and overall repair rates. This is detector-specific static checking.

Evidence: [E0401](source_excerpts.md#e0401), [E0402](source_excerpts.md#e0402), [E0403](source_excerpts.md#e0403).


<a id="s29"></a>

## S29: PailGen

### retrieval_relevance

Status: `human_sample`. Reported assessment: True. Applicable: True.

Two security experts judge code-context relevance and vulnerability-feature matching for 30 stratified samples, and retrieval failure rates are reported. Encoder cosine is an additional similarity proxy. Noisy retrieval is also tested through downstream patch outcomes.

Evidence: [E0414](source_excerpts.md#e0414), [E0415](source_excerpts.md#e0415).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Reports both retriever-encoder cosine proxies and expert-rated relevance/failure on a sample. CWEVAL-BENCH reports executable functional and combined functional/security patch tests. k in func@k is the generated candidate count.

Evidence: [E0414](source_excerpts.md#e0414), [E0415](source_excerpts.md#e0415), [E0416](source_excerpts.md#e0416).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Reports both retriever-encoder cosine proxies and expert-rated relevance/failure on a sample. CWEVAL-BENCH reports executable functional and combined functional/security patch tests. k in func@k is the generated candidate count.

Evidence: [E0414](source_excerpts.md#e0414), [E0415](source_excerpts.md#e0415), [E0416](source_excerpts.md#e0416).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Reports both retriever-encoder cosine proxies and expert-rated relevance/failure on a sample. CWEVAL-BENCH reports executable functional and combined functional/security patch tests. k in func@k is the generated candidate count.

Evidence: [E0414](source_excerpts.md#e0414), [E0415](source_excerpts.md#e0415), [E0416](source_excerpts.md#e0416).

### functional_correctness

Status: `execution_tests`. Reported assessment: True. Applicable: True.

CWEVAL-BENCH func@k reports candidates passing every functionality test.

Evidence: [E0417](source_excerpts.md#e0417), [E0418](source_excerpts.md#e0418).

### post_repair_security

Status: `execution_tests`. Reported assessment: True. Applicable: True.

CWEVAL-BENCH func-sec@k reports candidates passing both functional and security test suites.

Evidence: [E0417](source_excerpts.md#e0417), [E0418](source_excerpts.md#e0418).


<a id="s30"></a>

## S30: AutoPatch

### retrieval_relevance

Status: `gold_cve_match`. Reported assessment: True. Applicable: True.

Manually annotated CVE matches train and test the unified model. Reported held-out matching accuracy evaluates code-to-CVE selection, not general chunk relevance.

Evidence: [E0430](source_excerpts.md#e0430).

### context_recall

Status: `not_reported`. Reported assessment: False. Applicable: True.

Gold CVE matching accuracy evaluates the matching component. Patch feedback uses the LLM Vulnerability Verifier and reports patch accuracy and loop statistics. Independent execution/regression/security-test results for generated patches are not specified.

Evidence: [E0431](source_excerpts.md#e0431), [E0430](source_excerpts.md#e0430), [E0432](source_excerpts.md#e0432), [E0433](source_excerpts.md#e0433).

### provenance

Status: `not_reported`. Reported assessment: False. Applicable: True.

Gold CVE matching accuracy evaluates the matching component. Patch feedback uses the LLM Vulnerability Verifier and reports patch accuracy and loop statistics. Independent execution/regression/security-test results for generated patches are not specified.

Evidence: [E0431](source_excerpts.md#e0431), [E0430](source_excerpts.md#e0430), [E0432](source_excerpts.md#e0432), [E0433](source_excerpts.md#e0433).

### claim_faithfulness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Gold CVE matching accuracy evaluates the matching component. Patch feedback uses the LLM Vulnerability Verifier and reports patch accuracy and loop statistics. Independent execution/regression/security-test results for generated patches are not specified.

Evidence: [E0431](source_excerpts.md#e0431), [E0430](source_excerpts.md#e0430), [E0432](source_excerpts.md#e0432), [E0433](source_excerpts.md#e0433).

### functional_correctness

Status: `not_reported`. Reported assessment: False. Applicable: True.

Gold CVE matching accuracy evaluates the matching component. Patch feedback uses the LLM Vulnerability Verifier and reports patch accuracy and loop statistics. Independent execution/regression/security-test results for generated patches are not specified.

Evidence: [E0431](source_excerpts.md#e0431), [E0430](source_excerpts.md#e0430), [E0432](source_excerpts.md#e0432), [E0433](source_excerpts.md#e0433).

### post_repair_security

Status: `llm_verifier`. Reported assessment: True. Applicable: True.

The Vulnerability Verifier rechecks generated patches and patch/loop outcomes are reported. This is a model-based security check, with no separately specified independent security-test oracle.

Evidence: [E0431](source_excerpts.md#e0431), [E0433](source_excerpts.md#e0433).
