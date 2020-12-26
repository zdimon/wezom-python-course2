user_number1 = input("Введите первое число")
user_number2 = input("Введите второе число")
functions = ['1. Сложение', '2. Вычетание', '3. Умножение', '4. Деление']
print(functions)
user_choice = input("Выберите действие")
if int(user_choice) == int(1):
    rezult = int(user_number1) + int(user_number2)
if int(user_choice) == int(2):
    rezult = int(user_number1) - int(user_number2)
if int(user_choice) == int(3):
    rezult = int(user_number1) * int(user_number2)
if int(user_choice) == int(4):
    rezult = int(user_number1) / int(user_number2)

print(rezult)