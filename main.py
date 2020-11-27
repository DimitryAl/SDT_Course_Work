import sqlite3
from tkinter import *

from base_func import create_window, create_entry, create_button, create_listbox, create_label
from start_window_events import btn_show_events_click, btn_add_place_click, btn_delete_place_click


# создаём или открываем файл с бд
conn = sqlite3.connect("Data.bd")
#создаём курсор
c = conn.cursor()

# создаём таблицы 
c.execute("""CREATE TABLE IF NOT EXISTS Places(
    id INTEGER,
    name TEXT
    )
    """)
conn.commit()
c.execute("""CREATE TABLE IF NOT EXISTS Events(
    id INTEGER,
    place_id INTEGER,
    type TEXT,
    name TEXT,
    date TEXT,
    time TEXT,
    available_tickets INTEGER,
    sold_tickets INTEGER,
    price REAL
    )
    """)
conn.commit()
c.execute("""CREATE TABLE IF NOT EXISTS Visitors(
    name TEXT,
    age INTEGER,
    work_place TEXT,
    event_id INTEGER
    )
    """
)
conn.commit()
conn.close()

# инициализация переменных
y_init = 25
x_init = 10
x_listbox = 400

# главное окно
root_init = create_window("start window", str(600), str(400), str(600), str(300)) # главное окно
listbox_places = create_listbox(root_init, 'name', 'Places', 30)  # список заведений
listbox_date_search = create_listbox(root_init, 'date', 'Events', 30)
ent_date_search = create_entry(root_init, 25)
ent_add_place = create_entry(root_init, 25)
btn_add_place =create_button(root_init, 'Add place', 20)
bnt_delete_place = create_button(root_init, "delete place", 25)
btn_show_events = create_button(root_init, "show events", 25)
btn_date_search = create_button(root_init, "Date search", 21)
lbl = create_label(root_init, 30, 'list of places')

# размещение виджетов на стартовом окне
ent_date_search.place(x=x_init, y=y_init)
ent_add_place.place(x=x_init+225, y=y_init)
listbox_places.place(x=x_listbox, y=y_init)
listbox_date_search.place(x=x_init, y=y_init+60)
btn_add_place.place(x=x_init+225, y=y_init+30)
bnt_delete_place.place(x=x_listbox, y=y_init+220)
btn_show_events.place(x=x_listbox, y=y_init+260)
btn_date_search.place(x=x_init, y=y_init+30)
lbl.place(x=x_listbox-10, y=y_init-20)

# события на стартовом окне
btn_add_place.config(command=lambda: btn_add_place_click(ent_add_place, listbox_places))
bnt_delete_place.config(command=lambda: btn_delete_place_click(listbox_places))


root_init.mainloop()

conn = sqlite3.connect("Data.bd")
c = conn.cursor()
c.execute("""SELECT * FROM Places""")
places = c.fetchall()
for i in places:
    print(i)