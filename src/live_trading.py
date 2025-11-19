# src/live_trading.py

import time
import pandas as pd
from alpaca_client import submit_market_order, get_account
from strategy import MovingAverageStrategy

# Load your cleaned market data (or stream in real-time later)
df = pd.read_csv("data/market_data_clean.csv", parse_dates=["Datetime"])
df.set_index("Datetime", inplace=True)

symbol = "AAPL"
strat = MovingAverageStrategy()

print("Starting LIVE PAPER TRADING with Alpaca...")

# Loop over each new bar (simulate real-time)
for ts, bar in df.iterrows():
    signal = strat.on_bar(bar)

    if signal:
        side = signal["signal"].lower()
        qty = signal.get("size", 1)

        # Get account info safely
        acct = get_account()

        if acct and acct.status == "ACTIVE":
            print(f"[{ts}] Sending {side.upper()} order for {qty} share(s) of {symbol}")
            result = submit_market_order(symbol, qty, side)

            if result:
                print("Order submitted:", result)
            else:
                print("Order FAILED — check logs")
        else:
            print("Account not active or not accessible.")

    # Simulate 1-minute delay (remove if using real API streaming)
    time.sleep(0.2)

print("Live trading simulation complete.")
