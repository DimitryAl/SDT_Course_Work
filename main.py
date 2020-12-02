import sqlite3
from prettytable import PrettyTable
from prettytable import from_db_cursor


def func1():
    conn = sqlite3.connect('Data.bd')
    c = conn.cursor()
    c.execute("SELECT 'вид заведения' FROM Places")
    table = from_db_cursor(c)
    print(table)
    conn.close()


def func2():
    conn = sqlite3.connect('Data.bd')
    c = conn.cursor()
    c.execute("SELECT * FROM Events")
    table = from_db_cursor(c)
    print(table)
    conn.close()

# создаём или открываем файл с бд
conn = sqlite3.connect("Data.bd")
#создаём курсор
c = conn.cursor()

# создаём таблицы 
c.execute("""CREATE TABLE IF NOT EXISTS Places(
    id INTEGER,
    'вид заведения' TEXT
    )
    """)
conn.commit()
c.execute("""CREATE TABLE IF NOT EXISTS Events(
    id INTEGER,
    place_id INTEGER,
    вид TEXT,
    название TEXT,
    'дата проведения' TEXT,
    время TEXT,
    'имеющиеся билеты' INTEGER,
    'проданые билеты' INTEGER,
    цены REAL
    )
    """)
conn.commit()
c.execute("""CREATE TABLE IF NOT EXISTS Visitors(
    фио TEXT,
    возраст INTEGER,
    'место работы' TEXT,
    event_id INTEGER
    )
    """)
conn.commit()
conn.close()


print('1)Вывести список заведений')
print('2)Вывести список мероприятий')

while True:
    n = input()

    if n == '1':
        func1()

    if n == '2':
        func2()

    if n == '0':
        break