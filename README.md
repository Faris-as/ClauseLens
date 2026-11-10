# ClauseLens — Bilingual Contract Intelligence Assistant

[![CI](https://github.com/Faris-as/ClauseLens/actions/workflows/ci.yml/badge.svg)](https://github.com/Faris-as/ClauseLens/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![EasyOCR](https://img.shields.io/badge/OCR-EasyOCR_(ar%2Beng)-FF6F00)](https://github.com/JaidedAI/EasyOCR)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16_+_pgvector-336791?logo=postgresql&logoColor=white)](https://github.com/pgvector/pgvector)

> **Important Notice:** ClauseLens is an AI-assisted analysis tool designed for contract managers, legal reviewers, and procurement teams. It surfaces verbatim evidence and computes deadline alerts. **It does not provide legal advice or legal conclusions.**

---

## 1. The Problem

Enterprise and government procurement teams in the UAE process contracts across both English and Modern Standard Arabic. Manual contract review creates critical bottlenecks:
- Key obligations, renewal terms, and governing law clauses are missed or buried across 50+ page agreements.
- Notice periods (e.g., 30/60-day auto-renewal termination deadlines) expire unnoticed, locking organizations into costly unintended renewals.
- Traditional LLM chatbots hallucinate or reference outside knowledge rather than citing the contract's actual binding text.
- Arabic scanned contracts with complex ligatures and mixed RTL/LTR numerical figures fail standard OCR pipelines.

**ClauseLens** solves this with an evidence-first architecture: every extracted field requires verbatim quoted text and a verified page citation. A human reviewer stays in control to approve, edit, or reject every value.

---

## 2. Core Capabilities

- 🔍 **10 Core Field Extraction with Verbatim Citations**: Extracts document title, parties, agreement date, effective date, expiry date, renewal term, notice period, governing law, termination for convenience, and liability cap.
- 🇦🇪 **Bilingual Arabic & English Support**: Ingests digital PDFs and scanned documents in Arabic and English using deep-learning-based OCR (`EasyOCR`).
- 🛡️ **Anti-Hallucination & Evidence Validation**: Quotes must match the source text (exact or normalized). Failed or fabricated quotes are rejected or flagged with lowered confidence scores.
- 💬 **Grounded Q&A**: Answers questions exclusively using retrieved contract passages. Returns an explicit `"not_found"` sentinel when information is absent. Treats contract text strictly as untrusted data to mitigate prompt injection.
- ⏰ **Proactive Deadline Engine**: Automatically computes expiration dates, auto-renewal cutoffs, and notice windows, surfacing contracts due within 30, 60, or 90 days.
- 👥 **Human-in-the-Loop Review Queue**: Streamlit-based dual-pane reviewer interface with native RTL support for Arabic, side-by-side evidence inspection, and full audit logging.
- 🔌 **Integration-Ready REST API**: Fully documented OpenAPI/Swagger endpoints with token-based authentication and user-isolated multi-tenant security.

---

## 3. System Architecture

```
 Browser (Streamlit Review UI)        External Enterprise Systems (ERP / CLM)
            |                                      |
            +----------------- HTTPS / REST --------+
                                  |
                    FastAPI Service (Auth · Validation · API)
                      |             |             |
                 PostgreSQL     Task Queue     Storage
                (+ pgvector)    (Redis/RQ)    (Raw Documents)
                      ^             |
                      |    Asynchronous Ingestion Worker
                      |    1. Type & scan detection (PyMuPDF)
                      |    2. Image preprocessing & EasyOCR (ar + en)
                      |    3. Heading-aware clause segmentation
                      |    4. Embeddings (bge-m3) & vector indexing
                      |    5. Structured field extraction (IFM API / LLM)
                      |    6. Quote verification & confidence scoring
                      |             |
                      +--- Swappable Model Layer ---+
                          EasyOCR | bge-m3 | IFM API
```

---

## 4. Quick Start (One Command)

### Prerequisites
- Docker & Docker Compose
- Git

### 1. Clone & Configure
```bash
git clone https://github.com/Faris-as/ClauseLens.git
cd ClauseLens
cp .env.example .env
```

*(Edit `.env` to supply your `IFM_API_KEY` or custom LLM endpoints if testing extraction).*

### 2. Launch the Stack
```bash
docker compose up -d
```

### 3. Access Services
- **Interactive Review UI:** [http://localhost:8501](http://localhost:8501)
- **FastAPI Documentation (Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Health Check Probe:** [http://localhost:8000/health](http://localhost:8000/health)

---

## 5. Repository Layout

```
clauselens/
  app/
    api/            # REST API endpoints, schemas, JWT auth, dependencies
    core/           # Configuration (pydantic-settings), structured logging
    ingestion/      # PDF parsing, preprocessing, EasyOCR (ar/en)
    segmentation/   # Legal clause boundary chunker
    retrieval/      # Hybrid dense (pgvector) + keyword search & re-ranking
    extraction/     # Prompts, JSON schemas, quote validator, confidence model
    qa/             # Grounded retrieval Q&A with citation guards
    deadlines/      # Renewal & notice deadline arithmetic
    models/         # LLMProvider abstraction (IFM API / local / hosted)
    db/             # SQLAlchemy 2.0 models, Alembic migrations
    worker/         # Asynchronous RQ background jobs
  ui/               # Streamlit human review interface with RTL support
  eval/             # Evaluation harness, metrics, CUAD & Arabic benchmarks
  data/             # Public benchmarks & synthetic legal templates
  tests/            # Unit, integration, and security test suites
  docker-compose.yml
  Dockerfile
  pyproject.toml
```

---

## 6. Evaluation & Benchmarks

ClauseLens enforces a reproducible evaluation harness (`python eval/run_eval.py`) scored against:
1. **English Contracts:** CUAD (Atticus Project) test split across 10 core fields.
2. **Arabic & Bilingual Contracts:** Curated synthetic UAE commercial agreements (Federal Law, DIFC, ADGM).

Evaluation results, character error rates (CER) for OCR, and bootstrap 95% confidence intervals are generated directly via `python eval/run_eval.py` and saved to `eval/reports/`.

---

## 7. Dataset Attribution & Licenses

- **CUAD (Contract Understanding Atticus Dataset):** [Atticus Project](https://www.atticusproject.org/), licensed under CC BY 4.0.
- **ContractNLI:** Stanford NLP, licensed under CC BY 4.0.
- All code in this repository is licensed under the [MIT License](LICENSE).
