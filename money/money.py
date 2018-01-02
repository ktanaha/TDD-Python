from .expression import Expression
from .sum import Sum

class Money(Expression):

    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def __eq__(self, other: 'Money') -> bool:
        return (self._amount == other._amount) and (self.currency() == other.currency())
    
    def times(self, multiplier: int) -> 'Money':
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: 'Money') -> 'Expression':
        return Sum(self, addend)
    
    def reduce(self, to: str) -> 'Money':
        return self

    def currency(self) -> str:
        return self._currency

    def amount(self) -> int:
        return self._amount

    @staticmethod
    def doller(amount: int) -> 'Money':
        return Money(amount, 'USD')
    
    @staticmethod
    def franc(amount: int) -> 'Money':
        return Money(amount, 'CHF')