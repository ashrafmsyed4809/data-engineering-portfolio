INSERT INTO warehouse.dim_product (product_id, product_name, category, brand)
SELECT ...
FROM staging.stg_products p
LEFT JOIN warehouse.dim_product dp ON dp.product_id = p.product_id
WHERE dp.product_id IS NULL;
