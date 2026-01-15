import os
import requests
import psycopg2
import logging
from psycopg2.extras import execute_batch
from datetime import datetime
from decimal import Decimal
from dotenv import load_dotenv

# ===============================
# Logging Configuration
# ===============================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("ingestion.log")
    ]
)

logger = logging.getLogger(__name__)

# ===============================
# Load environment variables
# ===============================
load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

# ===============================
# CoinGecko API config
# ===============================
COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 100,
    "page": 1
}

# ===============================
# Database helpers
# ===============================
def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def get_latest_prices(cursor):
    cursor.execute("""
        SELECT coin_id, current_price_usd
        FROM current_prices;
    """)
    return dict(cursor.fetchall())

# ===============================
# API fetch
# ===============================
def fetch_prices():
    response = requests.get(COINGECKO_URL, params=PARAMS, timeout=30)
    response.raise_for_status()
    return response.json()

# ===============================
# Main ingestion logic
# ===============================
def ingest():
    logger.info("Starting CoinGecko ingestion run")

    try:
        conn = get_connection()
        cur = conn.cursor()

        latest_prices = get_latest_prices(cur)
        api_data = fetch_prices()

        history_rows = []
        current_rows = []

        for coin in api_data:
            coin_id = coin["id"]
            symbol = coin["symbol"]
            name = coin["name"]

            price = Decimal(str(coin["current_price"]))
            market_cap = coin["market_cap"]
            volume = coin["total_volume"]

            last_updated = datetime.fromisoformat(
                coin["last_updated"].replace("Z", "")
            )

            old_price = latest_prices.get(coin_id)

            # -------------------------------
            # CDC: price-based change detection
            # -------------------------------
            if old_price is None:
                price_changed = True
            else:
                price_changed = abs(price - old_price) / old_price >= Decimal("0.001")

            if price_changed:
                history_rows.append((
                    coin_id,
                    symbol,
                    price,
                    market_cap,
                    volume,
                    last_updated
                ))

            current_rows.append((
                coin_id,
                symbol,
                name,
                price,
                market_cap,
                volume,
                last_updated
            ))

        # Insert history
        if history_rows:
            execute_batch(cur, """
                INSERT INTO price_history (
                    coin_id,
                    symbol,
                    price_usd,
                    market_cap_usd,
                    total_volume_usd,
                    last_updated
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (coin_id, last_updated) DO NOTHING;
            """, history_rows)

        # Upsert current prices
        if current_rows:
            execute_batch(cur, """
                INSERT INTO current_prices (
                    coin_id,
                    symbol,
                    coin_name,
                    current_price_usd,
                    market_cap_usd,
                    total_volume_usd,
                    last_updated
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (coin_id) DO UPDATE SET
                    symbol = EXCLUDED.symbol,
                    coin_name = EXCLUDED.coin_name,
                    current_price_usd = EXCLUDED.current_price_usd,
                    market_cap_usd = EXCLUDED.market_cap_usd,
                    total_volume_usd = EXCLUDED.total_volume_usd,
                    last_updated = EXCLUDED.last_updated,
                    ingestion_time = CURRENT_TIMESTAMP;
            """, current_rows)

        conn.commit()

        logger.info(
            "Ingestion complete | history_inserted=%s | current_upserted=%s",
            len(history_rows),
            len(current_rows)
        )

    except Exception as e:
        logger.exception("Ingestion failed due to error")
        raise

    finally:
        if "cur" in locals():
            cur.close()
        if "conn" in locals():
            conn.close()

        logger.info("Database connection closed")

# ===============================
# Entry point
# ===============================
if __name__ == "__main__":
    ingest()
