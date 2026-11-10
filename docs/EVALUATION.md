# Evaluation Harness & Metrics — ClauseLens

> **Document Version:** 0.1.0  
> **Date:** 10 November 2026  

---

## 1. Principles of Honest Evaluation

1. **Document-Level Splits:** Train/Dev/Test splits are strictly divided by document ID, never by chunks or individual pages.
2. **Frozen Test Set:** The evaluation benchmark is frozen prior to prompt optimization or model tuning.
3. **Reproducibility:** A single command (`python eval/run_eval.py`) reproduces the published evaluation metrics.
4. **Bootstrap Confidence Intervals:** For small sample sets (30–60 documents), metrics are reported with 95% bootstrap confidence intervals rather than single point estimates.
5. **Transparent Failure Taxonomy:** Error cases and failure modes are explicitly cataloged rather than hidden behind aggregated averages.

---

## 2. Target Metrics by Pipeline Stage

| Pipeline Stage | Primary Metric | Target Benchmark |
|---|---|---|
| **EasyOCR Multilingual** | Character Error Rate (CER), Word Error Rate (WER) | Scanned Arabic & English degraded contracts |
| **Hybrid Retrieval** | Recall@5, MRR (Mean Reciprocal Rank) | Gold passage contract question set |
| **Field Extraction (10 Fields)** | Exact Match (Normalized), Precision, Recall, F1 | CUAD test split (English) & Synthetic UAE test set (Arabic) |
| **Grounded Q&A** | Grounding Rate (% verified against citations), `not_found` accuracy | Mixed answerable and unanswerable query set |
| **Confidence Calibration** | Expected Calibration Error (ECE), Brier Score | Dev validation split |
