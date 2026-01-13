import pandas as pd
from typing import Tuple

ALLOWED_CURRENCIES = {"USD", "EUR", "GBP"}

def validate_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Validate transaction data.

    Returns:
        valid_df: records that passed all validations
        rejected_df: records that failed any validation with reason
    """
    df = df.copy()
    rejected_rows = []

    # 1. Required columns check
    missing_cols = set(df.columns) ^ set([
        "transaction_id",
        "customer_id",
        "transaction_date",
        "amount",
        "currency",
        "country",
        "payment_method",
    ])
    if missing_cols:
        raise ValueError(f"Schema mismatch. Columns: {df.columns}")

    # 2. Duplicate transaction_id (keep first, reject rest)
    duplicate_mask = df.duplicated(subset=["transaction_id"], keep="first")
    duplicates = df[duplicate_mask]

    for _, row in duplicates.iterrows():
        rejected_rows.append({**row, "reject_reason": "duplicate_transaction_id"})

    df = df[~duplicate_mask]


    # 3. Null customer_id
    null_customer = df[df["customer_id"].isna()]
    for _, row in null_customer.iterrows():
        rejected_rows.append({**row, "reject_reason": "missing_customer_id"})

    df = df[df["customer_id"].notna()]

    # 4. Invalid transaction_date
    df["transaction_date_parsed"] = pd.to_datetime(
        df["transaction_date"], errors="coerce"
    )
    invalid_dates = df[df["transaction_date_parsed"].isna()]
    for _, row in invalid_dates.iterrows():
        rejected_rows.append({**row, "reject_reason": "invalid_transaction_date"})

    df = df[df["transaction_date_parsed"].notna()]
    df.drop(columns=["transaction_date_parsed"], inplace=True)

    # 5. Invalid amount
    invalid_amount = df[(df["amount"].isna()) | (df["amount"] <= 0)]
    for _, row in invalid_amount.iterrows():
        rejected_rows.append({**row, "reject_reason": "invalid_amount"})

    df = df[(df["amount"].notna()) & (df["amount"] > 0)]

    # 6. Invalid currency
    invalid_currency = df[~df["currency"].isin(ALLOWED_CURRENCIES)]
    for _, row in invalid_currency.iterrows():
        rejected_rows.append({**row, "reject_reason": "invalid_currency"})

    df = df[df["currency"].isin(ALLOWED_CURRENCIES)]

    rejected_df = pd.DataFrame(rejected_rows)
    return df.reset_index(drop=True), rejected_df.reset_index(drop=True)



