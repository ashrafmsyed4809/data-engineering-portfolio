Issues with the raw Data file.

    duplicate transaction

    missing customer ID

    negative amount

    invalid date

    inconsistent casing + spaces


data-cleaning-pipeline/
│
├── PROJECT_CONTEXT.md        ← ⭐ single source of truth
│
├── data/
│   ├── raw/
│   │   ├── sales_stripe.csv
│   │   ├── sales_pos.csv
│   │   └── sales_api.csv
│   │
│   └── final/
│       └── clean_sales.csv
│
├── notebooks/
│   └── exploration.ipynb
│
├── src/
│   ├── __init__.py
│   └── clean.py
│
├── main.py
├── requirements.txt
└── README.md


# Data Cleaning Pipeline (Multi-Source Sales Data)

## Overview
End-to-end data engineering project that cleans, standardizes, and merges
sales data from Stripe, POS, and API sources into a canonical schema.

## Key Features
- Handles mixed date formats safely
- Prevents silent data loss (NaT bug fix)
- Enforces data quality rules
- Deduplicates transactions correctly
- Production-ready Python pipeline

## Data Quality Guarantees
- No missing transaction_id, customer_id, date, or amount
- No non-positive transaction amounts
- Deterministic output ordering

## Design Decisions
- Cleaning logic separated from orchestration
- Explicit null normalization to prevent silent data loss
- Business keys enforced before deduplication

## How to Run
```bash
python main.py

