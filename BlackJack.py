# Shaheer Hami
# Simple Game of 21

import random

'''
Store all the cards in a list
'''
cards = ["AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
         "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
         "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
         "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",]

'''
Return a random card from the deck of cards
'''
def getRandomCard():
    randomCard = random.randint(0,len(cards)-1)
    return cards[randomCard];

'''
Assign integer values to the cards
'''
cardValue = 0
if getRandomCard() == "2C" or getRandomCard() == "2D" or getRandomCard() == "2H" or getRandomCard() == "2S":
    cardValue = 2
if getRandomCard() == "3C" or getRandomCard() == "3D" or getRandomCard() == "3H" or getRandomCard() == "3S":
    cardValue = 3
if getRandomCard() == "4C" or getRandomCard() == "4D" or getRandomCard() == "4H" or getRandomCard() == "4S":
    cardValue = 4
if getRandomCard() == "5C" or getRandomCard() == "5D" or getRandomCard() == "5H" or getRandomCard() == "5S":
    cardValue = 5
if getRandomCard() == "6C" or getRandomCard() == "6D" or getRandomCard() == "6H" or getRandomCard() == "6S":
    cardValue = 6
if getRandomCard() == "7C" or getRandomCard() == "7D" or getRandomCard() == "7H" or getRandomCard() == "7S":
    cardValue = 7
if getRandomCard() == "8C" or getRandomCard() == "8D" or getRandomCard() == "8H" or getRandomCard() == "8S":
    cardValue = 8
if getRandomCard() == "9C" or getRandomCard() == "9D" or getRandomCard() == "9H" or getRandomCard() == "9S":
    cardValue = 9
if getRandomCard() == "10C" or getRandomCard() == "10D" or getRandomCard() == "10H" or getRandomCard() == "10S":
    cardValue = 10
if getRandomCard() == "JC" or getRandomCard() == "JD" or getRandomCard() == "JH" or getRandomCard() == "JS":
    cardValue = 10
if getRandomCard() == "QC" or getRandomCard() == "QD" or getRandomCard() == "QH" or getRandomCard() == "QS":
    cardValue = 10
if getRandomCard() == "KC" or getRandomCard() == "KD" or getRandomCard() == "KH" or getRandomCard() == "KS":
    cardValue = 10
if getRandomCard() == "AC" or getRandomCard() == "AD" or getRandomCard() == "AH" or getRandomCard() == "AS":
    if playerPoints < 11:
        cardValue = 11
    else:
        cardValue = 1
    if computerPoints < 11:
        cardValue = 11
    else:
        cardValue = 1    

    


'''
Function to play entire game
'''
def playGame():
    print("Welcome to BlackJack")
    numHands = int(input("Enter the number of hands you wish to play: "))
    playerCards = []
    computerCards = []  
    '''
    Generate 4 random cards
    '''    
    while len(playerCards) < 2:
        playerCards.append(getRandomCard())
        if len(playerCards) == 2:
            print("Players cards:", playerCards)
    playerPoints = cardValue
    print(playerPoints)
playGame()
            
