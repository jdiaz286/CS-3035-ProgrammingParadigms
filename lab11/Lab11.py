import random

# ranks: 2,3,4,5,6,7,8,9,10,J,Q,K,A
# suits: clubs, diamonds, hearts, spades
# values: 2-14
# key numbers: 1-52


class Deck:
    # default constructor
    def __init__(self):
        # 'cards' will be represented by empty list
        self.cards = []
        # fill the empty list of 'cards'
        self.fillDeck()
        self.shuffleDeck()

    # helper method to fill deck of cards
    def fillDeck(self):
        # number that keeps track of id of card
        keyNumber = 0
        # loop through each suit
        for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
            # loop through values 2 through 14 (inclusive)
            for value in range(2, 15):
                # increment the key identifier
                keyNumber = keyNumber+1
                # if value = 11 then give card 'rank' = 'jack'
                if(value == 11):
                    self.cards.append(Card('Jack', suit, value, keyNumber))
                # if value = 12 then give card 'rank' = 'queen'
                elif(value == 12):
                    self.cards.append(Card('Queen', suit, value, keyNumber))
                # if value = 13 then give card 'rank' = 'king'
                elif(value == 13):
                    self.cards.append(Card('King', suit, value, keyNumber))
                # if value = 14 then give card 'rank' = 'ace'
                elif(value == 14):
                    self.cards.append(Card('Ace', suit, value, keyNumber))
                # if card not unique then just 'rank' same value as 'value'
                else:
                    self.cards.append(Card(value, suit, value, keyNumber))

    # helper method just to show all values have been obtained in the deck
    def showDeckInfo(self):
        # loop through all cards
        for c in self.cards:
            # print the stats of the cards
            print('rank: {0}, suit: {1}, value: {2}, keyNumber: {3}'.format(
                c.rank, c.suit, c.value, c.keyNumber))

    # A method that draws a card from the deck (returns a card)
    def getCard(self):
        if(self.isDeckEmpty() == False):
            # save the index to delete later
            indexToGet = random.randint(0, len(self.cards)-1)
            # save the instance of the card that is 'selected'
            cardToReturn = self.cards[indexToGet]
            # delete the card at correct index to avoid duplicates
            del self.cards[indexToGet]
            # return the card that was 'selected'
            return cardToReturn
        else:
            print("There are no more cards in the list")
            exit()

    # A method that returns whether or not the deck is empty
    def isDeckEmpty(self):
        # if 'self.cards' length is 0 then it is empty, return True
        if(len(self.cards) == 0):
            return True
        # if not then return False
        else:
            return False

    # A method that shuffles the deck
    def shuffleDeck(self):
        # use shuffle() from random to 'shuffle' deck
        random.shuffle(self.cards)

    # A method that resets the deck (creates a new list of cards and shuffles them)
    def resetAndShuffleDeck(self):
        # create a blank instance of the cards
        self.cards = []
        # use previously created method to fill deck
        self.fillDeck()
        # use previously created method to shuffle deck
        self.shuffleDeck()


class Card:
    # instantiates all parts of the card needed (rank, suit, value, keyNumber)
    def __init__(self, rank, suit, value, keyNumber):
        self.rank = rank
        self.suit = suit
        self.value = value
        self.keyNumber = keyNumber


# int to track how many games are played
gamesPlayed = 0

# deck that is used between both players
deck = Deck()

# variable to keep track of the score of the user
p1Score = 0
p2Score = 0

while(gamesPlayed < 5 and deck.isDeckEmpty()==False):
    # get the first players card and print result
    p1CurrentCard = deck.getCard()
    print("\nPlayer 1 plays a "+str(p1CurrentCard.rank) +
          " of "+str(p1CurrentCard.suit))

    # get the second players card and print result
    p2CurrentCard = deck.getCard()
    print("Player 2 plays a "+str(p2CurrentCard.rank) +
          " of "+str(p2CurrentCard.suit))

    # save the amount of points that are at stake
    pointsWon = p1CurrentCard.value + p2CurrentCard.value

    # check to see who has the highest card and give the user the points
    if(p1CurrentCard.value > p2CurrentCard.value):
        print("Player 1 Wins!")
        p1Score += pointsWon
    elif(p1CurrentCard.value < p2CurrentCard.value):
        print("Player 2 Wins!")
        p2Score += pointsWon
    else:
        print("Draw, no players win points")

    # show the amount of points each player has
    print("Player 1 score: "+str(p1Score))
    print("Player 2 score: "+str(p2Score)+"\n")

    # increment the number of gamesPlayed
    gamesPlayed += 1

print("\nGame Over!")
print("Final Score:")
print("Player 1 score: "+str(p1Score))
print("Player 2 score: "+str(p2Score))
# if player 1 has more points then state player 1 won
if(p1Score > p2Score):
    print("Player 1 wins the game!")

# if player 2 has more points then state player 2 won
elif(p2Score > p1Score):
    print("Player 2 wins the game!")

# if both points are equal then say that both players tied
else:
    print("Both players have tied")
print()
