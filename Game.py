from Player import *
from Deck import *


class War:

    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.players = [self.player1, self.player2]
        self.numPlayers = len(self.players)
    
    def getPlayers(self):
        return self.players

    

    
    
    
    














    
"""
amt of players, 
create 2 lists for every player (hand, winning hand)
deal 1 by 1 to however many players to hand

flip top card, index 1 in hand list
add to table list
remove from hand lists
compare values
add to winners hand
remove from table list
repeat until war or hand is empty



war: cards put down need to be stored in table list
compare values of index of 6 and 10


"""