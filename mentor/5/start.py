from secret import BOT_KEY
import telebot
bot = telebot.TeleBot(BOT_KEY)

@bot.message_handler(commands=['start'])
def start_message(message):
    print(message)
    bot.send_message(message.chat.id, 'C Новым Годом!!! /start')

print('Start bot service')
bot.polling()