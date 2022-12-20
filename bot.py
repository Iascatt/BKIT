import telebot
from telebot import types
import config
import dbworker

# Создание бота
bot = telebot.TeleBot(config.TOKEN)


# Начало диалога
@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, 'Привет! Появилась мысли прочитать или посмотреть что-нибудь, но времени нет?\n'
                                      'Чтобы не забыть, напиши название здесь!')
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_ACTION.value)

    # создаем пустую строку, где будем хранить типы контента
    dbworker.set(dbworker.make_key(message.chat.id, "CONTENT_TYPES"), "")

    markup = types.ReplyKeyboardMarkup(row_width=len(config.Dialogs.ACTIONS))
    for i in config.Dialogs.ACTIONS:
        markup.add(types.KeyboardButton(i))
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=markup)


# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
@bot.message_handler(commands=['reset'])
def cmd_reset(message):
    bot.send_message(message.chat.id, 'Сбрасываем результаты предыдущего ввода.')
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_ACTION.value)
    markup = types.ReplyKeyboardMarkup(row_width=len(config.Dialogs.ACTIONS))
    for i in config.Dialogs.ACTIONS:
        markup.add(types.KeyboardButton(i))
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=markup)


# Выбор типа
@bot.message_handler(func=lambda message: dbworker.get(
    dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_ACTION.value)
def content_type(message):
    text = message.text
    if text not in config.Dialogs.ACTIONS:
        # Состояние не изменяется, выводится сообщение об ошибке
        bot.send_message(message.chat.id, 'Попробуйте еще раз!')
        return
    else:
        bot.send_message(message.chat.id, f'Вы выбрали {text.lower()}.')
        # Меняем текущее состояние
        dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_CONTENT_TYPE.value)
        # Сохраняем действие
        dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_ACTION.value), text)

        markup = types.ReplyKeyboardMarkup(selective=False)
        bot.send_message(message.chat.id, "Выберите введите тип контента, например, \"книги\" (в 1 строчку!):",
                         reply_markup=markup)

# Выбор названия
@bot.message_handler(func=lambda message: dbworker.get(dbworker.make_key(message.chat.id,
                                                                         config.CURRENT_STATE)) == config.States.STATE_CONTENT_TYPE.value)
def content_name(message):
    text = message.text
    bot.send_message(message.chat.id, f'Вы выбрали тип: {text}.')

    if text not in config.Dialogs.TYPES:
        config.Dialogs.TYPES.append(text)
        # добавим тип в базу
        cur_types = dbworker.get(dbworker.make_key(message.chat.id, "CONTENT_TYPES"))
        new_types = cur_types + '\n' + text
        dbworker.set(dbworker.make_key(message.chat.id, "CONTENT_TYPES"), new_types)
        # создаем пустую строку, где будем хранить названия
        dbworker.set(dbworker.make_key(message.chat.id, text + "_CONTENT_TITLES"), "")
    # Меняем текущее состояние
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_CONTENT_TITLE.value)
    # Сохраняем тип
    dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_CONTENT_TYPE.value), text)
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, 'Введите название (или любой текст, если выбрали посмотреть): ',
                     reply_markup=markup)


# Сохранение
@bot.message_handler(func=lambda message: dbworker.get(dbworker.make_key(message.chat.id,
                                                                         config.CURRENT_STATE)) == config.States.STATE_CONTENT_TITLE.value)
def operation(message):
    # Название
    v_title = message.text
    # Читаем операнды из базы данных
    v_action = dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_ACTION.value))
    v_type = dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_CONTENT_TYPE.value))
    # сохраненный набор названий в строке
    titles = dbworker.get(dbworker.make_key(message.chat.id, v_type + "_CONTENT_TITLES"))

    # Выполняем действие

    if v_action == 'Добавить запись':
        bot.send_message(message.chat.id,
                         f'Вы хотите {v_action.lower()} {v_title} типа {v_type.lower()}? Будет сделано!')
        if v_title not in titles:
            titles += '\n' + v_title
            dbworker.set(dbworker.make_key(message.chat.id, v_type + "_CONTENT_TITLES"), titles)
            bot.send_message(message.chat.id, 'Получилось!')
            bot.send_message(message.chat.id, titles[titles.find('\n')::])
        else:
            bot.send_message(message.chat.id, 'А такая запись уже есть, вот:')
            bot.send_message(message.chat.id, titles[titles.find('\n')::])

    elif v_action == 'Удалить запись':
        bot.send_message(message.chat.id,
                         f'Вы хотите {v_action.lower()} {v_title} типа {v_type.lower()}? Будет сделано!')

        if v_title in titles:
            titles.remove(v_title)
            dbworker.set(dbworker.make_key(message.chat.id, v_type + "_CONTENT_TITLES"), titles)
            bot.send_message(message.chat.id, 'Получилось!')
            bot.send_message(message.chat.id, titles)

        else:
            bot.send_message(message.chat.id, 'Простите, такой записи пока нет, вот:')
            bot.send_message(message.chat.id, titles[titles.find('\n')::])
            pass
    elif v_action == 'Посмотреть записи':
        bot.send_message(message.chat.id, f'Вы хотите {v_action.lower()}? Вот!')

        bot.send_message(message.chat.id, titles[titles.find('\n')::])

    # Выводим результат
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_ACTION.value)
    bot.send_message(message.chat.id, 'Продолжим?')
    markup = types.ReplyKeyboardMarkup(row_width=len(config.Dialogs.ACTIONS))
    for i in config.Dialogs.ACTIONS:
        markup.add(types.KeyboardButton(i))
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=markup)


if __name__ == '__main__':
    bot.infinity_polling()
