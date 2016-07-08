"""Model for cards and decks"""

from random import shuffle

SUITS = {"S": 4, "D": 3, "C": 2, "H": 1}
RANKS = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
         "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}

class Card(object):

    def __init__(self, rank, suit):
        """Takes a rank and a suit as strings"""

        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + self.suit

    def __repr__(self):
        return self.rank + self.suit

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit


class Deck(object):

    # instatiates a list - representing a deck - to store 52 Card objects
    _deck = []

    def __init__(self):
        """Makes 52 cards from each suit, rank. Adds Cards to deck list"""

        for suit in SUITS:
            for rank in RANKS:
                self._deck.append(Card(rank, suit))

    def __repr__(self):
        return str(self._deck)

    def __iter__(self):
        return iter(self._deck)

    def shuffle(self):
        return shuffle(self._deck)
