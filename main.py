import sqlite3
from prettytable import PrettyTable
from prettytable import from_db_cursor


def func1():
    conn = sqlite3.connect('Data.bd')
    c = conn.cursor()
    
    c.execute("SELECT * FROM Places")
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


def func3():
    text = input('Введите название:\t')
    conn = sqlite3.connect('Data.bd')
    c = conn.cursor()
    c.execute("INSERT INTO Places (type) VALUES (?)", (text,))
    conn.commit()
    conn.close()


def func4():
    place = input('Введите место проведения:\t')
    conn = sqlite3.connect('Data.bd')
    c = conn.cursor()
    c.execute("SELECT id FROM Places WHERE type=?", (place,))
    id = c.fetchone()
    if id == None:
        return
    tip = input('Введите вид мероприятия:\t')
    name = input('Введите название мероприятия:\t')
    date = input('Введите дату мероприятия:\t')
    time = input('Введите время мероприятия:\t')
    atickets = int(input('Введите кол-во доступных билетов мероприятия:\t'))
    stickets = int(input('Введите кол-во проданных билетов мероприятия:\t'))
    price = float(input('Введите цену билета на мероприятия:\t'))
    c.execute("""INSERT INTO Events (place_id, type, title, date, time, aticket, sticket, price) VALUES (?,?,?,?,?,?,?,?)""",
                (id[0], tip, name, date, time, atickets, stickets, price))
    conn.commit()
    conn.close()


def func5():
    event = input('Введите мероприятие:\t')
    conn = sqlite3.connect('Data.bd')
    c = conn.cursor()
    c.execute("SELECT id FROM Events WHERE title=?", (event,))
    id = c.fetchone()
    if id == None:
        return
    name = input('Введите ФИО:\t')
    age = input('Введите возраст:\t')
    work = input('Введите место работы:\t')
    #изменить кол-во билетов
    c.execute("""INSERT INTO Visitors (event_id,name, age, work) VALUES (?,?,?,?)""", (id[0], name, age, work))
    conn.commit()
    conn.close()


def func6():
    place = input('Input place type:\t')
    conn = sqlite3.connect('Data.bd')
    c = conn.cursor()
    c.execute("""SELECT id FROM Places WHERE type=?""", (place,))
    place_id = c.fetchone()
    if place_id == None:
        print('fuck off')
        return
    c.execute("""SELECT id FROM Events WHERE place_id=?""", (place_id))
    event_id = c.fetchall()
    if event_id == None:
        print('fuck off')
        return
    for id in event_id:
        c.execute("""DELETE FROM Visitors WHERE event_id=?""", id)
        conn.commit()
    c.execute("""DELETE FROM Events WHERE place_id=?""", place_id)
    conn.commit()
    c.execute("""DELETE FROM Places WHERE type=?""", (place,))
    conn.commit()
    conn.close()


def func10():
    conn = sqlite3.connect('Data.bd')
    c = conn.cursor()
    c.execute("""SELECT e.title, v.name, v.age, v.work FROM 'Visitors' v 
                INNER JOIN 'Events' e ON v.event_id=e.id """)
    table = from_db_cursor(c)
    print(table)
    conn.close()


def func7():
    title = input('Введите название мероприятия:\t')
    date = input('Введите дату мероприятия:\t')

    conn = sqlite3.connect('Data.bd')
    c = conn.cursor()
    c.execute("""SELECT id FROM Events WHERE title=? AND date=? """, (title, date))
    id = c.fetchone()
    if id == None:
        print('fuck off')
        return
    c.execute("""DELETE FROM Visitors WHERE event_id=?""", id)
    conn.commit()
    c.execute("""DELETE FROM Events WHERE id=?""", id)
    conn.commit()
    conn.close()


# создаём или открываем файл с бд
conn = sqlite3.connect("Data.bd")
#создаём курсор
c = conn.cursor()

# создаём таблицы 
c.execute("""CREATE TABLE IF NOT EXISTS Places(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT
    )
    """)
conn.commit()
c.execute("""CREATE TABLE IF NOT EXISTS Events(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    place_id INTEGER,
    type TEXT,
    title TEXT,
    date TEXT,
    time TEXT,
    aticket INTEGER,
    sticket INTEGER,
    price REAL,
    FOREIGN KEY(place_id) REFERENCES Places(id)
    )
    """)
conn.commit()
c.execute("""CREATE TABLE IF NOT EXISTS Visitors(
    event_id INTEGER,
    name TEXT,
    age INTEGER,
    work TEXT,
    FOREIGN KEY(event_id) REFERENCES Evens(id)
    )
    """)
conn.commit()
conn.close()


print('1)Вывести список заведений')
print('2)Вывести список мероприятий')
print('3)Добавить вид культурного заведения')
print('4)Добавить мероприятие')
print('5)Добавить посетителя')
print('6)Удалить заведение')
print('7)Удалить мероприятие')
print('8)Удалить посетителя')
print('9)Поиск по дате')
print('10)Вывести всех посетителей')
print('0)Выход')

while True:
    n = input()

    if n == '1':
        func1()

    if n == '2':
        func2()

    if n == '3':
        func3()

    if n == '4':
        func4()

    if n == '5':
        func5()

    if n == '10':
        func10()

    if n == '6':
        func6()

    if n == '7':
        func7()

    if n == '0':
        break

