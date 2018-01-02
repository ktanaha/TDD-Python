from .expression import Expression

class Money(Expression):

    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def __eq__(self, other: 'Expression') -> bool:
        return (self._amount == other._amount) and (self.currency() == other.currency())

    def __str__(self) -> str:
        return 'amount = {0} currency = {1}'.format(str(self._amount), self._currency)
    
    def plus(self, addend: 'Expression') -> 'Expression':
        from .sum import Sum
        return Sum(self, addend)

    def times(self, multiplier: int) -> 'Expression':
        return Money(self._amount * multiplier, self._currency)
    
    def reduce(self, bank: 'Bank', to: str) -> 'Expression':
        rate = bank.rate(self._currency, to)
        return Money(self._amount / rate, to)

    def currency(self) -> str:
        return self._currency

    def amount(self) -> int:
        return self._amount

    @staticmethod
    def doller(amount: int) -> 'Expxression':
        return Money(amount, 'USD')
    
    @staticmethod
    def franc(amount: int) -> 'Expression':
        return Money(amount, 'CHF')