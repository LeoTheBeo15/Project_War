class Card:
    card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    suits = ["clubs", "diamonds", "hearts", "spades"]

    # dictionary for the head cards and values
    head_card = {
        "Jack" : 11,
        "Queen" : 12,
        "King" : 13,
        "Ace" : 14,
        11 : "Jack",
        12 : "Queen",
        13 : "King",
        14 : "Ace"
    }
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # prints out the face and suit once flipped
    def flipped(self):
        print(f"{self.value} of {self.suit}")