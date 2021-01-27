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
    bot.send_message(message.chat.id, "Hello, you are just typed /start \n typing /start again will reset your user score")
    bot.send_photo(chat_id=message.chat.id, photo=open('images/%s' % card, 'rb'))
    #print(dir(message.chat))
    #print(message)
    file = open('bd.json', 'r')
    s = file.read()
    file.close()
    dictionary = json.loads(s)
    is_single = 0
    for index in range(len(dictionary['users'])):
        if dictionary['users'][index]['chat_id'] == f"{message.chat.id}":
            is_single += 1
    if is_single == 0:
        dictionary['users'].append({"username": f"@{message.chat.username}", "chat_id": f"{message.chat.id}", "score": 0})
    str_dict = json.dumps(dictionary)
    file = open('bd.json', 'w')
    file.write(str_dict)
    file.close()


@bot.message_handler(commands=['game'])
def gues_number_game_start(message):
    bot.send_message(message.chat.id, "gues the number")
    num = random.randrange(1, 10)
    file = open('bd.json', 'r')
    s = file.read()
    file.close()
    dictionary = json.loads(s)
    dictionary['random_number'] = num
    dictionary['game'] = 1
    str_dict = json.dumps(dictionary)
    file = open('bd.json', 'w')
    file.write(str_dict)
    file.close()
    #file_num = open(r'random_num.txt', 'w')
    #file_game = open(r'game.txt', 'w')
    #file_game.write('1')
    #file_num.write(f'{num}')
    #file_num.close()
    #file_game.close()

@bot.message_handler(commands=['score'])
def display_score(message):
    file = open('bd.json', 'r')
    s = file.read()
    file.close()
    dictionary = json.loads(s)
    scores = ""
    for index in range(len(dictionary['users'])):
        scores = scores + f"{dictionary['users'][index]['username']} - {dictionary['users'][index]['score']}\n"
    bot.send_message(message.chat.id, f"{scores}")

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
            dictionary = json.loads(s)
            dictionary['game'] = 0
            for index in range(len(dictionary['users'])):
                if dictionary['users'][index]['chat_id'] == f"{message.chat.id}":
                    for index_1 in range(len(dictionary['users'])):
                        bot.send_message(int(dictionary['users'][index_1]['chat_id']), f"user {dictionary['users'][index]['username']} scored in game")
                    score = int(dictionary['users'][index]['score']) + 1
                    dictionary['users'][index]['score'] = f"{score}"
            str_dict = json.dumps(dictionary)
            with open('bd.json', 'w') as file:
                file.write(str_dict)
            #file_game = open(r'game.txt', 'w+')
            #file_game.write('0')
            #file_game.close()
        elif int(message.text) > int(f'{num}'):
            bot.send_message(message.chat.id, 'you number is bigger then hidden, try again')
        elif int(message.text) < int(f'{num}'):
            bot.send_message(message.chat.id, 'you number is lower then hidden, try again')


print(BOT_KEY)
bot.polling()
