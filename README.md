# Data Engineering Portfolio

This repository contains end-to-end data engineering projects focused on
data cleaning, validation, and production-ready pipelines.

## Projects

### Project 01 – Multi-Source Data Cleaning Pipeline
- CSV / Excel / JSON ingestion
- Canonical schema design
- Data quality enforcement
- Portable Python pipeline

### Project 02 – Data Validation & Standardization Pipeline

- Rule-based data validation framework

- Vendor name normalization and deduplication

- Null, empty, and inconsistent value handling

- Reusable validation utilities

- Production-ready Python project structure

#### Focus: Ensuring data correctness and consistency before downstream consumption.

### Project 03 – Incremental API Ingestion with Change Data Capture (CDC)

- Live API ingestion (CoinGecko)

- Incremental loading and idempotent pipeline design

- Change Data Capture (CDC) using price-based detection

- Append-only historical modeling

- PostgreSQL upserts and precision-safe numeric handling

- Production-style logging and error handling

#### Focus: Building real-world, production-style data pipelines for frequently changing data sources.

## Project 04 – Batch ETL with Star Schema

### Overview

Project 04 demonstrates core **data warehousing fundamentals** by building a batch ETL pipeline that loads raw CSV data into a PostgreSQL data warehouse using a **Star Schema**.

The project focuses on **SQL-based transformations**, **dimensional modeling**, and **historical data management**, rather than orchestration or scheduling.

---

### Problem Statement

Businesses require reliable, analytics-ready data models that support accurate historical reporting.

This project addresses how to:
- Convert raw transactional data into structured warehouse tables
- Preserve historical changes to customer attributes
- Design fact and dimension tables that support business analytics

---

### What Was Built

#### Staging Layer
- Raw CSV files are loaded into staging tables with minimal transformation
- Metadata columns (`load_date`, `source_file`) are added for traceability and auditing

#### Dimensional Model (Star Schema)
- `dim_date` generated programmatically to support time-based analysis
- `dim_product` and `dim_store` loaded idempotently
- `dim_customer` implemented as a **Slowly Changing Dimension (Type 2)** to track historical changes

#### Fact Table
- `fact_sales` created at the transaction grain
- Uses surrogate keys for all dimensions
- Calculates business metrics such as total sales amount

#### Analytics & Validation
- Sample analytical queries included (e.g., revenue by store, customer history)
- Ensures the warehouse is correct, queryable, and analytics-ready

---

### What This Project Intentionally Does NOT Include

This project does **not** include Python-based orchestration or scheduling.

That omission is **intentional**.

Project 04 focuses exclusively on:
- SQL correctness
- Dimensional modeling
- SCD Type 2 logic
- Data warehouse design principles

Workflow orchestration, retries, and monitoring are implemented in **Project 05**, reflecting real-world separation of responsibilities in data engineering systems.

---

### Technologies Used

- PostgreSQL
- SQL (DDL and transformation logic)
- CSV-based batch ingestion
- pgAdmin
- Dimensional Modeling (Star Schema)
- Slowly Changing Dimensions (Type 2)

---

### Why This Project Matters

This project demonstrates:
- Strong understanding of data warehouse fundamentals
- Ability to design analytics-ready schemas
- Correct handling of historical data using SCD Type 2
- Production-aware SQL design (idempotent loads, surrogate keys)

---

### How This Fits into the Portfolio

| Project | Focus |
|------|------|
| Project 01–03 | Data cleaning, validation, and pipelines |
| **Project 04** | **Warehouse modeling & historical data (SCD)** |
| Project 05 | Orchestration, retries, and monitoring |
| Cloud Projects | Deployment on Azure / AWS |

Project 04 serves as the **bridge between data pipelines and production-grade analytical systems**.

---

### One-Line Summary (Recruiter-Friendly)

Built a batch ETL pipeline in PostgreSQL using a Star Schema, including SCD Type 2 for customer history and fact table loading with surrogate key lookups.

