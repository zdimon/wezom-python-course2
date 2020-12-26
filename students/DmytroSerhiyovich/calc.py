x = input("Введите первое число")
y = input("Введите второе число")
functions = ['1. Сложение', '2. Вычетание', '3. Умножение', '4. Деление']
print(functions)
user_choice = input("Выберите действие")
if int(user_choice) == int(1):
    rezult = int(x) + int(y)
if int(user_choice) == int(2):
    rezult = int(x) - int(y)
if int(user_choice) == int(3):
    rezult = int(x) * int(y)
if int(user_choice) == int(4):
    rezult = int(x) / int(y)

print(rezult)