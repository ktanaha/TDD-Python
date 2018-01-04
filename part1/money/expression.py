class Expression(object):

    def plus(self, addend: 'Expression') -> 'Expression':
        pass

    def reduce(self, bank: 'Bank', to: str) -> 'Expression':
        pass