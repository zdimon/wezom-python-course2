from lib.secret import BOT_TOKEN
from lib.cards import make_deck, shuffle_deck, pop_card
import telebot

if __name__ == "__main__":
    bot = telebot.TeleBot(BOT_TOKEN)

    deck = shuffle_deck(make_deck())

    @bot.message_handler(commands=['start'])
    def start_message(message):
        if len(deck):
            card = pop_card(deck)
            photo = open(f'images/{card}.png',  'rb')
            bot.send_photo(message.chat.id, photo)
        else:
            bot.send_message(message.chat.id, "Карты закончились")

    print('Start bot service')
    bot.polling()
    pass

