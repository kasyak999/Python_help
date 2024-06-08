import sqlite3

# Если в текущей директории нет файла db.sqlite - 
# он будет создан; одновременно будет создано и соединение с базой данных.
# Если файл существует, метод connect просто подключится к базе.
con = sqlite3.connect('db.sqlite')
# con = sqlite3.connect(':memory:')
# Создаём специальный объект cursor для работы с БД.
# Вся дальнейшая работа будет вестись через методы этого объекта.
cur = con.cursor()

# Готовим SQL-запросы.
# Для читаемости запрос обрамлён в тройные кавычки и разбит построчно.
query_1 = '''
CREATE TABLE IF NOT EXISTS directors(
    id INTEGER PRIMARY KEY,
    full_name TEXT,
    birth_year INTEGER
);
'''
query_2 = '''
CREATE TABLE IF NOT EXISTS video_products(
    id INTEGER PRIMARY KEY,
    title TEXT,
    product_type TEXT,
    release_year INTEGER
);
'''

# query = '''
# CREATE TABLE IF NOT EXISTS directors(
#     id INTEGER PRIMARY KEY,
#     full_name TEXT,
#     birth_year INTEGER
# );

# CREATE TABLE IF NOT EXISTS video_products(
#     id INTEGER PRIMARY KEY,
#     title TEXT,
#     product_type TEXT,
#     release_year INTEGER
# );
# '''
# cur.executescript(query)

# Применяем запросы.
cur.execute(query_1)
cur.execute(query_2)

directors = [
    (1, 'Текс Эйвери', 1908),
    (2, 'Роберт Земекис', 1952),
    (3, 'Джерри Чиникей', 1912),
]

cur.executemany('INSERT INTO directors VALUES(?, ?, ?);', directors)

con.commit()

# Закрываем соединение с БД.
con.close()
