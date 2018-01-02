from .expression import Expression

class Money(Expression):

    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def __eq__(self, other: 'Money') -> bool:
        return (self._amount == other._amount) and (self.currency() == other.currency())
    
    def times(self, multiplier: int) -> 'Money':
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: 'Money') -> 'Expression':
        return Money(self._amount + addend._amount, self._currency)
    
    def currency(self) -> str:
        return self._currency

    @staticmethod
    def doller(amount: int) -> 'Money':
        return Money(amount, 'USD')
    
    @staticmethod
    def franc(amount: int) -> 'Money':
        return Money(amount, 'CHF')