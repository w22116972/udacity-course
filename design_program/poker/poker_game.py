
"""
# 設計Poker 程式

把手牌傳入poker程式會比較大小
- 2 pair
- 葫蘆 (n - kinds)
- 順子 (straight)
- 同花順 (flush)

"""

from poker.poker_rank import straight, flush, two_pair, kind
import random

def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    '''Shuffle the deck and deal out numhands n-card hands.'''
    random.shuffle(deck)
    return [deck[n * i: n * (i + 1)] for i in range(numhands)]

def poker(hands):
    """Return the best hand: poker([hand, ...]) => hand"""
    return max(hands, key=hand_rank)

def all_max(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    return [item for item in iterable if hand_rank(item) == hand_rank(max(iterable, key=hand_rank))]

def card_ranks(hand):
    """Return a list of the ranks, sorted with higher first"""
    nums = [str(n) for n in range(2, 10)] + ['T', 'J', 'Q', 'K', 'A']
    ranks = [nums.index(rank) + 2 for rank, suit in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def hand_rank(hand):
    """Return a value indicating the ranking of a hand"""
    ranks = card_ranks(hand)  # return in sorted order
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, ranks[0])
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks)[0], two_pair(ranks)[1], ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)


def test():
    """Test cases for functions in poker program"""
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "5S 5D 9H 9C 6S".split() # Two-pair
    al = "AC 2D 4H 3D 5S".split()  # Ace-Low Straight
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (9, 5)
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert poker([sf, fk, fh]) == sf

    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh

    assert poker([sf]) == sf
    assert poker([sf] + 99 * [fh]) == sf

    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    print("tests pass")

if __name__ == "__main__":
    test()