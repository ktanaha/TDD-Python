class Doller:

    def __init__(self, amount):
        self.amount = amount
    
    def times(self, multiplier):
        return Doller(self.amount * multiplier)

    def get_amount(self):
        return self.amount

    def __eq__(self, other):
        doller = other
        if isinstance(doller, Doller):
            return self.amount == doller.amount
        else:
            return False