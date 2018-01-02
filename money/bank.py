from .pair import Pair

class Bank(object):

    def __init__(self) -> None:
        self.rates = {}

    def reduce(self, source: 'Expression', to: str) -> 'Money':
        return source.reduce(self, to)

    def add_rate(self, frm: str, to: str, rate: int) -> None:
        pair = Pair(frm, to)
        self.rates[pair] = rate

    def rate(self, frm: str, to: str) -> int:
        pair = Pair(frm, to)
        return self.rates.get(pair, 1)