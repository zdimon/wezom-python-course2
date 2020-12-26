def add(*args):
    sum = 0
    for number in args:
        try:
            sum += number
        except TypeError:
            print('Type error: only numbers can be added')
            return None

    return sum


def wrapper(func):
    out = '<strong>'
    out = out + func()
    out = out+'</strong>'
    return out

def counter(*args,**kwargs):
    print(kwargs['operation'])



