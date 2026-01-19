INSERT INTO warehouse.dim_store (store_id, store_name, city, state)
SELECT ...
FROM staging.stg_stores s
LEFT JOIN warehouse.dim_store ds ON ds.store_id = s.store_id
WHERE ds.store_id IS NULL;

