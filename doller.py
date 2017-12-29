class Doller:

    def __init__(self, amount):
        self.amount = amount
    
    def times(self, multiplier):
        self.amount *= multiplier

    def get_amount(self):
        return self.amount
