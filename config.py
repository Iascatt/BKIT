from enum import Enum

# Токент бота
TOKEN = "5865146724:AAFGfLc7cF1A7gDBZ2j9gic5AOu5auxx41k"

# Файл базы данных Vedis
db_file = "db.vdb"

# Ключ записи в БД для текущего состояния
CURRENT_STATE = "CURRENT_STATE"


# Состояния автомата
class States(Enum):
    STATE_START = "STATE_START"  # Начало нового диалога
    STATE_ACTION = "STATE_ACTION"
    STATE_CONTENT_TYPE = "STATE_CONTENT_TYPE"
    STATE_CONTENT_TITLE = "STATE_CONTENT_TITLE"


class Dialogs:
    ACTIONS = ['Добавить запись', 'Удалить запись','Посмотреть записи']
    TYPES = ['Книги', 'Фильмы', 'Другое']



