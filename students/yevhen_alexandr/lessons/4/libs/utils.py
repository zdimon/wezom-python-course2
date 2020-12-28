def add(*args):
    sum = 0
    for number in args:
        try:
            sum += number
        except TypeError:
            print('Type error: only numbers can be added')
            return None

    return sum



class Animal():
    color = 'red'
    def move(self):
        print('Top top I am %s!!!' % self.color)

    def jump(self):
        print('I am jumping')

class Dog(Animal):
    def say(self):
        print('Gav gav')

class Cat(Animal):
    def say(self):
        print('Miauuuu')