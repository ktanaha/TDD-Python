class Bank(object):

    def reduce(self, expression: 'Expression', to: str) -> 'Money':
        from .money import Money
        return Money.doller(10)