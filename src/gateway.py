import pandas as pd
import time

class Gateway:
    def __init__(self, infile):
        self.df = pd.read_csv(infile, parse_dates=['Datetime'], index_col='Datetime')

    def stream(self):
        for ts, row in self.df.iterrows():
            yield ts, row  # consumer will process this
            # optional: time.sleep(0.01)  # don't use in backtest; for demo only
