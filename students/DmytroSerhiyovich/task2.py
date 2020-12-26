import random
print('Угадай число')
random_number = random.randint(1,5)

print(random_number)



while True:
    user_number = input('Вводи число')
    if int(random_number) == int(user_number):
        print("You`re right")
        break
    else:
        print("Try again")
        continue
         