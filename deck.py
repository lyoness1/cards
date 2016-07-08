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

    def __repr__(self):
        """Returns a readable version of the card, ex: AH for Ace of Hearts"""
        return self.rank + self.suit

    def __cmp__(self, other):
        """Compares the values of the cards' ranks. Aces low, ATM"""
        return cmp(RANK[self.rank], RANK[other.rank])

    def get_rank(self):
        """Returns card's rank"""
        return self.rank

    def get_suit(self):
        """Returns card's suit"""
        return self.suit


class Deck(object):
    def __init__(self):
        """Makes 52 cards from each suit, rank. Adds Cards to cards list"""
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(rank, suit))

    def __repr__(self):
        """Returns a list of cards values in the deck"""
        return str(self.cards)

    def __iter__(self):
        """Iterates over the list of cards in the deck"""
        return iter(self.cards)

    def shuffle(self):
        """Randomly orders the cards in the deck"""
        return shuffle(self.cards)

    def add_card(self, card):
        """Adds a specific card to the deck

        card: string representation of card, ex: 'AH'
        """
        self.cards.append(card)

    def remove_card(self, card):
        """Removes a specific card from the deck

        card: string representation of card, ex: 'AH'
        """
        self.cards.remove(card)

    def pop_card(self, i=-1):
        """Removes and returns a card from the deck. By default, top card"""
        return self.cards.pop(i)

    def sort_cards(self):
        """Sorts the cards by suit, rank"""
        self.cards.sort()

    def deal_cards(self, hand, num):
        """deals num cards from deck into hand

        hand: destination Hand object
        num: number of cards to be dealt
        """
        for i in range(num):
            hand.add_card(self.pop_card())


# Hand inherits from Deck because it has similar behaviors
class Hand(Deck):
    def __init__(self, player=""):
        """Creates a list to store cards, assigns a player to the hand"""
        self.cards = []
        self.player = player
