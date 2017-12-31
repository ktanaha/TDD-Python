from abc import ABCMeta, abstractmethod

class Money(metaclass=ABCMeta):

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def __eq__(self, other: "Money") -> bool:
        return (self.amount == other.amount) and ( self.__class__.__name__ == other.__class__.__name__)
    
    def times(multiplier: int) -> "Money":
        pass
        
    @staticmethod
    def doller(amount: int) -> "Money":
        from .doller import Doller
        return Doller(amount)
    
    @staticmethod
    def franc(amount: int) -> "Money":
        from .franc import Franc
        return Franc(amount)