# -*- coding: utf8 -*-

from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup
from data import read_json, write_json

bot = TeleBot("Your Token")

locations = read_json("game_data.json") # локации
players = read_json("user_data.json") # игроки


# Запуск бота
@bot.message_handler(commands=['старт', 'start'])
def start(message):
    menu_keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    menu_keyboard.add(*['/старт', '/помощь', '/информация', '/играть'])
    bot.send_message(message.from_user.id, "Привет, я бот-квест!\n"
                                      "\nЯ Бот-квест, могу предложить Вам пройти RPG игру «Доставщик пиццы»\n"
                                      "\n Доступные команды 📋:"
                                      "\n/start - начать диалог"
                                      "\n/help - справочная информация"
                                      "\n/info - получить подробную информацию о игре"
                                      "\n/play - начать играть", reply_markup=menu_keyboard)


# Помощь
@bot.message_handler(commands=['помощь', 'help'])
def help(message):
    menu_keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    menu_keyboard.add(*['/старт', '/помощь', '/информация', '/играть'])
    bot.send_message(message.from_user.id, "\n Доступные команды 📋:"
                                      "\n/start - начать диалог"
                                      "\n/help - справочная информация"
                                      "\n/info - получить подробную информацию о игре"
                                      "\n/play - начать играть\n"
                                      "\nНажми кнопочку, чтобы начать играть", reply_markup=menu_keyboard)


# Информация
@bot.message_handler(commands=['информация', 'info'])
def say_info(message):
    bot.send_message(message.chat.id, "\nBot_Quest_Anumi — это телеграмм-бот с текстовой RPG-игрой, которая позволит игрокам взаимодействовать и принимать решения.\n"
                                      "\nВ игре вы представляетесь доставщиком пиццы, который должен доставить заказ заказчику. При этом игра имеет всего 4 уровня, каждый из которых имеет свой поворот событий в сюжете. В игре имеется 12 концовок. Как завершиться игра, зависит от того, как поступит и что выберет пользователь при её прохождении.\n"
                                      "\nБолее подробно об игре вы можете узнать по этой ссылке: https://github.com/Sensei-PGD/Telegram_Bot_Quest/blob/main/README.md\n"
                                      "\nЖелаю вам веселого времяпровождения!")


# Играть
@bot.message_handler(commands=['играть', 'play'])
def play(message):
    p_id = str(message.from_user.id)
    if new_player(p_id): return
    send_info(p_id)


# Движок игры
@bot.message_handler(func=lambda message: True)
def engine(message):
    p_id = str(message.from_user.id)
    if new_player(p_id): return
    try:
        p_new_location = locations[players[p_id]['location']]['actions'][message.text]
        players[p_id]['location'] = p_new_location
        exec(locations[players[p_id]['location']].get("def", ""))
        write_json(players)
    except:
        bot.send_message(p_id, "Неверное действие. Повторите еще раз")

    # Отправка локации
    send_info(p_id)


# Проверка на нового игрока
def new_player(p_id):
    if p_id not in players:
        players[p_id] = {"location": "pizzeria", "loss": 0, 'transport': []}
        write_json(players)
        send_info(p_id)
        return True
    return False


# Отправка локации
def send_info(p_id):
    text = locations[players[p_id]['location']]['description']  # описание локации
    img = open(locations[players[p_id]['location']]['image'], 'rb')  # картинка локации
    actions = list(locations[players[p_id]['location']]['actions'].keys())  # действия локации
    # Действия на локации
    menu_keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    menu_keyboard.add(*actions)
    # Отправка сообщения
    bot.send_photo(p_id, photo=img, caption=text, reply_markup=menu_keyboard)


# Проверка наличия транспорта
def check_key(p_id):
    if 'key' in players[p_id]['transport']:
        players[p_id]['location'] = "lawn"
    else:
        players[p_id]['location'] = "key"


def check_bike(p_id):
    if 'bike' in players[p_id]['transport']:
        players[p_id]['location'] = "lawn"
    else:
        players[p_id]['location'] = "bike"


def check_scooter(p_id):
    if 'scooter' in players[p_id]['transport']:
        players[p_id]['location'] = "lawn"
    else:
        players[p_id]['location'] = "scooter"


# Выбрать велосипед
def equip_bike(p_id):
    players[p_id]['transport'].append("bike")


# Выбрать электросамокат
def equip_scooter(p_id):
    players[p_id]['transport'].append("scooter")


# Счетчик проигрышей
def count_loss(p_id):
    players[p_id]['loss'] += 1


bot.polling()

