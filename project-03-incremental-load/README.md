# Project 03: Incremental API Load with Change Data Capture (CDC)

## Overview

This project demonstrates a production-style data engineering pipeline that ingests live market data from the CoinGecko API into PostgreSQL using incremental loading and change data capture (CDC).

The pipeline is designed to be **idempotent**, **append-only for history**, and **safe to re-run**, closely mirroring how real-world financial and event-driven systems are built.

---

## Architecture

```
CoinGecko API
     │
     ▼
Python Ingestion Script
(ingest_coingecko.py)
     │
     ├── UPSERT → current_prices
     └── INSERT → price_history (CDC)
     │
     ▼
PostgreSQL
```

---

## Data Source

* **API:** CoinGecko Public API
* **Endpoint:** `/coins/markets`
* **Characteristics:**

  * Frequently changing prices
  * Timestamps updated on every API call
  * Ideal for incremental ingestion and CDC

---

## Database Design

### `current_prices` (Latest State)

Stores the most recent price and market data per coin.

* One row per coin
* Updated using UPSERT
* Optimized for fast reads

### `price_history` (Append-Only CDC Table)

Stores historical price changes over time.

* Append-only
* One row per coin per meaningful price change
* Enforces uniqueness to prevent duplicates

---

## Incremental Load & CDC Strategy

### Key Challenge

CoinGecko updates timestamps on every API call, making timestamp-only incremental logic unreliable.

### Solution

This pipeline uses **price-based change data capture (CDC)**:

* Fetch latest prices from the API
* Compare against stored prices in `current_prices`
* Insert into `price_history` **only when the price changes beyond a defined threshold**
* Always UPSERT into `current_prices`

This approach prevents unnecessary history noise while preserving meaningful market movements.

---

## Precision Handling

* API prices arrive as Python `float`
* PostgreSQL `NUMERIC` fields are returned as `Decimal`
* All price calculations are performed using `Decimal` to ensure correctness and financial precision

---

## Scheduling & Streaming Simulation

Although implemented as a batch script, this pipeline is designed for near-real-time execution and can be scheduled using:

* **Cron jobs** (local or server-based)
* **n8n workflows** (webhook or scheduled trigger)
* **Apache Airflow** (DAG-based orchestration)

Frequent execution simulates a streaming ingestion model commonly used in financial systems.

---

## Project Structure

```
project-03-incremental-load/
│
├── scripts/
│   └── ingest_coingecko.py
├── .env
├── requirements.txt
├── .gitignore
└── README.md
```

---

## How to Run

1. Create PostgreSQL tables (`current_prices`, `price_history`)
2. Configure environment variables in `.env`
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the ingestion script:

   ```bash
   python scripts/ingest_coingecko.py
   ```

The script is safe to re-run and will only append meaningful changes.

---

## What This Project Demonstrates

* API ingestion from real-world data sources
* Incremental loading strategies
* Change Data Capture (CDC)
* Append-only historical modeling
* PostgreSQL upserts and constraints
* Financial data precision handling
* Production-style pipeline design

---

## Future Enhancements

* Dockerized deployment
* Raw (bronze) data storage layer
* Visualization of historical price trends
* Monitoring and alerting

---

## Author

**Ashraf Syed**

Data Engineering & AI Automation Portfolio
