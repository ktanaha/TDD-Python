from .pair import Pair

class Bank(object):

    def __init__(self) -> None:
        self.rates = {}

    def reduce(self, source: 'Expression', to: str) -> 'Money':
        return source.reduce(self, to)

    def add_rate(self, frm: str, to: str, rate: int) -> None:
        self.rates[Pair(frm, to)] = rate

    def rate(self, frm: str, to: str) -> int:
        return self.rates.get(Pair(frm, to), 1)