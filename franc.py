import money

class Franc(money.Money):

    def __init__(self, amount):
        super().__init__(amount)
    
    def times(self, multiplier):
        return Franc(self.amount * multiplier)