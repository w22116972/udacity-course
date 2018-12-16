
def straight(ranks):
    '''Return True if the ordered ranks form 5-card straight'''
    return len(set(ranks)) == 5 and (max(ranks) - min(ranks) == 4)


def flush(hand):
    '''Return True if all the cards have the same suit
    Args:
        hand: list of (rank, suit)
    '''
    return len(set([suit for rank, suit in hand])) == 1


def kind(n ,ranks):
    '''Return the first rank that this hand has exactly n of.
    Returns:
        None if there is no n-of-a-kind in the hand.
    '''
    for rank in ranks:
        if ranks.count(rank) == n:
            return rank
    return None


def two_pair(ranks):
    '''If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None.'''
    higher_pair = kind(2, ranks)
    lower_pair = kind(2, list(reversed(ranks)))
    if higher_pair and higher_pair != lower_pair:
        return (higher_pair, lower_pair)
    else:
        return None