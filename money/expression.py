class Expression(object):

    def plus(self, addend: 'Money') -> 'Expression':
        pass

    def reduce(self, bank: 'Bank', to: str) -> 'Money':
        pass