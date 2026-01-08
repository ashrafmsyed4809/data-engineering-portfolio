# Project 02 — Automated Data Validation & Quality Pipeline

## Overview
This project demonstrates a production-style data engineering pipeline
focused on data quality, validation, and reliability.

The pipeline ingests raw transactional data, validates it against
schema and business rules, rejects bad records, and loads trusted data
into a relational database.

## Architecture
Raw Data → Validation → Transformation → Load → Analytics-Ready Tables

## Key Features
- Schema validation
- Business rule enforcement
- Rejected data handling
- Unit testing
- CI/CD with GitHub Actions

## Tech Stack
- Python
- Pandas
- SQL (PostgreSQL / SQLite)
- pytest
- GitHub Actions

## How to Run
```bash
python run_pipeline.py
