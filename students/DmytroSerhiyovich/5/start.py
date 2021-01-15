from secret import BOT_KEY
import telebot
import random
import json
bot = telebot.TeleBot(BOT_KEY)

@bot.message_handler(commands=['start'])
def start_message(message):
    #print(message)
    bot.send_message(message.chat.id, 'Hi! /start')
    file = open('bd.json', 'r')
    z = file.read()
    zdic = json.loads(z)
    file.close()
    data = {"chat.id": message.chat.id, "chat.username": message.chat.username}
    user_exist = False
    if message.chat.id in zdic:
        user_exist = True
    else:
        zdic['users'].append(data)
        str_zdic = json.dumps(zdic)
        file = open('bd.json', 'w')
        idw = file.write(str_zdic)
        file.close()


@bot.message_handler(commands=['photo'])
def photo_msg(message):
    bot.send_photo(message.chat.id, photo=open('/home/dmytro/wezom-python-course2/students/DmytroSerhiyovich/5/images/6-C.png', 'rb'))

@bot.message_handler(commands=['guess'])
def guess_number(message):
    bot.send_message(message.chat.id, 'Guess a number 1-10')
    file = open('bd.json', 'r')
    s = file.read()
    dic = json.loads(s)
    file.close()
    dic['random_number'] = random.randint(1,10)
    str_dic = json.dumps(dic)
    file = open('bd.json', 'w')
    w = file.write(str_dic)
    file.close()


    
    

    

@bot.message_handler()
def guess_number(message):
    file = open('bd.json', 'r')
    s = file.read()
    dic = json.loads(s)
    numb = dic['random_number']
    y = message.text
    if int(y) == int(numb):
        bot.send_message(message.chat.id, 'U`re right')
    else:
        bot.send_message(message.chat.id, 'Try again')



#print('Start bot service')
bot.polling()