import random
from pprint import pp


def deal(num, n=5, deck=[r + s for r in "23456789TJQKA" for s in "DHSC"]):
    random.shuffle(deck)
    return [deck[i * n:(i + 1)*n] for i in range(num)]


def play_poker(hands):
    return max(hands, key=hand_rank)


def hand_rank(hand):
    ranks = card_rank(hand)
    if flush(hand) and straight(ranks):
        return 8, max(ranks)
    elif kind(4, ranks):
        return 7, kind(4, ranks), ranks
    elif kind(3, ranks) and kind(2, ranks):
        return 6, kind(3, ranks), kind(2, ranks)
    elif flush(hand):
        return 5, max(ranks)
    elif straight(ranks):
        return 4, max(ranks)
    elif kind(3, ranks):
        return 3, ranks
    elif two_pair(ranks):
        return 2, two_pair(ranks), ranks
    elif kind(2, ranks):
        return 1, kind(2, ranks), ranks
    else:
        return 0, max(ranks)


def card_rank(hand):
    return sorted(["__23456789TJQKA".index(r) for r, s in hand], reverse=True)


def flush(hand):
    return len(set([s for r, s in hand])) == 1


def straight(ranks):
    return max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5


def kind(n, ranks):
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return False


def two_pair(ranks):
    high_pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))
    if high_pair and high_pair != low_pair:
        return high_pair, low_pair
    return False


def test():
    assert card_rank(['KD', 'AS', '3S', '8D', '8S']) == [14, 13, 8, 8, 3]
    assert flush(['KD', 'AS', '3S', '8D', '8S']) is False
    assert flush(['KD', 'AD', '3D', '8D', '8D']) is True
    assert straight(card_rank(['KD', 'AD', '3D', '8D', '8D'])) is False
    assert straight(card_rank(['KD', 'QD', 'QD', 'TD', '9D'])) is False
    assert straight(card_rank(['KD', 'QD', 'JD', 'TD', '9D'])) is True
    assert kind(2, [12, 12, 6, 5, 4]) == 12
    assert kind(2, [12, 12, 6, 6, 4]) == 12
    assert two_pair(2, [12, 12, 6, 6, 4]) == (12, 6)
    assert two_pair(2, [12, 12, 12, 12, 10]) is False
    assert kind(4, [12, 12, 12, 12, 4]) == 12
    return "You are Green!"


hands = deal(5)
pp(hands)
print(play_poker(hands))