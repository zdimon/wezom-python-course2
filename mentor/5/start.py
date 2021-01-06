from secret import BOT_KEY
import telebot
bot = telebot.TeleBot(BOT_KEY)


@bot.message_handler(commands=['start'])
def start_message(message):
    print(message)
    bot.send_message(message.chat.id, 'C Новым Годом!!! /start')


# bot.send_photo(chat_id=room_id, photo=open('images/%s' % card, 'rb'))


print('Start bot service')
bot.polling()