from Card import *

class Deck:
    def __init__(self):
        self.cards = []
        # make method to create the cards
        self.make_cards()

    # define method to create cards
    def make_cards(self):
        cards = []
        # for each value in card values it'll run once
        for value in card_values:
            # for each suit in suits it'll run 4 times
            for suit in suits:
                # if the value of the card is a head card or not
                if value in head_card:
                    _card = Card(head_card[value], suit)
                else:
                    _card = Card(value, suit)
                # add cards created into the cards list
                cards.append(_card)
        return cards
    
    def flipped(self):
        for card in self.cards:
            card.flipped()
deck = Deck()
deck.flipped()