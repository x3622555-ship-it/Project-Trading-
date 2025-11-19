import pandas as pd

def prepare(infile='data/market_data.csv', outfile='data/market_data_clean.csv'):
    df = pd.read_csv(infile)

    # Ensure Datetime exists
    if 'Datetime' in df.columns:
        df['Datetime'] = pd.to_datetime(df['Datetime'])
        df.set_index('Datetime', inplace=True)

    # Convert all price/volume columns to numeric
    numeric_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Drop rows with missing data
    df.dropna(subset=numeric_cols, inplace=True)

    # Features
    df['return'] = df['Close'].pct_change().fillna(0)
    df['ma_short'] = df['Close'].rolling(5).mean()
    df['ma_long'] = df['Close'].rolling(20).mean()

    df.to_csv(outfile)
    print("Prepared:", outfile)

if __name__ == "__main__":
    prepare()
