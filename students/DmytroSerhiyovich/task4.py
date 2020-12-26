
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
    print(list_diagnoses[d]['diagnose'])
user_choise = input("Your diagnose")
for exercise in list_diagnoses[user_choise]['exesizes']:
    print(exercise)
