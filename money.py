class Money:
    
    def __init__(self, amount):
        self.amount = amount
    
    def get_amount(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount and self.__class__.__name__ == other.__class__.__name__