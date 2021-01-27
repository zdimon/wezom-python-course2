faces = ['diamonds', 'clubs', 'hearts', 'spades']
ranges = [2, 3, 4, 5, 6, 7, 8, 9, 10]
pack = []


def make_pack():
    for face in faces:
        for range in ranges:
            pack.append(f'{face} - {range}')
    return pack


print(make_pack())



