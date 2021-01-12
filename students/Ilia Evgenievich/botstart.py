from secret import BOT_KEY
import telebot
import random
import json

bot = telebot.TeleBot(BOT_KEY)

@bot.message_handler(commands=['start'])
def start_message(message):
    sym = ['C', 'D', 'H', 'S']
    symb = random.choice(sym)
    num = random.randrange(6, 11)
    card =f'{num}-{symb}.png'
    bot.send_message(message.chat.id, "Happy new year!!! /start")
    bot.send_photo(chat_id=message.chat.id, photo=open('images/%s' % card, 'rb'))
    file = open('bd.json', 'r')
    s = file.read()
    file.close()
    file = open('bd.json', 'w')
    dictionary = json.loads(s)
    dictionary['usres'].append(message.chat.id) 
    str_dict = json.dumps(dictionary)
    file.write(str_dict)
    file.close()


@bot.message_handler(commands=['game'])
def gues_number_game_start(message):
    bot.send_message(message.chat.id, "gues the number")
    num = random.randrange(1, 10)
    file = open('bd.json', 'r')
    s = file.read()
    file.close()
    file = open('bd.json', 'w')
    dictionary = json.loads(s)
    dictionary['random_number'] = num
    dictionary['game'] = 1
    str_dict = json.dumps(dictionary)
    file.write(str_dict)
    file.close()
    #file_num = open(r'random_num.txt', 'w')
    #file_game = open(r'game.txt', 'w')
    #file_game.write('1')
    #file_num.write(f'{num}')
    #file_num.close()
    #file_game.close()

@bot.message_handler()
def gues_number_game(message):
    file = open('bd.json', 'r')
    s = file.read()
    dictionary = json.loads(s)
    game = int(dictionary['game'])
    file.close()
    #file_game = open(r'game.txt', 'r+')
    #file_num = open(r'random_num.txt', 'r+')
    #game = int(file_game.read())
    #file_game.close()
    if game:
        with open('bd.json', 'r') as file:
            s = file.read()
            dictionary = json.loads(s)
            num = dictionary['random_number']
        #num = file_num.read()
        print(num)
        if message.text == f'{num}':
            bot.send_message(message.chat.id, 'you guesed the number')
            file = open('bd.json', 'r')
            s = file.read()
            file.close()
            with open('bd.json', 'w') as file:
                dictionary = json.loads(s)
                dictionary['game'] = 0
                str_dict = json.dumps(dictionary)
                file.write(str_dict)
            #file_game = open(r'game.txt', 'w+')
            #file_game.write('0')
            #file_game.close()
        elif message.text != f'{num}':
            bot.send_message(message.chat.id, 'you do not guesed the number, try again')
    


print(BOT_KEY)
bot.polling()