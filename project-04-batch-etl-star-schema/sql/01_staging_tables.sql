-- CREATE staging tables
CREATE SCHEMA IF NOT EXISTS staging;

CREATE TABLE IF NOT EXISTS staging.stg_sales_transactions (
    transaction_id VARCHAR PRIMARY KEY,
    transaction_date DATE,
    customer_id VARCHAR,
    product_id VARCHAR,
    store_id VARCHAR,
    quantity INT,
    unit_price NUMERIC(10,2),
    load_date DATE DEFAULT CURRENT_DATE,
    source_file VARCHAR
);

-- Repeat similar for stg_customers, stg_products, stg_stores
