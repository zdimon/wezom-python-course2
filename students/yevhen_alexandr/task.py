import random

def make_pack():
    pack = []
    faces = ['diamonds', 'clubs', 'hearts', 'spades']
    ranges = [2,3,4,5,6,7,8,9,10]

    for face in faces:
        for range in ranges:
            pack.append('%s-%s' % (face,range))

    return pack


def shuffle_pack(pack):
    random.shuffle(pack)

    return pack


def get_card(pack):
    card = pack.pop(0)

    return card



pack = shuffle_pack(make_pack())
print(get_card(pack))
