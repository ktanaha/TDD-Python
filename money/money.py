from abc import ABCMeta, abstractmethod

class Money(metaclass=ABCMeta):

    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def __eq__(self, other: 'Money') -> bool:
        return (self._amount == other._amount) and ( self.__class__.__name__ == other.__class__.__name__)
    
    @abstractmethod
    def times(multiplier: int) -> 'Money':
        pass
    
    def currency(self) -> str:
        return self._currency

    @staticmethod
    def doller(amount: int) -> 'Money':
        from .doller import Doller
        return Doller(amount, 'USD')
    
    @staticmethod
    def franc(amount: int) -> 'Money':
        from .franc import Franc
        return Franc(amount, 'CHF')