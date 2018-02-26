# This class is the data structure used for cards.
class Card:

    ranks = {'A': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12 }
    suits = {'C': 0, 'D': 1, 'S': 2, 'H': 3}

    def __init__(self, rank, suit):
        # Assign rank
        if type(rank) == str:
            self.rank = ranks[rank]
        else:
            if rank < 0 or rank > 12:
                raise ValueError
            self.rank = rank

        # Assign suit
        if type(suit) == str:
            self.suit = suits[suit]
        else:
            if suit < 0 or suit > 3:
                raise ValueError
            self.suit = suit

    def __init__(self, id):
        self.rank = id % 13
        self.suit = int(id / 13)

    def get():
        return (self.rank, self.suit)

    def getRank():
        return self.rank

    def getSuit():
        return self.suit

    def getid():
        return self.suit * 13 + self.rank
