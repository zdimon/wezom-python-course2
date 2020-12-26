
def add(*a):
    sum = 0
    for i in a:
        if type(i) == int or type(i) == float:
            sum+=i
    return sum

class Animal():
    color = 'red'
    def move(self):
        print('Top top I am %s!!!' % self.color)

    def jump(self):
        print('Jump!')

class Dog(Animal):
    def say(self):
        print('Gav gav')

class Cat(Animal):
    def say(self):
        print('Miauuuu')