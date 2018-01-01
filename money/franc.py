from .money import Money

class Franc(Money):

    def __init__(self, amount: int) -> None:
        super().__init__(amount, 'CHF')
    
    def times(self, multiplier: int) -> 'Money':
        return Money.franc(self.amount * multiplier)