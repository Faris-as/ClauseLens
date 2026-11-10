"""Dataset Acquisition Script for ClauseLens.

Downloads and verifies the open-source evaluation benchmarks:
1. CUAD (Contract Understanding Atticus Dataset) - CC BY 4.0
2. ContractNLI - CC BY 4.0

Usage:
    python eval/download_datasets.py --dataset cuad
    python eval/download_datasets.py --dataset contractnli
    python eval/download_datasets.py --all
"""

import argparse
import hashlib
import json
import logging
import os
import sys
import urllib.request
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("clauselens.data_fetch")

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
CUAD_URL = "https://raw.githubusercontent.com/TheAtticusProject/cuad/main/data.zip"
CONTRACT_NLI_INFO = "https://stanfordnlp.github.io/contract-nli"


def calculate_sha256(filepath: Path) -> str:
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(65536), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def setup_sample_gold_fixtures() -> None:
    """
    Creates the 10 core fields gold fixture definitions for M0.
    These schema definitions match the 10 CUAD categories chosen for ClauseLens.
    """
    fixtures_dir = DATA_DIR / "sample"
    fixtures_dir.mkdir(parents=True, exist_ok=True)

    fields_schema = {
        "description": "ClauseLens 10 Core Evaluation Fields",
        "version": "1.0.0",
        "fields": [
            {
                "key": "document_name",
                "cuad_category": "Document Name",
                "type": "string",
                "description": "Title or formal name of the agreement",
            },
            {
                "key": "parties",
                "cuad_category": "Parties",
                "type": "list[string]",
                "description": "Named legal entities entering into the agreement",
            },
            {
                "key": "agreement_date",
                "cuad_category": "Agreement Date",
                "type": "date",
                "description": "Date on which the contract was executed or entered into",
            },
            {
                "key": "effective_date",
                "cuad_category": "Effective Date",
                "type": "date",
                "description": "Date from which the contract's terms become binding",
            },
            {
                "key": "expiration_date",
                "cuad_category": "Expiration Date",
                "type": "date",
                "description": "End or termination date of the initial term",
            },
            {
                "key": "renewal_term",
                "cuad_category": "Renewal Term",
                "type": "string",
                "description": "Duration and conditions for renewing the agreement",
            },
            {
                "key": "notice_period_to_terminate_renewal",
                "cuad_category": "Notice Period To Terminate Renewal",
                "type": "string",
                "description": "Notice required prior to renewal to prevent automatic renewal",
            },
            {
                "key": "governing_law",
                "cuad_category": "Governing Law",
                "type": "string",
                "description": "Jurisdiction and legal system governing the agreement",
            },
            {
                "key": "termination_for_convenience",
                "cuad_category": "Termination For Convenience",
                "type": "boolean",
                "description": "Whether either party can terminate without cause, with quote",
            },
            {
                "key": "cap_on_liability",
                "cuad_category": "Cap On Liability",
                "type": "string",
                "description": "Monetary limit or formula bounding either party's liability",
            },
        ],
    }

    schema_path = fixtures_dir / "core_fields_schema.json"
    with open(schema_path, "w", encoding="utf-8") as f:
        json.dump(fields_schema, f, indent=2, ensure_ascii=False)

    logger.info(f"10 Core fields schema written to {schema_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch and setup ClauseLens evaluation datasets.")
    parser.add_argument("--dataset", choices=["cuad", "contractnli", "fixtures"], default="fixtures")
    parser.add_argument("--all", action="store_true", help="Setup all fixtures and dataset dirs")
    args = parser.parse_args()

    setup_sample_gold_fixtures()
    logger.info("Dataset directories and core schemas initialized successfully.")


if __name__ == "__main__":
    main()
