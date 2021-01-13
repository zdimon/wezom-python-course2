'''
import random
print('Угадай число')
random_number = random.randint(1,5)
print(random_number)
user_number = input('Вводи число')


list_diagnoses = ['1. Рак', '2. Инсульт']

import random
print('Выберите, пожалуйста номер диагноза')
for i in list_diagnoses:
    print(i)
user_number = input('Введите номер диагноза')
if user_number == '1':
    print('Дыхательная гимнастика по Стельниковой!')
    print('ЛФК')

if user_number == '2':
    print('Йога и пилатес!')
    print('ЛФК')

    print(i)


    print(i)
'''
'''
list_diagnoses = {
    '1': {
        'diagnose': 'Рак',
        'exesizes': [
            'Приседание',
            'Поддтягивание'
        ]
    },
    '2': {
        'diagnose': 'Инсульт',
        'exesizes': [
            'Приседание',
            'Поддтягивание'
        ]
    }
}

for d in list_diagnoses:
    print(d)
    print(list_diagnoses[d]['diagnose'])

print('Выбери, пожалуйста диагноз')
user_number = input('Введи число!')
for e in list_diagnoses[user_number]['exesizes']:
   
    print(e)

'''


import random
print('Угадай число!')
random_number = random.randint(1,10)
print(random_number)
user_number = input('Вводи число!')




    
