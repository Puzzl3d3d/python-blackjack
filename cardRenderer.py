
import os
os.system("color")

card = """
**********
* {}    {} *
*        *
*        *
*        *
* {}    {} *
**********
"""

suitColours = {
    "Hearts": "\033[91m{}\033[00m",
    "Diamonds": "\033[91m{}\033[00m",
    "Clubs": "{}",
    "Spades": "{}"
}
suitEmojis = {
    "Hearts": "♥",
    "Clubs": "♣",
    "Diamonds": "♦",
    "Spades": "♠"
}

def combineStrings(str1, str2, *args, spacing="  ", suit1="Spades", suit2="Spades"):
    combined = ""
    str1 = str1.split("\n")
    str2 = str2.split("\n")
    
    for i in range(min(len(str1), len(str2))):
        combined += f"{suitColours[suit1].format(str1[i])}{spacing}{suitColours[suit2].format(str2[i])}\n"
    return combined

def getCardDisplay(suit, value):
    if suit is None or value is None:
        return card.format(" "," "," "," ")
    if value >= 10:
        value = {10: "T", 11: "A", 12: "J", 13: "Q", 14: "K"}[value]
    else:
        value = str(value)
    suitEmoji = suitEmojis[suit]
    return suitColours[suit].format(card.format(value, suitEmoji, suitEmoji, value))
