import sqlite3

con = sqlite3.connect('SQL/db_video_type_slogan.sqlite')
cur = con.cursor()
result = cur.execute('''
    SELECT
        video_products.title, slogans.slogan_text, product_types.title, COUNT(*)
    FROM
        video_products
    LEFT JOIN slogans ON video_products.slogan_id = slogans.id
    LEFT JOIN product_types ON video_products.type_id = product_types.id
    GROUP BY product_types.id
''')
# qwe = cur.fetchall()
# print(qwe)
print('-----------------')
for i in result:
    print(i)
con.close()
