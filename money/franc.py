from .money import Money

class Franc(Money):

    def __init__(self, amount: int) -> None:
        super().__init__(amount)
    
    def times(self, multiplier: int) -> int:
        return Franc(self.amount * multiplier)