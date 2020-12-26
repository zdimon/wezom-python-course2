def add(*args):
    sum = 0
    for number in args:
        try:
            sum += number
        except TypeError:
            print('Type error: only numbers can be added')
            return None

    return sum


def decorator_factory(argument):
    def decorator(function):
        def wrapper(*args, **kwargs):
            out = '<strong>'
            out = out + function(*args, **kwargs)
            out = out+'</strong>'
            return out
        return wrapper
    return decorator

def wrapper(func):
    out = '<strong>'
    out = out + func()
    out = out+'</strong>'
    return out

def counter(*args,**kwargs):
    print(kwargs['operation'])



