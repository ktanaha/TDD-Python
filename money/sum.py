from .expression import Expression

class Sum(Expression):

    def __init__(self, augend: 'Money', addend: 'Money') -> None:
        self._augend = augend
        self._addend = addend

    def reduce(self, bank: 'Bank', to: str) -> 'Money':
        amount = self._augend.reduce(bank, to).amount() + self._addend.reduce(bank, to).amount()
        from .money import Money
        return Money(amount, to)

    def plus(self, addend: 'Expression') -> 'Expression':
        return Sum(self, addend)

    def times(self, multiplier: int) -> 'Expression':
        return Sum(self._augend.times(multiplier), self._addend.times(multiplier))
    
    def augend(self) -> 'Money':
        return self._augend

    def addend(self) -> 'Money':
        return self._addend

    