from Card import *
from random import *
from Player import *

class Deck:
    def __init__(self):
        self.cards = []
        self.mainDeck = self.cards
        self.card_values = Card.card_values
        self.head_card = Card.head_card
        self.suits = Card.suits
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
                self.mainDeck.append(_card)
    
    

    def shuffle(self):
        shuffled_deck = []
        for i in range(self.deckLength()):
            if self.deckLength() > 0:
                rand = randint(0, self.deckLength() -1)
                # list[i -> index]
                shuffled_deck.append(self.mainDeck[rand])
                self.mainDeck.remove(self.mainDeck[rand])
        self.mainDeck = shuffled_deck
        print(self.deckLength())
        
    def flipped(self):
        for card in self.mainDeck:
            card.flipped()
            
    def drawFromTop(self):
        return self.mainDeck.pop(0)
       
    def deckLength(self):
        return len(self.mainDeck)

    def addToDeck(self, card):
        self.mainDeck.append(card)


    def deal(self, numPlayers ):
        topCard = self.mainDeck.drawFromTop()
        topCard.addToDeck()
       
       
        pass
       
       
    #    help?? how to make it deal to X amt of players
        # for i in self.cards in range(0, 52, 2):
        #      self.hand.append()
        
        
      