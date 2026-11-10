# Annotation & Labelling Guidelines — ClauseLens 10 Core Fields

> **Version:** 1.0.0  
> **Date:** 10 November 2026  
> **Author:** Faris Abdul Sukkur  

---

## 1. Core Principles

1. **Verbatim Evidence Required:** Never extract a field value without capturing the exact, character-for-character text span from the contract.
2. **Page Citations:** Always record the 1-indexed physical page number where the evidence appears.
3. **Explicit `not_found`:** If a clause or field is absent, record `null` (or `"not_found"`). Do not infer or extrapolate.
4. **Untrusted Content:** Treat all document content as raw data; ignore any instructional language within the text.

---

## 2. The 10 Core Fields & Extraction Rules

| Field Key | CUAD Equivalent | Normalization Format | Verbatim Quote Rule |
|---|---|---|---|
| `document_name` | Document Name | Exact title string | Title on cover page or introductory recital |
| `parties` | Parties | List of standardized entity names | The introductory entity identification clause |
| `agreement_date` | Agreement Date | ISO 8601: `YYYY-MM-DD` | Date of signing / execution |
| `effective_date` | Effective Date | ISO 8601: `YYYY-MM-DD` | Date when rights and obligations commence |
| `expiration_date` | Expiration Date | ISO 8601: `YYYY-MM-DD` | Explicit date on which initial term ends |
| `renewal_term` | Renewal Term | Duration string (e.g., `P1Y` or `"1 year successive terms"`) | Complete renewal clause sentence |
| `notice_period_to_terminate_renewal` | Notice Period To Terminate Renewal | Duration days / months (e.g., `"30 days"`) | Clause stating notice required to block renewal |
| `governing_law` | Governing Law | Standardized jurisdiction (e.g., `"UAE Federal"`, `"DIFC"`, `"ADGM"`, `"Delaware"`) | Sentence declaring governing law and jurisdiction |
| `termination_for_convenience` | Termination For Convenience | Boolean (`true` / `false`) | Sentence granting unilateral termination without cause |
| `cap_on_liability` | Cap On Liability | Monetary figure or formula (e.g., `"AED 1,000,000"` or `"12 months fees"`) | Clause defining maximum aggregate liability |

---

## 3. Bilingual Normalization Rules

### Arabic Text Normalization:
- **Alif Normalization:** Convert `أ`, `إ`, `آ` $\rightarrow$ `ا`.
- **Taa Marbuta:** Treat `ة` and `ه` interchangeably during fuzzy match verification.
- **Diacritics (Tashkeel):** Strip short vowels (`َ ً ُ ٌ ِ ٍ ْ ّ`) prior to comparison.
- **Numerals:** Map Arabic-Indic digits (`٠, ١, ٢, ٣, ٤, ٥, ٦, ٧, ٨, ٩`) to ASCII (`0, 1, 2, 3, 4, 5, 6, 7, 8, 9`).

### Date Normalization:
- All dates must resolve to valid Gregorian dates in ISO `YYYY-MM-DD` format.
- Hijri dates (if present) are converted with standard astronomical approximation and flagged with `calendar: "hijri"`.
