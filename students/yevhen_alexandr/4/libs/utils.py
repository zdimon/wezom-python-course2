def add(*args):
    sum = 0
    for number in args:
        try:
            sum += number
        except TypeError:
            print('Type error: only numbers can be added')
            return None

    return sum