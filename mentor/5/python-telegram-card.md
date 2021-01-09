# Карточная игра для телеграм.

Суть игры описывает игра БлекДжек.

Когда пользователь последовательно набирает случайные карты из колоды и набирает балы не более 21. 

Поосле прохождения курса студент научится следующему.

Устанавливать и использовать библиотеки Python.

Создавать телеграм бота и отсылать сообщения в месенджер.

Генерировать и работать с случайными числами.

Реагировать на события в telegram.

Обрабатывать изображения с помощью Pillow.

Работать с файловой системой и форматом json.

### Реализация.

Для телегам бота есть несколько библиотек.

python-telegram-bot - имеет несколько сложноватый синтаксис поэтому будем использовать pytelegramapi 
      
Установим библиотеку.

    pip install pyTelegramBotAPI

Регистрируем бота.

Заходим в клиенте на BotFather и набираем имя и логин бота.



Создание бота.

    import telebot
    bot = telebot.TeleBot(key)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

    bot.polling()

Выбираем случайные карты и считаем очки.

    from os import listdir
    from os.path import isfile, join
    import random

    def get_score(cards):
        score = 0
        for card in cards:
            num = int(card.split('-')[0])
            score += num
        return score

    def get_random_cards():
        path = 'images'
        out = []
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        for i in range(1,3):
            rand = random.randint(0,len(onlyfiles)-1)
            out.append(onlyfiles[rand])
            onlyfiles.pop(rand)
        return out

Посылаем картинки и сколько набрали.

    cards = get_random_cards()
    score = get_score(cards)
    bot.send_message(message.chat.id, 'Вы набрали: %s!' % score)
    for card in cards:
        bot.send_photo(chat_id=room_id, photo=open('images/%s' % card, 'rb'))

Делаем функцию для склеивания картинок в одну.

Устанавливаем инструмент

    pip install Pillow

Определяем функцию

    from PIL import Image
    def combine_images(cards,name):
        images = []
        for image in cards:
            images.append(Image.open('images/%s' % image))
        new_im = Image.new('RGB', (210, 107))
        x_offset = 0
        for im in images:
            new_im.paste(im, (x_offset,0))
            x_offset += 70
    new_im.save(name)

Используем.

    combine_images(cards,'player.png')
    bot.send_photo(chat_id=room_id, photo=open('player.png', 'rb'))

Посылаем 2 кнопки.


    @bot.message_handler(commands=['start'])
    def start_message(message):
        user_cards = get_random_cards()
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Взять новую карту',callback_data='new'))
        markup.add(InlineKeyboardButton('Прекратить',callback_data='done'))
        bot.send_message(message.chat.id,'Вы набрали %s' % get_score(user_cards), reply_markup=markup)
        combine_images(user_cards,'tmp.jpg')
        bot.send_photo(chat_id=message.chat.id, photo=open('tmp.jpg','rb'))

Создаем дополнительный модуль bd.py для работы с базой данных.


    import json

    def save_bd(data):
        with open('bd.json','w') as f:
            rowdata = json.dumps(data)
            f.write(rowdata)


    def read_bd():
        with open('bd.json','r') as f:
            rowdata = f.read()
            data = json.loads(rowdata)
            return data

    def add_cards(cards):
        data = read_bd()
        data['cards'] = cards
        save_bd(data)



Делаем обработчики.

    @bot.callback_query_handler(lambda payload: payload.data=='done')
    def button_done(query):
        comp_cards = get_random_cards()
        comp_score = get_score(comp_cards)
        bot.send_message(query.message.chat.id,'Компьютер набрал %s' % comp_score)
        db = read_bd()
        user_score = get_score(db['cards'])
        print('%s<%s' % (user_score,comp_score) )
        if(user_score<comp_score):
            bot.send_message(query.message.chat.id,'Вы проиграли!')
        elif(user_score>comp_score):
            bot.send_message(query.message.chat.id,'Вы выйграли!')
        else:
            bot.send_message(query.message.chat.id,'Ничья!')


    @bot.message_handler(commands=['start'])
    def start_message(message):
        user_cards = get_random_cards()
        add_cards(user_cards)
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Взять новую карту',callback_data='new'))
        markup.add(InlineKeyboardButton('Прекратить',callback_data='done'))
        bot.send_message(message.chat.id,'Вы набрали %s' % get_score(user_cards), reply_markup=markup)
        combine_images(user_cards,'tmp.jpg')
        bot.send_photo(chat_id=message.chat.id, photo=open('tmp.jpg','rb'))



