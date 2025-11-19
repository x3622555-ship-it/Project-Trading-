import json
from datetime import datetime

class OrderManager:
    def __init__(self, cash=100000):
        self.cash = cash
        self.position = 0
        self.order_log = 'logs/orders.log'

    def validate_and_send(self, ts, signal, price):
        # very simple checks: enough cash for buy of size 1 at price
        size = signal.get('size', 1)
        if signal['signal'] == 'BUY':
            cost = price * size
            if cost > self.cash:
                return None  # reject
            order = {'ts': str(ts), 'side':'BUY','price':price,'size':size}
            self._log(order)
            return order
        elif signal['signal'] == 'SELL':
            if self.position <= 0:
                return None
            order = {'ts': str(ts), 'side':'SELL','price':price,'size':size}
            self._log(order)
            return order

    def on_fill(self, fill):
        # update cash and position
        if fill['side'] == 'BUY':
            self.position += fill['size']
            self.cash -= fill['price'] * fill['size']
        else:
            self.position -= fill['size']
            self.cash += fill['price'] * fill['size']

    def _log(self, order):
        with open(self.order_log, 'a') as f:
            f.write(json.dumps(order) + '\n')
