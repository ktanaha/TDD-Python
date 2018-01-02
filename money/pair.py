class Pair():

    def __init__(self, frm: str, to: str):
        self.frm = frm
        self.to = to

    def __eq__(self, other: 'Pair') -> bool:
        return (self.frm == other.frm) and (self.to == other.to)
    
    def __hash__(self) -> hash:
        return hash(self.frm + self.to)