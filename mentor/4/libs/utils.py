
class Animal():
    color = 'red'
    def move(self):
        print('Top top I am %s!!!' % self.color)

class Dog(Animal):
    def say(self):
        print('Gav gav')

class Cat(Animal):
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



