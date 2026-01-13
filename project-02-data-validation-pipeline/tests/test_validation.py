import pandas as pd
from src.validate import validate_data

def sample_df():
    return pd.DataFrame(
        {
            "transaction_id": ["T1", "T1", "T2"],
            "customer_id": ["C1", "C1", None],
            "transaction_date": ["2024-01-01", "2024-01-01", "bad-date"],
            "amount": [100, 100, -5],
            "currency": ["USD", "USD", "EUR"],
            "country": ["USA", "USA", "Germany"],
            "payment_method": ["card", "card", "card"],
        }
    )

def test_validation_splits_valid_and_rejected():
    df = sample_df()
    valid_df, rejected_df = validate_data(df)

    assert len(valid_df) == 1
    assert len(rejected_df) == 2

def test_duplicate_handling_keeps_first():
    df = sample_df()
    valid_df, rejected_df = validate_data(df)

    assert valid_df.iloc[0]["transaction_id"] == "T1"
