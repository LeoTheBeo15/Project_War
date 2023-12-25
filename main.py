from Deck import *
from Player import *
from Game import *
"""
Test code below
"""
deck = Deck()
# deck.flipped()
war = War()

deck.shuffle()
# deck.flipped()

# card = deck.drawFromTop()
# card.flipped()
# deck.deckLength()


deck.deal(war.getPlayers())
for player in war.getPlayers():
    player.showHand()