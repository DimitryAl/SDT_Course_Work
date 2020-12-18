import sqlite3
from prettytable import PrettyTable
from prettytable import from_db_cursor


def Places_output():
    conn = sqlite3.connect('Data.bd')
    c = conn.cursor()
    c.execute("SELECT * FROM Places")
    table = from_db_cursor(c)
    print(table)
    conn.close()


def Events_output():
    conn = sqlite3.connect('Data.bd')
    c = conn.cursor()
    c.execute("SELECT * FROM Events")
    table = from_db_cursor(c)
    print(table)
    conn.close()


def Add_place():
    text = input('Введите название:\t')
    conn = sqlite3.connect('Data.bd')
    c = conn.cursor()
    c.execute("INSERT INTO Places (type) VALUES (?)", (text,))
    conn.commit()
    conn.close()


def Add_event():
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
    c.execute("""INSERT INTO Events (place_id, type, title, date, time, available_ticket, sold_ticket, price) VALUES (?,?,?,?,?,?,?,?)""",
                (id[0], tip, name, date, time, atickets, stickets, price))
    conn.commit()
    conn.close()


def Add_visitor():
    event = input('Введите мероприятие:\t')
    date = input('Введите дату проведения:\t')
    conn = sqlite3.connect('Data.bd')
    c = conn.cursor()
    c.execute("SELECT id FROM Events WHERE title=? AND date=?", (event, date))
    ID = c.fetchone()
    if ID == None:
        return
    name = input('Введите ФИО:\t')
    age = input('Введите возраст:\t')
    work = input('Введите профессию:\t')
    c.execute("""SELECT available_ticket, sold_ticket FROM Events WHERE title=? AND date=?""", (event, date))
    tickets = c.fetchone()
    if tickets[0] == 0:
        print('На данное мероприятие все билеты проданы!')
        return
    available_tickets = tickets[0] - 1
    sold_tickets = tickets[1] + 1
    c.execute("""UPDATE Events SET available_ticket=?, sold_ticket=? WHERE id=? AND date=?""", (available_tickets, sold_tickets, ID[0], date))
    conn.commit()
    c.execute("""INSERT INTO Visitors (event_id,name, age, profession) VALUES (?,?,?,?)""", (ID[0], name, age, work))
    conn.commit()
    conn.close()


def Delete_place():
    place = input('Input place type:\t')
    conn = sqlite3.connect('Data.bd')
    c = conn.cursor()
    c.execute("""SELECT id FROM Places WHERE type=?""", (place,))
    place_id = c.fetchone()
    if place_id == None:
        print('Культурное заведение отсутствует в базе!')
        return
    c.execute("""SELECT id FROM Events WHERE place_id=?""", (place_id))
    event_id = c.fetchall()
    if event_id == None:
        print('Мероприятие отсутвует!')
        return
    for id in event_id:
        c.execute("""DELETE FROM Visitors WHERE event_id=?""", id)
        conn.commit()
    c.execute("""DELETE FROM Events WHERE place_id=?""", place_id)
    conn.commit()
    c.execute("""DELETE FROM Places WHERE type=?""", (place,))
    conn.commit()
    conn.close()


def Visitors_output():
    conn = sqlite3.connect('Data.bd')
    c = conn.cursor()
    c.execute("""SELECT e.title, e.date, v.name, v.age, v.profession FROM 'Visitors' v 
                INNER JOIN 'Events' e ON v.event_id=e.id """)
    table = from_db_cursor(c)
    print(table)
    conn.close()


def Delete_event():
    title = input('Введите название мероприятия:\t')
    date = input('Введите дату мероприятия:\t')

    conn = sqlite3.connect('Data.bd')
    c = conn.cursor()
    c.execute("""SELECT id FROM Events WHERE title=? AND date=? """, (title, date))
    ID = c.fetchone()
    if ID == None:
        print('Мероприятие отсутствует!')
        return
    c.execute("""DELETE FROM Visitors WHERE event_id=?""", ID)
    conn.commit()
    c.execute("""DELETE FROM Events WHERE id=?""", ID)
    conn.commit()
    conn.close()

def Delete_visitor():
    name = input('Имя посетителя\t')
    title = input('Введите название мероприятия\t')
    date = input('Введите дату\t')
    conn = sqlite3.connect('Data.bd')
    c = conn.cursor()
    c.execute("""SELECT id FROM Events WHERE title=? AND date=?""", (title, date))
    ID = c.fetchone()
    if ID == None:
        print('Такого мероприятия нет!')
        return
    #c.execute("""SELECT available_ticket, sold_ticket FROM Events WHERE title=? AND date=?""", (name, date))
    c.execute("""SELECT available_ticket, sold_ticket FROM Events WHERE id=?""", (ID[0],))
    tickets = c.fetchone()
    available_tickets = tickets[0] + 1
    sold_tickets = tickets[1] - 1
    c.execute("""UPDATE Events SET available_ticket=?, sold_ticket=? WHERE id=? AND date=?""", (available_tickets, sold_tickets, ID[0], date))
    conn.commit()
    c.execute("""DELETE FROM Visitors WHERE name=? AND event_id=?""", (name, ID[0]))
    conn.commit()
    conn.close()


def Date_search():
    date = input('Введите дату\t')

    conn = sqlite3.connect('Data.bd')
    c = conn.cursor()
    c.execute("""SELECT * FROM Events WHERE date=? """, (date,))
    table = from_db_cursor(c)
    print(table)
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
    available_ticket INTEGER,
    sold_ticket INTEGER,
    price REAL,
    FOREIGN KEY(place_id) REFERENCES Places(id)
    )
    """)
conn.commit()
c.execute("""CREATE TABLE IF NOT EXISTS Visitors(
    event_id INTEGER,
    name TEXT,
    age INTEGER,
    profession TEXT,
    FOREIGN KEY(event_id) REFERENCES Events(id)
    )
    """)
conn.commit()
conn.close()


print('1)Вывести список культурных заведений')
print('2)Вывести список мероприятий')
print('3)Вывести всех посетителей')
print('4)Поиск по дате')
print('0)Выход')
n = input()
while True:
    
    if n == '0':
        break

    if n == '1':
        Places_output()
        while True:
            print('1)Добавить культурное заведение')
            print('2)Удалить заведение')
            print('0)Назад')
            n = input()
            if n == '1':
                Add_place()
            if n == '2':
                Delete_place()
            if n == '0':
                break
            Places_output()

    if n == '2':
        Events_output()
        while True:
            print('1)Добавить мероприятие')
            print('2)Удалить мероприятие')
            print('0)Назад')
            n = input()
            if n == '1':
                Add_event()
            if n == '2':
                    Delete_event()
            if n == '0':
                break
            Events_output()

    if n == '3':
        Visitors_output()
        while True:
            print('1)Добавить посетителя')
            print('2)Удалить посетителя')
            print('0)Назад')
            n = input()
            if n == '1':
                Add_visitor()
            if n == '2':
                Delete_visitor()
            if n == '0':
                break
            Visitors_output()

    if n == '4':
        Date_search()
    
    print('\n')
    print('1)Вывести список культурных заведений')
    print('2)Вывести список мероприятий')
    print('3)Вывести всех посетителей')
    print('4)Поиск по дате')
    print('0)Выход')
    n = input()
