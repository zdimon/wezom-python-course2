import random


def make_deck():
    deck = []
    suits = ('D', 'C', 'H', 'S')
    ranges = (6, 7, 8, 9, 10, 11)

    for suit in suits:
        for range in ranges:
            deck.append(f'{range}-{suit}')

    return deck


def shuffle_deck(deck):
    random.shuffle(deck)

    return deck


def pop_card(deck):
    return deck.pop()


