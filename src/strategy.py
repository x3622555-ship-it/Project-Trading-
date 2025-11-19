import pandas as pd

class MovingAverageStrategy:
    def __init__(self):
        self.position = 0  # 0 = flat, 1 = long

    def on_bar(self, bar):  # bar is a pd.Series for a single timestamp
        short = bar['ma_short']
        long  = bar['ma_long']
        if pd.isna(short) or pd.isna(long):
            return None  # no signal
        if short > long and self.position == 0:
            self.position = 1
            return {'signal': 'BUY', 'size': 1}
        if short < long and self.position == 1:
            self.position = 0
            return {'signal': 'SELL', 'size': 1}
        return None
