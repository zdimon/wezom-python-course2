import random

def make_pack():
    pack = []
    faces = ['D', 'C', 'H', 'S']
    ranges = [6,7,8,9,10,11]

    for face in faces:
        for range in ranges:
            pack.append(f'{range}-{face}')

    return pack


def shuffle_pack(pack):
    random.shuffle(pack)

    return pack


def get_card(pack):
    if len(pack) > 0:
        card = pack.pop(0)
        return card

    return None
