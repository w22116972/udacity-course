import random

def shuffle(deck):
    "Knuth's algorithm"
    n = len(deck)
    for i in range(n-1):
        deck[i], deck[random.randrange(i, n)] = deck[random.randrange[i, n]], deck[i]
    return deck


