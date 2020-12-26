
def add(*a):
    sum = 0
    for i in a:
        if type(i) == int or type(i) == float:
            sum+=i
    return sum