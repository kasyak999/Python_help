import sqlite3

con = sqlite3.connect('SQL/1db.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS original_titles(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS video_products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    original_title_id INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(original_title_id) REFERENCES original_titles(id)
);
''')


result = cur.execute('''
SELECT video_products.title AS translation,
    original_titles.title AS original
FROM video_products,
    original_titles
WHERE
    video_products.original_title_id = original_titles.id
    -- Для интереса добавим условие
    AND
        original LIKE 'M%';
''')

print(result)
for i in result:
    print(i)
con.close()
