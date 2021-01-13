from secret import BOT_KEY
import telebot
bot = telebot.TeleBot(BOT_KEY)
import random
print('Угадай число!')
random_number = random.randint(1,10)
import json
file = open('bd.json', 'r')
s = file.read()
file.close()
dictionary = json.loads(s)
dictionary['random_number'] = random_number
str_dict = json.dumps(dictionary)
print(str_dict)
file = open('bd.json', 'w')
s = file.write(str_dict)
file.close()


print('random_number')
@bot.message_handler(commands=['start'])
def start_message(message):
    print(message)
    bot.send_message(message.chat.id, 'Вводи число!!! /start')


@bot.message_handler()
def start_message(message):
    print(message.text)
    file = open('bd.json', 'r')
    s = file.read()
    file.close()
    dictionary = json.loads(s)

    if message.text == str(dictionary['random_number']):

        print(message)           
        bot.send_message(message.chat.id, 'Верно!!! /start' )
        random_number = random.randint(6,11)
        print(random_number)

        bot.send_photo(chat_id=message.chat.id, photo=open('images/random_number', 'rb'))
    else:
        print(message)
        bot.send_message(message.chat.id, 'Не верно!!! /start')


print('Start bot service')
bot.polling()
