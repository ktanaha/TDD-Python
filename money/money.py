from abc import ABCMeta, abstractmethod

class Money(metaclass=ABCMeta):

    def __init__(self, amount: int, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __eq__(self, other: 'Money') -> bool:
        return (self.amount == other.amount) and ( self.__class__.__name__ == other.__class__.__name__)
    
    @abstractmethod
    def times(multiplier: int) -> 'Money':
        pass
    
    def get_currency(self) -> str:
        return self.currency

    @staticmethod
    def doller(amount: int) -> 'Money':
        from .doller import Doller
        return Doller(amount)
    
    @staticmethod
    def franc(amount: int) -> 'Money':
        from .franc import Franc
        return Franc(amount)