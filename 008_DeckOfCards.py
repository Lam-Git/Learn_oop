import random


# https://github.com/eli-byers/Deck-Of-Cards-Python/blob/master/deckofcards.py


class Card(object):  # blueprint (Card Class)
    def __init__(self, suit, val):  # instance attributes
        self.suit = suit
        self.val = val

    def show(self):  # instance method and it help print out the card and value
        print(f"{self.suit} of {self.val}.")


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()  # this function is to call the #def build instant method

    def build(self):  # instance method will build the deck in order
        for s in ["Spades", "Clubs", "Diamonds", "Heats"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):  # print out the deck your calling
        for c in self.cards:
            c.show()

    def shuffle(self):  # instance method for shuffle
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHands(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()


deck = Deck()  # instance object
# deck.shuffle()
# deck.show()
# deck.build() #we can call any of the instance
# deck.show()

lam = Player("Lam")  # instance object
lam.draw(deck).draw(deck)
lam.showHands()
