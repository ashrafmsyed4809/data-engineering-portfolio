# Project: Multi-Source Sales Data Cleaning Pipeline

## Goal
Build an end-to-end data engineering portfolio project focused on
data cleaning, standardization, and correctness.

## Stack
- Python
- Pandas
- Jupyter (exploration)
- PyCharm (production code)
- Git / GitHub

## Data Reality
- Stripe data provided as CSV
- POS data provided as Excel (.xlsx)
- API data provided as JSON
- Pipeline adjusted to handle heterogeneous input formats

## Canonical Schema
transaction_id, customer_id, date, amount, currency, source

## Key Bugs Solved
- tx1002 dropped due to date casting (`astype(str)`)
- Mixed date formats → NaT bug
- Safe date parsing using `format="mixed"`
- Fixed logic drift between notebook and production code
- Explicitly normalized empty strings to nulls before validation
- Replaced absolute paths with pathlib-based project-relative paths

## Current Status
- Day 1: Exploration complete
- Day 2: Cleaning logic complete
- clean.py created and validated
- Day 2: Cleaning logic finalized and validated via UI + terminal
- Day 3: Added row-count validation and data quality assertions
- Verified no silent data loss


## Next Step
- Day 3: Validation, metrics, logging

------------ Validaation ------
CSV -- Stripe

0	tx1001	C001	john@example.com	100.0	2024-01-05	USD
1	tx1002	C002	mary@example.com	85.5	01/06/2024	usd
2	tx1003	NaN	    alex@example.com   -20.0	2024/01/07	USD
3	tx1004	C004	sara@example.com	100.0	2024-13-01	USD
4	tx1002	C002	mary@example.com	85.5	01/06/2024	USD

Excel - POS

0	P5001	C001	2024-01-05	100.0	USD	pos
1	P5002	C003	2024-01-06	90.0	USD	pos
2	P5003	C004	2024-01-07	NaN	USD	pos

Json - API

0	api_9001	C005	2024-01-06 10:45:00+00:00	120
1	api_9002		2024-01-07 12:00:00+00:00	75

Final -- CSV

transaction_id,customer_id,date,amount,currency,source
tx1001,C001,2024-01-05,100.00,USD,stripe
tx1002,C002,2024-01-06,85.50,USD,stripe
P5001,C001,2024-01-05,100.00,USD,pos
P5002,C003,2024-01-06,90.00,USD,pos
api_9001,C005,2024-01-06,120.00,USD,api

The Record dropped -- Reason listed below

Stripe

There were two duplicates tx1002 so one dropped. 
tx1004 dropped due to invalid date 2024-13-01 
tx1003 dropped due to missing customer id 
so Stripe gave us only 2. 

Pos

There were 3 from POS but P5003 dropped due to missing
so it gave us only 2

API

There were only 2

one dropped due to missing customer id
so it gave us only 1

Before        After

Stripe 5       2
POS    3       2
Api    2       1

Now there are 5 recs in the final


