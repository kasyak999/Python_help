import sqlite3

con = sqlite3.connect('db_video.sqlite')
cur = con.cursor()

# Выполнение запроса на получение списка всех таблиц в базе данных
cur.execute("SELECT tbl_name FROM sqlite_master WHERE type='table';")

# Получение результатов запроса
tables = cur.fetchall()
print(tables[0][0])
# Вывод названий таблиц
# for table in tables:
#     print(table[0])


# отключаем соединение
cur.close()
