# Security & Privacy Policy — ClauseLens

> **Document Version:** 0.1.0  
> **Date:** 10 November 2026  

---

## 1. Threat Model & Mitigations

| Threat | Risk Level | Architectural Mitigation |
|---|---|---|
| **Cross-User Document Leakage** | Critical | Mandatory tenant filtering on all queries (`WHERE owner_id = :current_user_id`). Automated cross-user integration tests. |
| **Prompt Injection via Contract Text** | High | Contract text is strictly demarcated as untrusted payload data. Extraction and Q&A pipelines have no tool access or execution capabilities. |
| **Data Leakage into Logs** | High | Structured JSON logger explicitly filters out raw document text, prompts, and extracted strings. Only IDs, statuses, and execution durations are logged. |
| **Arbitrary File Upload / Malicious Blobs** | High | MIME type sniffing, strict file extension whitelist (PDF, PNG, JPEG, TIFF), 25 MB file limit, and 200 page ceiling. File parsing runs isolated inside containerized worker. |
| **Insecure Secrets & Tokens** | High | JWT tokens with short TTLs and Argon2 password hashing. All credentials loaded exclusively via environment variables; CI enforces secret scanning. |

---

## 2. Data Deletion Guarantee (Right to Erasure)
When a user deletes a document via `DELETE /api/v1/documents/{id}`, ClauseLens performs a hard transactional cascade:
- Deletes the source binary blob from disk.
- Deletes all parsed pages and OCR records.
- Deletes all text chunks and pgvector embedding rows.
- Deletes all extracted fields, review history, and computed deadlines.
No orphan data persists in the database or vector index.
