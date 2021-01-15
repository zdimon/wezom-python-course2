class Animal():
    color = 'red'
    def move(self):
        print('Top top I am %s!!!' % self.color)
    def jump(self):
        print("prig prig")

class Dog(Animal):
    def say(self):
        print('Gav gav')

class Cat(Animal):
    def say(self):
        print('Miauuuu')