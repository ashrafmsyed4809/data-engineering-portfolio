# Project 02: Data Validation Pipeline (End-to-End)

## Overview

This project implements a **production-style data validation pipeline** for transactional data using Python.
The pipeline ingests raw data, applies schema and business-rule validation, isolates rejected records, and produces **data quality metrics** — all backed by automated testing and CI/CD.

This project reflects **real-world data engineering responsibilities**, where data quality, reproducibility, and reliability are critical.

---

## Key Objectives

* Build a **deterministic, auditable data validation pipeline**
* Apply **business rules** beyond basic data cleaning
* Demonstrate **testing and CI/CD** best practices
* Produce **data quality metrics** for monitoring and reporting

---

## Tech Stack

* **Python 3**
* **Pandas**
* **Pytest**
* **GitHub Actions (CI/CD)**
* **Structured Logging**
* **JSON-based Data Quality Reports**

---

## Project Structure

```
project-02-data-validation-pipeline/
├── src/
│   ├── __init__.py
│   ├── ingest.py          # Data ingestion logic
│   ├── validate.py        # Validation rules and checks
│   └── config.py          # Configuration and logging
├── tests/
│   ├── __init__.py
│   └── test_validation.py # Unit tests
├── data/
│   ├── raw/               # Input datasets
│   ├── rejected/          # Invalid records with reasons
│   └── processed/         # Valid data + quality reports
├── run_pipeline.py        # Pipeline entry point
├── requirements.txt
└── .github/workflows/
    └── project-02-ci.yml  # CI pipeline
```

---

## Pipeline Workflow

1. **Ingest raw data** from CSV files
2. **Validate records** using schema and business rules
3. **Separate valid and rejected records**
4. **Persist rejected records** for audit and analysis
5. **Generate data quality metrics** in JSON format
6. **Log pipeline execution details**

Run the pipeline locally:

```bash
python run_pipeline.py
```

---

## Data Validation Rules

The pipeline enforces the following validations:

| Rule               | Description                                                |
| ------------------ | ---------------------------------------------------------- |
| Required fields    | Mandatory columns must be present                          |
| Null checks        | Critical fields cannot be null                             |
| Business logic     | Transaction amount must be greater than zero               |
| Allowed values     | Currency must be from an approved list                     |
| Duplicate handling | Duplicate transaction IDs are rejected (first record kept) |

Rejected records are saved separately with clear reasons for rejection.

---

## Data Quality Metrics

After each run, a **data quality report** is generated:

```
data/processed/data_quality_report.json
```

Example output:

```json
{
  "total_records": 8,
  "valid_records": 3,
  "rejected_records": 5,
  "rejection_rate": 0.62
}
```

This enables **continuous monitoring of data quality**.

---

## Testing

* Unit tests written using **pytest**
* Tests validate:

  * Correct separation of valid vs rejected records
  * Duplicate detection logic
* Run tests locally:

```bash
python -m pytest
```

---

## Continuous Integration (CI/CD)

* CI implemented using **GitHub Actions**
* Automatically runs on every push and pull request
* Workflow steps:

  * Install dependencies
  * Execute unit tests
* Successful runs are indicated by a **green check ✅** in GitHub Actions

---

## Why This Project Matters

This project demonstrates skills directly applicable to data engineering roles:

* Production-style **data validation**
* Defensive data engineering practices
* Test-driven development
* CI/CD integration
* Clear separation of concerns and modular design

---

## Future Enhancements

* Add incremental data loads
* Integrate Great Expectations
* Extend metrics for trend-based quality monitoring
* Persist results to a database instead of files

---

## Author

**Ashraf Syed**
Data Engineering & Automation
GitHub Portfolio: *data-engineering-portfolio*