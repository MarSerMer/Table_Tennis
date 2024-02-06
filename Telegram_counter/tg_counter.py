import telebot
from telebot import types

import token_Marina

bot = telebot.TeleBot(token_Marina.my_token())

WINNING_POINTS = 11
BALANCE_POINTS = 10
BAL_DIFF = 2  # balance difference
CHANGE_PLACE_POINT = 5
serve = 1
player_one: str = "Игрок 1"
player_two: str = "Игрок 2"
decisive_game: bool = False
count1 = 0
count2 = 0
pl1 = [1, 2, 5, 6, 9, 10, 13, 14, 17, 18]
pl2 = [3, 4, 7, 8, 11, 12, 15, 16, 19, 20]


@bot.message_handler()
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_start_game = types.KeyboardButton("Начать 🏓")
    markup.add(btn_start_game)
    bot.send_message(message.chat.id,
                     text="Приветствую, {0.first_name}! Это счётчик очков для настольного тенниса.".
                     format(message.from_user),
                     reply_markup=markup)
    bot.register_next_step_handler(message, before_the_start)


def before_the_start(message):
    global serve
    global decisive_game
    global count1
    global count2
    if (message.text == "Начать 🏓"):
        serve = 1
        decisive_game = False
        count1 = 0
        count2 = 0
        bot.send_message(message.from_user.id,
                         "Решите, кто будет подавать первым. Введите фамилию и имя первого игрока")
        bot.register_next_step_handler(message, get_first_player)
    else:
        bot.send_message(message.from_user.id, 'Нажмите кнопку "Начать"')


def get_first_player(message):
    global player_one
    player_one = message.text
    bot.send_message(message.from_user.id, 'Введите фамилию и имя второго игрока')
    bot.register_next_step_handler(message, get_second_player)


def get_second_player(message):
    global player_two
    player_two = message.text
    bot.send_message(message.from_user.id, 'Это будет решающая партия?')
    get_if_decisive(message)


def get_if_decisive(message):
    global decisive_game
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    key_what = types.InlineKeyboardButton(text='Что это значит?', callback_data='what')
    keyboard.add(key_what)
    bot.send_message(message.from_user.id, text="Сделайте выбор", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global decisive_game
    global serve
    global count1
    global count2
    if call.data == "yes":
        decisive_game = True
        bot.send_message(call.message.chat.id,
                         f"Начинаем! Первый игрок {player_one}, второй игрок {player_two}. Решающая партия.")
        start_counting(call)
    elif call.data == "no":
        decisive_game = False
        bot.send_message(call.message.chat.id,
                         f"Начинаем! Первый игрок {player_one}, второй игрок {player_two}. Партия промежуточная.")
        start_counting(call)
    elif call.data == "what":
        bot.send_message(call.message.chat.id, 'В решающей партии игроки должны поменяться местами '
                                               'после того, как один из них наберёт пять очков')
        get_if_decisive(call)
    elif call.data == "first":
        count1 += 1
        serve += 1
        if decisive_game and count1 == CHANGE_PLACE_POINT:
            bot.send_message(call.message.chat.id, "🏓🏓🏓 ПОМЕНЯЙТЕСЬ МЕСТАМИ 🏓🏓🏓")
            decisive_game = False
        start_counting(call)
    elif call.data == "second":
        count2 += 1
        serve += 1
        if decisive_game and count2 == CHANGE_PLACE_POINT:
            bot.send_message(call.message.chat.id, "🏓🏓🏓 ПОМЕНЯЙТЕСЬ МЕСТАМИ 🏓🏓🏓")
            decisive_game = False
        start_counting(call)
    elif call.data == "first_bal":
        count1 += 1
        serve += 1
        if count1 == count2 + BAL_DIFF:
            bot.send_message(call.message.chat.id, f"Счёт {player_one} {count1} : {player_two} {count2}.\n"
                                                   f"🎉🏆🎉 Выиграл {player_one} 🎉🏆🎉")
            count1 = 0
            count2 = 0
            serve = 1
        else:
            balance_count(call)
    elif call.data == "second_bal":
        count2 += 1
        serve += 1
        if count1 + BAL_DIFF == count2:
            bot.send_message(call.message.chat.id, f"Счёт {player_two} {count2} : {player_one} {count1}.\n"
                                                   f"🎉🏆🎉 Выиграл {player_two} 🎉🏆🎉")
            count1 = 0
            count2 = 0
            serve = 1
        else:
            balance_count(call)


def start_counting(message):
    global serve
    global count1
    global count2
    global pl1
    global pl2
    global decisive_game
    if count1 == BALANCE_POINTS and count2 == BALANCE_POINTS:
        bot.send_message(message.from_user.id, "Баланс!")
        balance_count(message)
    elif count1 == WINNING_POINTS:
        serve = 1
        count1 = 0
        count2 = 0
        decisive_game = False
        bot.send_message(message.from_user.id, f'Счёт {player_one} {count1} : {player_two} {count2}')
        bot.send_message(message.from_user.id, f"🎉🏆🎉 Победитель {player_one} 🎉🏆🎉")
    elif count2 == WINNING_POINTS:
        serve = 1
        count1 = 0
        count2 = 0
        decisive_game = False
        bot.send_message(message.from_user.id, f'Счёт {player_two} {count2} : {player_one} {count1}')
        bot.send_message(message.from_user.id, f"🎉🏆🎉 Победитель {player_two} 🎉🏆🎉")
    elif (serve in pl1) and count1 != WINNING_POINTS and count2 != WINNING_POINTS:
        bot.send_message(message.from_user.id, f'Счёт {player_one} {count1} : {player_two} {count2}')
        bot.send_message(message.from_user.id, f'Подаёт {player_one}')
        keyboard = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text=f'{player_one}', callback_data='first')
        keyboard.add(key_first)
        key_second = types.InlineKeyboardButton(text=f'{player_two}', callback_data='second')
        keyboard.add(key_second)
        bot.send_message(message.from_user.id, text="Очко выиграл: ", reply_markup=keyboard)
    elif (serve in pl2) and count1 != WINNING_POINTS and count2 != WINNING_POINTS:
        bot.send_message(message.from_user.id, f'Счёт {player_two} {count2} : {player_one} {count1}')
        bot.send_message(message.from_user.id, f'Подаёт {player_two}')
        keyboard = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text=f'{player_one}', callback_data='first')
        keyboard.add(key_first)
        key_second = types.InlineKeyboardButton(text=f'{player_two}', callback_data='second')
        keyboard.add(key_second)
        bot.send_message(message.from_user.id, text="Очко выиграл: ", reply_markup=keyboard)


def balance_count(message):
    if serve % 2 == 1:
        bot.send_message(message.from_user.id, f"Счёт {player_one} {count1} : {count2} {player_two}")
        bot.send_message(message.from_user.id, f"Подаёт {player_one}")
    elif serve % 2 == 0:
        bot.send_message(message.from_user.id, f"Счёт {player_two} {count2} : {count1} {player_one}")
        bot.send_message(message.from_user.id, f"Подаёт {player_two}")
    keyboard = types.InlineKeyboardMarkup()
    key_first = types.InlineKeyboardButton(text=f'{player_one}', callback_data='first_bal')
    keyboard.add(key_first)
    key_second = types.InlineKeyboardButton(text=f'{player_two}', callback_data='second_bal')
    keyboard.add(key_second)
    bot.send_message(message.from_user.id, text="Очко выиграл: ", reply_markup=keyboard)


bot.polling(none_stop=True, interval=0)
