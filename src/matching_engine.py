import random
import json

class MatchingEngine:
    def __init__(self, fill_prob=0.9):
        self.fill_prob = fill_prob
        self.exec_log = 'logs/executions.log'

    def match(self, order):
        r = random.random()
        if r < self.fill_prob:
            # full fill
            fill = {'ts':order['ts'],'side':order['side'],'price':order['price'],'size':order['size']}
            self._log(fill)
            return fill
        else:
            # rejected or cancelled
            return None

    def _log(self, fill):
        with open(self.exec_log, 'a') as f:
            f.write(json.dumps(fill) + '\n')
