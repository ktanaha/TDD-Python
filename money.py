class Money:
    
    def __init__(self, amount):
        self.amount = amount
    
    def get_amount(self):
        return self.amount

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount
        else:
            return False
