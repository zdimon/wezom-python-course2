
class CanJump():
    def jump(self):
        print('I can jump')

class CanNotJump():
    def jump(self):
        print('I can NOT jump')

class Animal():
    color = 'red'
    def move(self):
        print('Top top I am %s!!!' % self.color)

    def jump(self):
        print('I am jumping')

class Dog(Animal):
    canjump = CanJump()
    def say(self):
        print('Gav gav')
    def jump(self):
        self.canjump.jump()

class Cat(Animal):
    canjump = CanNotJump()
    def say(self):
        print('Miauuuu')
    def jump(self):
        self.canjump.jump()


class WoodenCat(Animal):
    def say(self):
        print('Miauuuu')


# def decorator_factory():
#     def decorator(function):
#         def wrapper(*args, **kwargs):
#             out = '<strong>'
#             out = out + str(function(*args, **kwargs))
#             out = out+'</strong>'
#             return out
#         return wrapper
#     return decorator

# @router('/start')
# def index():
#     return ..

# @decorator_factory(1,2,3)
# def add(*args):
#     sum = 0
#     for number in args:
#         try:
#             sum += number
#         except TypeError:
#             print('Type error: only numbers can be added')
#             return None

#     return sum

# def wrapper(func):
#     out = '<strong>'
#     out = out + func()
#     out = out+'</strong>'
#     return out

# def counter(*args,**kwargs):
#     print(kwargs['operation'])



