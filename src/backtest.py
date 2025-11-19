from gateway import Gateway
from strategy import MovingAverageStrategy
from order_manager import OrderManager
from matching_engine import MatchingEngine

def run_backtest(datafile):
    gw = Gateway(datafile)
    strat = MovingAverageStrategy()
    om = OrderManager()
    me = MatchingEngine()

    equity = []
    timestamps = []

    for ts, bar in gw.stream():
        # 1) strategy generates signal
        signal = strat.on_bar(bar)
        price = bar['Close']
        if signal:
            order = om.validate_and_send(ts, signal, price)
            if order:
                fill = me.match(order)
                if fill:
                    om.on_fill(fill)

        # record equity = cash + position * price
        net = om.cash + om.position * price
        equity.append(net)
        timestamps.append(ts)

    # save equity curve
    import pandas as pd
    df = pd.DataFrame({'ts':timestamps,'equity':equity})
    df.to_csv('outputs/equity_curve.csv', index=False)
    print("Backtest complete. Equity saved to outputs/equity_curve.csv")

if __name__ == "__main__":
    run_backtest('data/market_data_clean.csv')
