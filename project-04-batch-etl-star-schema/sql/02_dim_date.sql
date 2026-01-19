-- Generate dim_date
INSERT INTO warehouse.dim_date (...)
SELECT ...
FROM generate_series(DATE '2019-01-01', DATE '2030-12-31', INTERVAL '1 day') d
LEFT JOIN warehouse.dim_date dd ON dd.full_date = d
WHERE dd.full_date IS NULL;
