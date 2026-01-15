# Project 04 – Batch ETL with Fact & Dimension Modeling

## Goal

Design and implement a **production-style batch ETL pipeline** that transforms raw transactional data into a **star schema** (fact and dimension tables) suitable for analytics and BI reporting.

This project demonstrates:

* Dimensional modeling (Kimball-style)
* Batch ETL design
* Data quality enforcement
* Incremental loads
* SQL-first analytics thinking

---

## Business Scenario

A fictional retail company wants analytics on **sales performance** across:

* Time
* Customers
* Products
* Stores

Raw transactional data arrives daily as CSV files from multiple operational systems.

---

## Source Data (Raw / Staging)

### 1. `raw_sales_transactions`

| column           | description         |
| ---------------- | ------------------- |
| transaction_id   | unique transaction  |
| transaction_date | datetime            |
| customer_id      | customer identifier |
| product_id       | product identifier  |
| store_id         | store identifier    |
| quantity         | units sold          |
| unit_price       | price per unit      |

### 2. `raw_customers`

| column      | description         |
| ----------- | ------------------- |
| customer_id | natural key         |
| first_name  | customer first name |
| last_name   | customer last name  |
| email       | email               |
| city        | city                |
| state       | state               |

### 3. `raw_products`

| column       | description |
| ------------ | ----------- |
| product_id   | natural key |
| product_name | name        |
| category     | category    |
| brand        | brand       |

### 4. `raw_stores`

| column     | description |
| ---------- | ----------- |
| store_id   | natural key |
| store_name | store name  |
| city       | city        |
| state      | state       |

---

## Target Data Model (Star Schema)

### Dimension Tables

#### `dim_date`

| column        |
| ------------- |
| date_key (PK) |
| full_date     |
| day           |
| month         |
| month_name    |
| quarter       |
| year          |
| is_weekend    |

#### `dim_customer`

| column            |
| ----------------- |
| customer_key (PK) |
| customer_id (NK)  |
| first_name        |
| last_name         |
| email             |
| city              |
| state             |
| effective_date    |
| end_date          |
| is_current        |

(SCD Type 2)

#### `dim_product`

| column           |
| ---------------- |
| product_key (PK) |
| product_id (NK)  |
| product_name     |
| category         |
| brand            |

#### `dim_store`

| column         |
| -------------- |
| store_key (PK) |
| store_id (NK)  |
| store_name     |
| city           |
| state          |

---

### Fact Table

#### `fact_sales`

| column             |
| ------------------ |
| sales_key (PK)     |
| date_key (FK)      |
| customer_key (FK)  |
| product_key (FK)   |
| store_key (FK)     |
| quantity_sold      |
| unit_price         |
| total_sales_amount |

---

## ETL Flow (Batch)

```
RAW FILES
   ↓
STAGING TABLES
   ↓
DIMENSION LOADS
   ↓
FACT LOAD
```

### Step 1: Extract

* Load CSV files into staging tables
* Enforce schema & data types

### Step 2: Transform

* Standardize strings (trim, upper/lower)
* Handle NULLs
* Generate surrogate keys
* Apply SCD Type 2 logic for customers
* Create date dimension

### Step 3: Load

* Load dimensions first
* Load fact table using surrogate keys
* Support incremental batch loads

---

## Data Quality Checks

* No NULL foreign keys in fact table
* Quantity > 0
* Unit price >= 0
* Referential integrity validation
* Duplicate transaction detection

---

## Tech Stack

* Python (Pandas)
* PostgreSQL
* SQL (DDL + analytics queries)
* Git + GitHub

---

## Analytics Queries (Examples)

* Daily sales revenue
* Top 10 products by revenue
* Sales by state
* Customer lifetime value

---

## Repository Structure

```
project-04-batch-etl-star-schema/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── sql/
│   ├── ddl/
│   ├── transformations/
│   └── analytics/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load_dimensions.py
│   └── load_fact.py
│
├── tests/
├── README.md
└── requirements.txt
```

---

## Why This Project Matters

This project mirrors **real-world analytics engineering** work and demonstrates:

* Business-to-warehouse translation
* Dimensional modeling
* Batch ETL best practices
* SQL analytics readiness

---

**Next Step:**

1. Create raw CSV sample data
2. Write DDL for staging & warehouse tables
3. Implement dimension loaders
4. Implement fact loader
5. Add analytics queries
