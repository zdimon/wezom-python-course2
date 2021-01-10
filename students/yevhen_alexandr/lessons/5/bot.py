from libs.secret import BOT_KEY
import telebot
import libs.cards as cards
from libs.db import DB


bot = telebot.TeleBot(BOT_KEY)

pack = cards.make_pack()
cards.shuffle_pack(pack)

db = DB('db/users.json')


@bot.message_handler(commands=['start'])
def send_card(message):
    db.add_user(message)
    bot.send_message(message.chat.id, f'Welcome!')


@bot.message_handler(commands=['getcard'])
def send_card(message):
    print(message)
    card = cards.get_card(pack)
    if card:
        photo = open(f'images/{card}.png', 'rb')
        bot.send_photo(message.chat.id, photo=photo)
    else:
        bot.send_message(message.chat.id, 'The card pack is empty!')    


@bot.message_handler()
def some_text(message):
    bot.send_message(message.chat.id, f'You said {message.text}')

bot.polling()