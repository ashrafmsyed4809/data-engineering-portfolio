-- Total sales by store
SELECT ds.store_name, SUM(fs.total_sales_amount) AS revenue
FROM warehouse.fact_sales fs
JOIN warehouse.dim_store ds ON fs.store_key = ds.store_key
GROUP BY ds.store_name;

-- Customer history example
SELECT customer_id, first_name, last_name, effective_date, end_date, is_current
FROM warehouse.dim_customer
ORDER BY customer_id, effective_date;
