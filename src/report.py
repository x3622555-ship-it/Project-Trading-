import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def simple_report(equity_csv='outputs/equity_curve.csv'):
    df = pd.read_csv(equity_csv)
    df['equity_return'] = df['equity'].pct_change().fillna(0)
    total_return = df['equity'].iloc[-1] / df['equity'].iloc[0] - 1
    volatility = df['equity_return'].std() * (252**0.5)  # rough
    sharpe = (df['equity_return'].mean() * 252) / (volatility + 1e-9)

    print("Total Return:", total_return)
    print("Annualized Volatility (approx):", volatility)
    print("Sharpe (approx):", sharpe)

    plt.plot(pd.to_datetime(df['ts']), df['equity'])
    plt.title('Equity Curve')
    plt.xlabel('Time')
    plt.ylabel('Equity')
    plt.tight_layout()
    plt.savefig('outputs/equity_curve.png')
    print("Plot saved to outputs/equity_curve.png")

if __name__ == "__main__":
    simple_report()
