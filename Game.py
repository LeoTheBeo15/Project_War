from Player import *
from Deck import *


class War:

    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.players = [self.player1, self.player2]
        self.numPlayers = len(self.players)
        # want table to be a list bc the order matters for war (maybe)
        self.table = Deck()
    
    def getPlayers(self):
        return self.players

    def compare(self):
        if self.table.index(max(self.table)) == 0:
            self.player1.getWinningHand().addToDeck(self.table)
        else:
            self.player2.getWinningHand().addToDeck(self.table)

        """
        needs to take a card from each players hand and put it in the table
        compare card values, card from index 0 or 1
        max and index function
        """

    def switchHands(self):
        """
        need to shuffle winning deck before switching hands
        can't be a for loop because it won't make sense
        needs an if statement
        need to find a way for player to be defined so i can get the hands
        """
        player.



    def play(self):
        # needs a while loop of some sort so it continues until one player's hands are empty
        while player.getHand().isEmpty() & player.getWinningHand().isEmpty() == False:
        
        
        for player in self.players:
            # gets hand, takes card from top, adds to table
            player.getHand().drawFromTop().addToDeck(self.table) 

    
    
    
    














    
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