import random
print('Угадай число')
random_number = random.randint(1,5)
print(random_number)
user_number = input('Вводи число')


list_diagnoses = ['1. Рак', '2. Инсульт']


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




