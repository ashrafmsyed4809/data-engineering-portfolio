import pandas as pd

# Canonical schema for all sources
CANONICAL_COLUMNS = [
    "transaction_id",
    "customer_id",
    "date",
    "amount",
    "currency",
    "source"
]

# -------------------------------
# Helper functions
# -------------------------------

def clean_strings(df, columns):
    """Strip whitespace for string columns"""
    for col in columns:
        df[col] = df[col].astype(str).str.strip()
    return df

def parse_dates(df, column):
    """Parse mixed-format dates safely"""
    df[column] = df[column].replace(["", "nan", "NaN", "None"], pd.NA)
    df[column] = pd.to_datetime(df[column], errors="coerce", format="mixed").dt.date
    return df

def clean_amounts(df, column):
    df[column] = pd.to_numeric(df[column], errors="coerce")
    return df

def normalize_currency(df, column):
    df[column] = df[column].str.upper()
    return df

def drop_invalid_rows(df):
    """Drop rows with missing critical fields or invalid amounts"""

    df["customer_id"] = df["customer_id"].replace("", pd.NA)
    df = df.dropna(subset=["transaction_id", "customer_id", "date", "amount"])
    df = df[df["amount"] > 0]
    return df

# -------------------------------
# Source-specific cleaning
# -------------------------------

def clean_stripe(df):
    df = df.rename(columns={
        "txn_id": "transaction_id",
        "customer": "customer_id",
        "created_at": "date"
    })
    df["source"] = "stripe"

    # Only clean string columns
    df = clean_strings(df, ["transaction_id", "customer_id", "currency"])
    df = parse_dates(df, "date")
    df = clean_amounts(df, "amount")
    df = normalize_currency(df, "currency")

    return df

def clean_pos(df):
    df = df.rename(columns={
        "order_id": "transaction_id",
        "cust_id": "customer_id",
        "sale_date": "date",
        "total": "amount"
    })
    df["source"] = "pos"

    df = clean_strings(df, ["transaction_id", "customer_id", "currency"])
    df = parse_dates(df, "date")
    df = clean_amounts(df, "amount")
    df = normalize_currency(df, "currency")

    return df

def clean_api(df):
    df = df.rename(columns={
        "id": "transaction_id",
        "timestamp": "date",
        "amount_usd": "amount"
    })
    df["currency"] = "USD"
    df["source"] = "api"

    df = clean_strings(df, ["transaction_id", "customer_id"])
    df = parse_dates(df, "date")
    df = clean_amounts(df, "amount")

    return df

# -------------------------------
# Merge and finalize
# -------------------------------

def merge_sources(dfs):
    """
    Accepts a list of cleaned dataframes
    Returns a single canonical dataframe
    """
    df_all = pd.concat(dfs, ignore_index=True)
    df_all = drop_invalid_rows(df_all)
    df_all = df_all.drop_duplicates(subset=["transaction_id"])
    df_all = df_all[CANONICAL_COLUMNS]
    return df_all
