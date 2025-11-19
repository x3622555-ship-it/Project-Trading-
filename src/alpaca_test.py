# src/alpaca_test.py
import os
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

load_dotenv()  # loads .env

API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_SECRET_KEY")
BASE_URL = os.getenv("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")

api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

def main():
    acct = api.get_account()
    print("Account status:", acct.status)
    print("Cash:", acct.cash)
    print("Equity:", acct.equity)
    print("Buying power:", acct.buying_power)

if __name__ == "__main__":
    main()
