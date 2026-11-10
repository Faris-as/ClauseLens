# Data Card — ClauseLens

> **Version:** 0.1.0  
> **Date:** 10 November 2026  
> **Authors:** Faris Abdul Sukkur  

---

## 1. Overview & Ethical Considerations

ClauseLens is evaluated against public and synthetic contract datasets.
- **Strict Privacy Rule:** **Never** train or evaluate on confidential enterprise client contracts without explicit written consent and proper redaction.
- **Untrusted Input Rule:** Contract text is treated strictly as untrusted data, mitigating prompt injection risks.
- **Attribution Rule:** All public datasets are used strictly in compliance with their open-access licenses.

---

## 2. Public Datasets

### CUAD (Contract Understanding Atticus Dataset)
- **Source:** The Atticus Project / Stanford
- **URL:** https://huggingface.co/datasets/theatticusproject/cuad
- **License:** CC BY 4.0
- **Size:** 510 commercial contracts, 13,000+ expert annotations across 41 categories.
- **Use in ClauseLens:** Gold-standard ground truth for English contract extraction across the 10 core fields.

### ContractNLI
- **Source:** Stanford NLP Group
- **URL:** https://stanfordnlp.github.io/contract-nli
- **License:** CC BY 4.0
- **Size:** 607 Non-Disclosure Agreements (NDAs).
- **Use in ClauseLens:** Document-level natural language inference, testing negative/unmentioned assertions and grounded Q&A.

---

## 3. Synthetic Arabic & Bilingual Contracts

Because no public, expert-annotated Arabic commercial contract benchmark exists for clause extraction, ClauseLens generates synthetic legal contracts:
- **Domains:** NDAs, Service Level Agreements (SLAs), Supply Agreements.
- **Jurisdictions:** UAE Federal Commercial Law, Dubai International Financial Centre (DIFC), Abu Dhabi Global Market (ADGM).
- **Labeling Policy:** Every synthetic document is explicitly tagged as synthetic to prevent contamination.
- **Human Verification:** A native Arabic speaker reviews a random sample of synthetic contracts to verify legal phrasing consistency.
