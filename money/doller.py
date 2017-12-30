from .money import Money

class Doller(Money):

    def __init__(self, amount: int):
        super().__init__(amount)
    
    def times(self, multiplier: int):
        return Doller(self.amount * multiplier)