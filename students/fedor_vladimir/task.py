import random


def make_deck():
    deck = []
    suits = ('diamonds', 'clubs', 'hearts', 'spades')
    ranges = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace')

    for face in suits:
        for range in ranges:
            deck.append(f'{face}-{range}')

    return deck


def shuffle_deck(deck):
    random.shuffle(deck)

    return deck


def pop_card(deck):
    return deck.pop()


deck = make_deck()
shuffled = shuffle_deck(deck)
print(shuffled)

# deck size before card pop
print(len(shuffled))
first_card = pop_card(shuffled)

print(first_card)

# deck size after card pop
print(len(shuffled))
