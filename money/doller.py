from .money import Money

class Doller(Money):

    def __init__(self, amount: int) -> None:
        super().__init__(amount, 'USD')
    
    def times(self, multiplier: int) -> 'Money':
        return Money.doller(self.amount * multiplier)