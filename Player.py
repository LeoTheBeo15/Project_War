from Deck import *


class Player:

    def  __init__(self):
        self.hand = Deck()
        self.winningHand = Deck()

    def showHand(self):
         self.hand.flipped()

    def getHand(self):
            return self.hand
    # need input for number of players?