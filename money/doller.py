from .money import Money

class Doller(Money):

    def __init__(self, amount: int) -> None:
        super().__init__(amount)
    
    def times(self, multiplier: int) -> "Doller":
        return Doller(self.amount * multiplier)