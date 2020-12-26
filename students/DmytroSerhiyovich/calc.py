user_number1 = input("Введите первое число")
user_number2 = input("Введите второе число")
functions = ['1. Сложение', '2. Вычетание', '3. Умножение', '4. Деление']
print(functions)
user_choice = input("Выберите действие")
if user_choice == 1:
    rezult = add(user_number1, user_number2)
if user_choice == 2:
    rezult = subtract(user_number1, user_number2)
if user_choice == 3:
    rezult = multiply(user_number1, user_number2)
if user_choice == 4:
    rezult = devide(user_number1, user_number2)

print(rezult)