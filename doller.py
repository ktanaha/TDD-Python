import money

class Doller(money.Money):

    def __init__(self, amount):
        super().__init__(amount)
    
    def times(self, multiplier):
        return Doller(self.amount * multiplier)