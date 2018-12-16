"""
Write a function best_wild_hand(hand) that takes as input a 7-card hand
and returns the best 5 card hand.
In this problem, it is possible for a hand to include jokers.
Jokers will be treated as 'wild cards' which can take any rank or suit of the same color.
The black joker, '?B', can be used as any spade or club and the red joker,
'?R', can be used as any heart or diamond.
"""

import itertools
from poker.poker_game import hand_rank

def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."
    if '?B' not in hand and '?R' not in hand:
        return hand_rank(hand)
    rank_values = [str(i) for i in range(2, 10)] + ['A', 'T', 'J', 'Q', 'K']
    black_joker = itertools.product(['S', 'C'], rank_values)
    red_joker = itertools.product(['H', 'D'], rank_values)
    result = []
    for card in hand:
        if card == '?B':
            result = itertools.product(result, black_joker)
        elif card == '?R':
            result = itertools.product(result, red_joker)

    return best_hand


def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'


test_best_wild_hand()