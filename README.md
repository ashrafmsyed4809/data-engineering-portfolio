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



### Project 04 – Batch ETL with Star Schema (Portfolio Summary)
#### What this project is

Project 04 demonstrates core data warehousing fundamentals by building a batch ETL pipeline that loads raw CSV data into a PostgreSQL data warehouse using a Star Schema.
The project focuses on data modeling, SQL transformations, and historical data management, not orchestration or scheduling.

### What problem this project solves

Businesses need reliable, historical reporting on sales data.
This project shows how to:

Convert raw transactional data into analytics-ready tables

Preserve historical customer changes using SCD Type 2

Build a fact table that supports accurate reporting

#### What I built (plain language)

#### Staging layer

Raw CSV files are loaded into staging tables with minimal transformation

Metadata columns (load_date, source_file) added for traceability

Dimensional model (Star Schema)

dim_date generated programmatically

dim_product and dim_store loaded idempotently

dim_customer implemented with Slowly Changing Dimension (Type 2) to track history

Fact table

fact_sales created at the transaction grain

Uses surrogate keys for all dimensions

Calculates business metrics like total sales amount

Data validation & analytics

Example analytical queries for revenue by store and customer history

Ensures correctness and usability of the warehouse

What this project intentionally does NOT include

This project does not include Python orchestration or scheduling.

That is intentional.

Project 04 focuses on:

SQL correctness

Dimensional modeling

SCD logic

Warehouse design

Workflow orchestration, retries, and monitoring are handled in Project 05.

This separation reflects real-world data engineering practices.

Technologies used

PostgreSQL

SQL (DDL + transformation logic)

CSV-based batch ingestion

pgAdmin

Dimensional Modeling (Star Schema)

SCD Type 2

Why this project matters

This project proves:

Strong understanding of data warehouse fundamentals

Ability to design analytics-ready schemas

Correct handling of historical data

Production-aware SQL design (idempotent loads, surrogate keys)

#### How this fits into the full portfolio

#### Project	Focus

Project 01–03	Data cleaning, validation, pipelines
Project 04	Warehouse modeling & SCD
Project 05	Orchestration, retries, monitoring

Cloud Projects	Deployment to Azure / AWS

Project 04 is the bridge between data pipelines and production systems.

One-line summary (for recruiters)

Built a batch ETL pipeline in PostgreSQL using a Star Schema, including SCD Type 2 for customer history and fact table loading with surrogate key lookups.