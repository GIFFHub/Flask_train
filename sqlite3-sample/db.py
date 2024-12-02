import os
import sqlite3


base_dir = os.path.dirname(__file__)
database = os.path.join(base_dir, 'data.sqlite')


conn = sqlite3.connect(database)
print('-----------connect------------')
print()


cur = conn.cursor()
drop_sql = """
    DROP TABLE IF EXISTS items;
"""
cur.execute(drop_sql)
print('(1) 対象テーブルがあれば削除')


create_sql = """
    CREATE TABLE items(
        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name STRING UNIQUE NOT NULL,
        price INTEGER NOT NULL
        )
    """
cur.execute(create_sql)
print('(2) create table')


insert_sql = """
    INSERT INTO items (item_name, price) VALUES(?, ?)
    """
insert_data_list = [
    ('団子', 100), ('肉まん', 150), ('どら焼き', 200)
]
cur.executemany(insert_sql, insert_data_list)

conn.commit()

print('(3) データ登録：実行')

select_all_sql = """
    SELECT * FROM items
"""

cur.execute(select_all_sql)

print('(4) -------全件取得：実行-------')
data = cur.fetchall()
print(data)

select_one_sql = """
    SELECT * FROM items WHERE item_id = ?
    """

id = 3
cur.execute(select_one_sql, (id,))
print('(5) ------1件取得：実行')
data = cur.fetchone()
print(data)

update_sql = """
    UPDATE items SET price=? WHERE item_id=?
"""

price = 500
id = 1
cur.execute(update_sql, (price, id))
print('(6) ------データ更新：実行-------')

conn.commit()
cur.execute(select_one_sql, (id,))
data = cur.fetchone()
print('確認のため１件取得：実行', data)

delete_sql = """
    DELETE FROM items WHERE item_id=?
    """
id = 3
cur.execute(delete_sql, (id,))

conn.commit()

print('(7) ------データ削除：実行-------')
cur.execute(select_all_sql)
data = cur.fetchall()
print('確認のため全件取得：実行', data)

conn.close()
print()

print('--------close Connection -------')
