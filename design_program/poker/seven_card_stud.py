"""
Quiz:
From 7-card hand, return the best 5 card hand.
"""
import itertools
from .poker_game import hand_rank

def best_hand(hand):
    max_rank = (-1, -1)
    best_hand = None
    # combinations returns in sorted order and no repeated elements
    for i in itertools.combinations(hand, 5):
        if hand_rank(i) > max_rank:
            max_rank = hand_rank(i)
            best_hand = i
    return best_hand




def test_best_hand():
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'

print(test_best_hand())