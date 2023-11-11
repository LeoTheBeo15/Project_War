from Card import *
from random import *

class Deck:
    def __init__(self):
        self.cards = []
        self.card_values = Card.card_values
        self.head_card = Card.head_card
        self.suits = Card.suits
        # make method to create the cards
        self.make_cards()

    # define method to create cards
    def make_cards(self):
        # for each value in card values it'll run once
        for value in self.card_values:
            # for each suit in suits it'll run 4 times
            for suit in self.suits:
                # if the value of the card is a head card or not
                if value in self.head_card:
                    _card = Card(suit, self.head_card[value])
                else:
                    _card = Card(suit, value)
                # add cards created into the cards list
                self.cards.append(_card)
    
    

    def shuffle(self):
        shuffled_deck = []
        for i in range(len(self.cards)):
            if len(self.cards) > 0:
                rand = randint(0, len(self.cards) -1)
                # list[i -> index]
                shuffled_deck.append(self.cards[rand])
                self.cards.remove(self.cards[rand])
        self.cards = shuffled_deck
        print(len(self.cards))
        
    def flipped(self):
            for card in self.cards:
                card.flipped()
            