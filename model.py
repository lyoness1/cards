"""Model for cards and decks"""

SUITS = {"S", "D", "C", "H"}
RANKS = {"A": [1, 14], "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
         "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}

class Card(object):

    def __init__(self, rank, suit):
        """Takes a rank and a suit as strings"""

        self.rank = rank
        self.suit = suit

    def __str__(self):
        return rank + suit

    def __repr__(self):
        return rank + suit

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit


class Deck(object):

    # A set - representing a deck - to store 52 Card objects
    deck = set()

    def __init__(self):
        """Makes 52 cards from each suit, rank. Adds Cards to deck set"""

        for suit in SUITS:
            for rank in RANKS:
                deck.add(Card(suit, rank))

    def __str__(self):
