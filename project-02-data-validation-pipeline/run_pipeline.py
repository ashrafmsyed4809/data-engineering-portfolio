from src.ingest import ingest_data
from src.validate import validate_data
from pathlib import Path

def main():
    df = ingest_data()
    valid_df, rejected_df = validate_data(df)

    print(f"Valid records: {len(valid_df)}")
    print(f"Rejected records: {len(rejected_df)}")

    REJECTED_PATH = Path("data/rejected/rejected_records.csv")
    REJECTED_PATH.parent.mkdir(exist_ok=True)

    rejected_df.to_csv(REJECTED_PATH, index=False)

if __name__ == "__main__":
    main()
