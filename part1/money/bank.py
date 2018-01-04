class Bank(object):

    def __init__(self) -> None:
        self._rates = {}

    def reduce(self, source: 'Expression', to: str) -> 'Money':
        return source.reduce(self, to)

    def add_rate(self, frm: str, to: str, rate: int) -> None:
        self._rates[(frm, to)] = rate

    def rate(self, frm: str, to: str) -> int:
        return 1 if frm == to else self._rates.get((frm, to))