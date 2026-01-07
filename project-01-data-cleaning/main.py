import pandas as pd
from src.clean import clean_stripe, clean_pos, clean_api, merge_sources

from pathlib import Path
import pandas as pd
from src.clean import clean_stripe, clean_pos, clean_api, merge_sources
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Project root = location of main.py
PROJECT_ROOT = Path(__file__).resolve().parent

DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_FINAL = PROJECT_ROOT / "data" / "final"

# Load raw CSVs

df_stripe = pd.read_csv(DATA_RAW / "sales_stripe.csv")
df_pos = pd.read_excel(DATA_RAW / "sales_pos.xlsx")
df_api = pd.read_json(DATA_RAW / "sales_api.json")

#print("Stripe raw rows:", len(df_stripe))
#print("POS raw rows:", len(df_pos))
#print("API raw rows:", len(df_api))


logging.info("Stripe raw rows: %s", len(df_stripe))
logging.info("POS raw rows: %s", len(df_pos))
logging.info("API raw rows: %s", len(df_api))




#df_stripe = pd.read_csv("C:/Users/ashra/PycharmProjects/Ashraf_Portfolio_Projects/data/raw/sales_stripe.csv")
#df_pos = pd.read_excel("C:/Users/ashra/PycharmProjects/Ashraf_Portfolio_Projects/data/raw/sales_pos.xlsx")
#df_api = pd.read_json("C:/Users/ashra/PycharmProjects/Ashraf_Portfolio_Projects/data/raw/sales_api.json")

# Clean each source
df_stripe_clean = clean_stripe(df_stripe)
df_pos_clean = clean_pos(df_pos)
df_api_clean = clean_api(df_api)

# Merge all sources
df_final = merge_sources([df_stripe_clean, df_pos_clean, df_api_clean])

#print("Final cleaned rows:", len(df_final))


assert df_final["transaction_id"].isna().sum() == 0
assert df_final["customer_id"].isna().sum() == 0
assert (df_final["amount"] <= 0).sum() == 0
# sorting

df_final = df_final.sort_values(by=["date", "transaction_id"])

assert df_final.duplicated(subset=["transaction_id"]).sum() == 0

# Save final output

DATA_FINAL.mkdir(parents=True, exist_ok=True)
df_final.to_csv(DATA_FINAL / "clean_sales.csv", index=False)
#df_final.to_csv("C:/Users/ashra/PycharmProjects/Ashraf_Portfolio_Projects/data/final/clean_sales3.csv", index=False)
logging.info("Final cleaned rows: %s", len(df_final))
print("Pipeline completed. Final rows:", len(df_final))
