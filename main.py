from random import randint as random
from random import choice

from cardRenderer import combineStrings, getCardDisplay

cardsChosen = []
playerCards = []
dealerCards = []


import os
def clear():
    os.system("cls")


def getResult():
    hand, dealerHand = getHands()

    print(f"FINAL | Player: {hand}, Dealer: {dealerHand}")

    if dealerHand == 21 and len(dealerCards) == 2:
        # Dealer blackjack
        print("Lose! | Dealer blackjack")
        return -1
    elif hand == 21 and len(playerCards) == 2:
        # Player blackjack
        print("Win! | Blackjack!")
        return 1.5
    elif hand > 21:
        print("Bust!")
        return -1
    elif dealerHand > 21:
        print("Win! | Dealer busted")
        return 1
    elif dealerHand == hand:
        print("Draw!") # return bet
        return 0
    elif hand > dealerHand:
        print("Win! | Better hand")
        return 1
    elif dealerHand > hand:
        print("Lose! | Worse hand")
        return -1

def getRandomCard():
    suit = ""
    value = 0
    while True:
        suit = choice(["Clubs", "Spades", "Diamonds", "Hearts"])
        value = random(2,14)
        if not [suit, value] in cardsChosen: break
    return suit, value

def getHandValue(cards):
    numAces = 0
    hand = 0

    for card in cards:
        if card == []: continue
        _suit, value = card
        if value == 11:
            numAces += 1
            continue
        elif value > 11:
            value = 10
        hand += value

    for _i in range(numAces):
        if hand + 11 > 21:
            hand += 1
        else:
            hand += 11

    return hand

def getHands():
    return getHandValue(playerCards), getHandValue(dealerCards)

def deal(cards):
    suit, value = getRandomCard()
    cardsChosen.append([suit, value])

    if len(cards) == 2 and cards[1] == []:
        cards[1] = [suit, value]
    else:
        cards.append([suit, value])
    
    hand = getHandValue(cards)

    return hand, suit, value
def printList(l):
    combined = "\n\n\n\n\n\n\n\n"
    for card in l:
        if card == []:
            combined = combineStrings(combined, getCardDisplay(None, None), suit2="Spades") # default as spades for no reason whatsoever
        else:
            combined = combineStrings(combined, getCardDisplay(*card), suit2=card[0])
    print(combined)
    print(getHandValue(l))

def dealer():
    hand, dealerHand = getHands()

    if hand > 21: return -1
    if dealerHand > 21: return 2
    while True:
        if dealerHand < hand and dealerHand < 17:
            print(f"Dealer: {dealerHand}, Player: {hand}")
            dealerHand, suit, value = deal(dealerCards)

            printList(dealerCards)
            
            if dealerHand > 21:
                print("Win! | Dealer busted")
                return 1
        else:
            break
            
    return getResult()
        

def hitCardPlayer(*a, p=True):
    deal(playerCards)
    hand, dealerHand = getHands()

    #print("PLAYER DREW, CARDS:", playerCards)
    if p:
        clear()
        print("Player:")
        printList(playerCards)
        print("Dealer:")
        printList(dealerCards)

    if hand > 21:
        print("Bust!")
        return -1
    
    return hand

def doGame():
    global playerCards
    global dealerCards
    
    clear()
    
    cardsChosen = []

    playerCards = []
    dealerCards = []

    hitCardPlayer(p=False)
    hitCardPlayer(p=False)

    deal(dealerCards)
    dealerCards.append([])

    hand, dealerHand = getHands()
        
    print("Player:")
    printList(playerCards)
    print("Dealer:")
    printList(dealerCards)
        
    while True:
        choice = input("Hit or stand? ")
        if choice.lower()[0] != "h":
            #playerStopped = True
            break
        
        #hand, suit, value = deal(hand)
        #playerCards.append([suit, value])
        
        result = hitCardPlayer(hand)
        if result == -1:
            return -1
            
        #printList(playerCards)
        
        if hand > 21:
            print("Bust!")
            return -1
        elif dealerHand > 21:
            print("Win! | Dealer busted")
            return 2
        
    dealer()
        
    clear()
    print("\nFinal hand:\n")
    print("Player:")
    printList(playerCards)
    print("Dealer:")
    printList(dealerCards)
            
    return getResult()

def main():
    global playerCards
    global dealerCards
    
    money = 100
    
    while True:
        while True:
            try:
                bet = int(input(f"What's your bet (You have ${money})? "))
            except:
                print("Not a valid number")
            if bet > money:
                print("Not enough money")
            elif bet <= 0:
                print("Too low!")
            else:
                break
        
        if bet == money:
            print("ALL IN!")
        
        result = doGame()
        
        money += bet*result
        
        if money == 0:
            print("Oops, you ran out of money!")
            break
        
    print("Wanna try again?")
        
    
main()