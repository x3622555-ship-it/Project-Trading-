import yfinance as yf
import pandas as pd

def download_1min(ticker='AAPL', period='7d', out='data/market_data.csv'):
    data = yf.download(tickers=ticker, period=period, interval='1m')
    data = data[['Open','High','Low','Close','Volume']]
    data.index.name = 'Datetime'
    data.reset_index().to_csv(out, index=False)
    print("Saved", out)

if __name__ == "__main__":
    download_1min()
