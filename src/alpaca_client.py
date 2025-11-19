# src/alpaca_client.py
import os, logging
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from typing import Optional

load_dotenv()

API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_SECRET_KEY")
BASE_URL = os.getenv("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")

api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

logging.basicConfig(filename='logs/alpaca_client.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

def get_account():
    try:
        return api.get_account()
    except Exception as e:
        logging.exception("Failed to get account")
        raise

def submit_market_order(symbol: str, qty: int, side: str = 'buy', time_in_force: str = 'day') -> Optional[dict]:
    """Submit a MARKET order. side: 'buy' or 'sell'."""
    try:
        order = api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type='market',
            time_in_force=time_in_force
        )
        logging.info(f"Submitted market order: {order}")
        return order._raw  # raw dict
    except Exception as e:
        logging.exception("Order submission failed")
        return None

def submit_limit_order(symbol: str, qty: int, limit_price: float, side: str = 'buy', time_in_force: str = 'day') -> Optional[dict]:
    try:
        order = api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type='limit',
            time_in_force=time_in_force,
            limit_price=str(limit_price)
        )
        logging.info(f"Submitted limit order: {order}")
        return order._raw
    except Exception as e:
        logging.exception("Limit order submission failed")
        return None

def get_position(symbol: str):
    try:
        return api.get_position(symbol)
    except Exception:
        return None

def close_all_positions():
    try:
        resp = api.close_all_positions()
        logging.info("Close all positions response: %s", resp)
        return resp
    except Exception:
        logging.exception("Failed to close positions")
        return None
