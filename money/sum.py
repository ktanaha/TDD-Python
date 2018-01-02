from .expression import Expression

class Sum(Expression):

    def __init__(self, augend: 'Money', addend: 'Money') -> None:
        self._augend = augend
        self._addend = addend

    def reduce(self, to: str) -> 'Money':
        amount = self._augend.amount() + self._addend.amount()
        from .money import Money
        return Money(amount, to)

    def augend(self) -> 'Money':
        return self._augend

    def addend(self) -> 'Money':
        return self._addend

    