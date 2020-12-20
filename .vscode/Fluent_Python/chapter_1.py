import collections

Card = collections.namedtuple('Card',['rank','suit'])

class FrechDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self,position):
        return self._cards[position]

beer_card = Card('7','diamonds')
print(beer_card)

def my_function:
    pass