# test_trade.py

import os
import logging
from alpaca_trade_api.rest import REST, APIError

# --- Hardcoded Alpaca paper trading keys ---
ALPACA_API_KEY = "PKWABPREA2FUMXWBOQXAQ34VDU"
ALPACA_SECRET_KEY = "B4Gus2fVEtdWPbB9kHGCT4u5jVTFtQA6e5Jb6PYWoAU"
ALPACA_BASE_URL = "https://paper-api.alpaca.markets"

# Check if keys are loaded
if not ALPACA_API_KEY or not ALPACA_SECRET_KEY or not ALPACA_BASE_URL:
    print("⚠️ API keys or BASE_URL not found. Check your hardcoded keys.")
    exit(1)

print("✅ API keys loaded successfully!")

# Set up logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/alpaca_client.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

orders_log = "logs/orders.log"
executions_log = "logs/executions.log"

# Alpaca REST API object
api = REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, base_url=ALPACA_BASE_URL)

# Trading parameters
symbol = "AAPL"
qty = 1

try:
    # Submit a buy order only
    buy_order = api.submit_order(
        symbol=symbol,
        qty=qty,
        side="buy",
        type="market",
        time_in_force="day"
    )
    print(f"Buy order submitted: {buy_order.id}")
    logging.info(f"Buy order submitted: {buy_order}")
    with open(orders_log, "a") as f:
        f.write(f"Buy order submitted: {buy_order}\n")

except APIError as e:
    print("Error with Alpaca API:", e)
    logging.error(f"Alpaca API error: {e}")
    with open(executions_log, "a") as f:
        f.write(f"Alpaca API error: {e}\n")
