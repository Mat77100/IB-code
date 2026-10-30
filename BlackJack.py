#blackjack 30/10/2026
import random #Yes okay its not random, but close enough


S_Deck = [1,2,3,4,5,6,7,8,9,10,11,12,13] #1 = Ace, 11 = jack, 12 = queen, 13 = king. so i can do A==B without issue of str == int
C_Deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]
H_Deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]
D_Deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]#Global?

FullDeck = [S_Deck,C_Deck,H_Deck,D_Deck]

class Players:
    def __init__(self):
        self.Hand = {}

    def DrawCard(self):
        NewCard = random.randint(1,13)
        NewCardSuit = random.randint(1,4)

        # 1 = Spades
        # 2 = Hearts
        # 3 = Clubs
        # 4 = Diamonds

        DrawnCard = (NewCard,NewCardSuit)

        if not (DrawnCard in self.Hand):
        

    


#def GameRound(Deck,Money):
