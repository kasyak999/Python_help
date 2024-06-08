import sqlite3

con = sqlite3.connect('db_video.sqlite')
cur = con.cursor()
cur.execute('''
    SELECT COUNT(title)
    FROM video_products;
''')
results = cur.fetchall()
print(results)
con.close()

