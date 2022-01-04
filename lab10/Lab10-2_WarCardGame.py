""" Lab 10: Part 2: War Card Game [10 POINTS] """

"""
In this assignment, you are going to write a command line card game of War (see
https://youtu.be/G4DhzhDlXFM and/or https://en.wikipedia.org/wiki/War_(card_game) for
the game). For simiplification, assume that the deck of cards just has numbers
from 1 to 10 (no repeats) in it. Please implement the game in three steps as follows.

Note: Do NOT define ANY functions in your implementation.

Please do all of these in Python 3, NOT Python 2. Your submitted file MUST be compilable
(i.e. NO compiling errors) in Python 3, otherwise you will get ZERO.
If you have some uncompilable code, I recommend COMMENTing them.

After writing your code, please play the game to test your implementation.
The testing procedure is as follows:
-- Open a command prompt and locate to the directory/folder of THIS script/file.
-- In the command prompt, type $python THISFILENAME.py$ OR $python3 THISFILENAME.py$ to
    run the script, then you can play the game.

This video (https://calstatela.zoom.us/rec/share/uIcKncpEt8rvakCv35XKGEnMD8BLA21CpLFmYp8sJJeItDljIRdTjY06DiHveSDB.Pda6RN2vVGCY5CH0?startTime=1604017135000)
illustrates a play round of my implementation. You may take it as a reference.
"""


# Please do NOT DELETE nor CHANGE the following line.
# It is used to import the random module which pre-defines functions to generate
#   pseudo-random numbers (https://docs.python.org/3/library/random.html).
# You need it in Step 1.
import random

"""
Step 1 [2.5 POINTS]:
Create two player variable scores, and a deck of cards for each player.
Each deck has 10 cards. Shuffle the decks.

Hint: Use random.shuffle(your_deck) to shuffle in place

Note: Do NOT define ANY functions in your implementation.
"""

# print out a screen indicating the status of the game
print("\n\nLet's Play War!\n")
print("Shuffling Player 1's Deck.")
print("Shuffling Player 2's Deck.\n")

# variable to keep track of the score of the user
p1Score = 0
p2Score = 0

# lists that represents each players deck
p1Deck = list(range(1, 11))
p2Deck = list(range(1, 11))

# shuffle the users decks
random.shuffle(p1Deck)
random.shuffle(p2Deck)

#DELETE THIS AFTER THE PROGRAM IS DONE
#print(p1Deck)
#print(p2Deck)

"""
Step 2 [5 POINTS]:
Using a while loop (while some_boolean_expression :  block of code), repeatedly
ask the user to type/enter 1 to "hit", that is, play a hand. With each hand,
check which side wins and update player scores. If there is a tie, just leave
the player scores alone and repeat the asking process.

Note: Do NOT define ANY functions in your implementation.
"""
# index to keep track of the card to look at for each player
current_index = 0

# ask the user for an input
user_input = input("Type 1 to hit! ")

# repeat program while the user input is 1 and the index is less than list size
while(int(user_input) == 1 and current_index<len(p1Deck)):
    # get the first players card and print result
    p1CurrentCard = p1Deck[current_index]
    print("\nPlayer 1 has "+str(p1CurrentCard))

    # get the second players card and print result
    p2CurrentCard = p2Deck[current_index]
    print("Player 2 has "+str(p2CurrentCard))

    # save the amount of points that are at stake
    pointsWon = p1CurrentCard+p2CurrentCard

    # check to see who has the highest card and give the user the points
    if(p1CurrentCard > p2CurrentCard):
        print("\nPlayer 1 wins the hand")
        p1Score += pointsWon
    elif(p1CurrentCard < p2CurrentCard):
        print("\nPlayer 2 wins the hand")
        p2Score += pointsWon
    else:
        print("\nDraw, no players win points")

    # show the amount of points each player has
    print("\nPlayer 1 has "+str(p1Score)+" points.")
    print("Player 2 has "+str(p2Score)+" points.")
    # increment the index to check for the next round
    current_index+=1

    # make sure you don't ask the user to type in 1 more than necessary
    if(current_index < len(p1Deck)):
        user_input = input("\nType 1 to hit! ")
    else: 
        break


"""
Step 3 [2.5 POINTS]:
When any of the decks are empty, print who won (or tie if it's a tie),
and end/terminate the game.

Note: Do NOT define ANY functions in your implementation.
"""
# if player 1 has more points then state player 1 won
if(p1Score > p2Score):
    print("\nPlayer 1 wins the game!")

# if player 2 has more points then state player 2 won
elif(p2Score > p1Score):
    print("\nPlayer 2 wins the game!")

# if both points are equal then say that both players tied
else:
    print("\nBoth players have tied")
