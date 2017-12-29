class Franc:

    def __init__(self, amount):
        self.amount = amount
    
    def times(self, multiplier):
        return Franc(self.amount * multiplier)

    def get_amount(self):
        return self.amount

    def __eq__(self, other):
        franc = other
        if isinstance(franc, Franc):
            return self.amount == franc.amount
        else:
            return False