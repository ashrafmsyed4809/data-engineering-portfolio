
import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw/transactions_raw.csv")

def ingest_data() -> pd.DataFrame:
    """
    Read raw transaction data from CSV.
    """
    if not RAW_DATA_PATH.exists():
        raise FileNotFoundError(f"Raw data not found at {RAW_DATA_PATH}")

    df = pd.read_csv(RAW_DATA_PATH)
    return df
