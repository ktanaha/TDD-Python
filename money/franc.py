from .money import Money

class Franc(Money):

    def __init__(self, amount: int):
        super().__init__(amount)
    
    def times(self, multiplier: int):
        return Franc(self.amount * multiplier)