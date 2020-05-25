import random


def shuffle_deck(cards):
    for i in range(0,len(cards)):
        k = int(random.random() * (i  + 1))
        cards[i], cards[k] = cards[k], cards[i]
    return cards


def test_card_shuffle():
    result = [i for i in range(1, 53)]
    print(result)
    i = 0
    while i < 10:
        result = shuffle_deck(result)
        print(result)
        i += 1
test_card_shuffle()
