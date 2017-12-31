class Money(object):

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def __eq__(self, other: "Money") -> bool:
        return (self.amount == other.amount) and ( self.__class__.__name__ == other.__class__.__name__)