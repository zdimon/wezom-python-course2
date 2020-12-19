#!/usr/bin/env python3
import random

name = "Dima"
age = 43
isTrue = False

#import pdb; pdb.set_trace()

users = [1,2,3,True, "Hello world", name]

users.append('casdas')

korteg = (1,2,3,4)

lib = { korteg: users, '1': '2', 'book3': 'Star war2222' }

#print(lib['book1'])
#print(users[4])
#print(random.randint(2,9))

#d = input('Как вас зовут?')
#print("Привет %s %s!!!" % (d,1))



# while True:
#     d = input('Пароль?')
#     if d == '123':
#         print('Yes')
#         break
#     else:
#         print('Wrong paswd!!!')
#         continue

# for i in range(0,100,2):
#     print(i)

# def logit(string):
#     print(string)
#     return True

# rezult = logit('Say hello!!!')
# print(rezult)

import requests
out = requests.get('https://webmonstr.com')
print(out.text)


































