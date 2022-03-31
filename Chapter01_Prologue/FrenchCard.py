#/usr/bin/python3
import collections
from random import choice

# use "namedtuple" to create a tiny class
Card = collections.namedtuple('Card', ['rank', 'suit'])

# create a class based on Card.
# overwrite some special methods: 
#       __len__, __getitem__
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

# create french deck siut and check it's length
dk = FrenchDeck()
print(len(dk))

# add size compare
# assign values to each 'suit' in frenchdeck class
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    print('rank value: ', rank_value)
    return rank_value * len(suit_values) + suit_values[card.suit]

rand_a = choice(dk)
rand_b = choice(dk)
print(rand_a, " > ", rand_b, rand_a > rand_b)

# __getitem__ right now is immutable. 
# To change it mutable/random, use this below to overwrite __getitem__ (from Chapter 11)
