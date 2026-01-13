import logging
from pathlib import Path
from src.ingest import ingest_data
from src.validate import validate_data
from src.config import setup_logging
import json

def main():
    setup_logging()
    logging.info("Pipeline started")

    df = ingest_data()
    logging.info(f"Ingested {len(df)} records")

    valid_df, rejected_df = validate_data(df)
    logging.info(f"Valid records: {len(valid_df)}")
    logging.info(f"Rejected records: {len(rejected_df)}")

    rejected_path = Path("data/rejected/rejected_records.csv")
    rejected_path.parent.mkdir(exist_ok=True)
    rejected_df.to_csv(rejected_path, index=False)
    logging.info(f"Rejected records saved to {rejected_path}")

    logging.info("Pipeline finished successfully")




    quality_report = {
    "total_records": len(df),
    "valid_records": len(valid_df),
    "rejected_records": len(rejected_df),
    "rejection_rate": round(len(rejected_df) / len(df), 2),
    }

    report_path = Path("data/processed/data_quality_report.json")
    report_path.parent.mkdir(exist_ok=True)
    with open(report_path, "w") as f:
        json.dump(quality_report, f, indent=4)

    logging.info(f"Data quality report saved to {report_path}")

if __name__ == "__main__":
   main()

