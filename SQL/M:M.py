import sqlite3


con = sqlite3.connect('SQL/MMdb.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS toppings(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ice_cream(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ice_cream_toppings(
id INTEGER PRIMARY KEY,
ice_cream_id INTEGER NOT NULL,
toppings_id INTEGER NOT NULL,
FOREIGN KEY(ice_cream_id) REFERENCES ice_cream(id),
FOREIGN KEY(toppings_id) REFERENCES toppings(id)
);
''')

# toppings = [
#     (1, 'один'),
#     (2, 'два'),
#     (3, 'три'),
# ]
# ice_cream = [
#     (1, '1один'),
#     (2, '2два'),
#     (3, '3три'),
# ]
# ice_cream_toppings = [
#     (1, 1, 1),
#     (2, 2, 1),
# ]
# cur.executemany('INSERT INTO toppings VALUES(?, ?);', toppings)
# cur.executemany('INSERT INTO ice_cream VALUES(?, ?);', ice_cream)
# cur.executemany('INSERT INTO ice_cream_toppings VALUES(?, ?, ?);', ice_cream_toppings)
# con.commit()

result = cur.execute('''
    SELECT ice_cream.title, toppings.title
    FROM ice_cream
    JOIN toppings ON ice_cream_toppings.ice_cream_id = toppings.id
    JOIN ice_cream_toppings ON ice_cream.id = ice_cream_toppings.ice_cream_id
''')
for i in result:
    print(i)

con.close()
