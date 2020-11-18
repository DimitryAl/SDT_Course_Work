import sqlite3
from tkinter import *
#from base_func import create_window, create_entry, create_button, create_listbox
from base_func import *
from start_window_events import btn_show_events_click, btn_add_place_click, btn_delete_place_click

# инициализация переменных
y_init = 50
x_init = 10
x_listbox = 400



# создаём или открываем файл с бд
# conn = sqlite3.connect("E:\\Dimas\\Study\\MAI\\5 term\\trpo\\SDT-Course-Work\\Data.bd")
# создаём курсор
# c = conn.cursor()
'''
# add row in db
c.execute("INSERT INTO table1 VALUES ('ДК МАИ', 'чипирование', 'прививка', '16.11.2020', '18.24', 100, 99, 322.69, 'Петров Петр Петрович', '25')")
conn.commit()
conn.close()
'''
'''
# создаём таблицы 
c.execute("""CREATE TABLE table1(
    place TEXT,
    type TEXT,
    name TEXT,
    date TEXT,
    time TEXT,
    all_tickets INTEGER,
    sold_tickets INTEGER,
    price REAL,
    full_name TEXT,
    age INTEGER)
    """)
'''

# c.execute("SELECT * FROM table1")
# print(c.fetchall())
'''
file_places = open('list_of_places.txt', 'r+', encoding='utf-8-sig')
file_events = open('events.txt', 'r+', encoding='utf-8-sig')

for line in file_places:
    if line not in places:
        if '\n' in line:
            line=line.replace("\n", "")
        places.append(line)
'''

# print(events)
'''
for i in range(len(places)):
    events.update({places[i]: []})
events.update({'circus1':[1,2,3]})
'''

# главное окно
root_init = create_window("start window", str(600), str(300), str(300), str(300)) # главное окно
<<<<<<< HEAD
listbox_places = create_listbox(root_init,  30)  # список заведений
=======
listbox_places = create_listbox(root_init, 'place', 30)  # список заведений
>>>>>>> 418d6b0ab9b66f7d24d84c3a2f49b8d57b34a7f7
#scroll = Scrollbar(root_init)
ent_input = create_entry(root_init, 30)
btn_add_place = create_button(root_init, "Add place", 25)
bnt_delete_place = create_button(root_init, "delete place", 25)
btn_show_events = create_button(root_init, "show events", 25)
lbl = create_label(root_init, 30, 'list of places')

# размещение виджетов на стартовом окне
ent_input.place(x=x_init, y=y_init)
#scroll.place(x=x_listbox+185, y=y_init)
listbox_places.place(x=x_listbox, y=y_init)
btn_add_place.place(x=x_init, y=y_init+30)
bnt_delete_place.place(x=x_init, y=y_init+80)
btn_show_events.place(x=x_init, y=y_init+130)
lbl.place(x=x_listbox-10, y=y_init-20)

# configs
#scroll.config(command=listbox_places.yview)
#listbox_places.config(yscrollcommand=scroll.set)

# события на стартовом окне
<<<<<<< HEAD
# btn_add_place.config(command=lambda: btn_add_place_click(ent_input, places, listbox_places, events))
# bnt_delete_place.config(command=lambda: btn_delete_place_click(listbox_places, places, events))
=======
'''
btn_add_place.config(command=lambda: btn_add_place_click(ent_input, places, listbox_places, events))
bnt_delete_place.config(command=lambda: btn_delete_place_click(listbox_places, places, events))
>>>>>>> 418d6b0ab9b66f7d24d84c3a2f49b8d57b34a7f7

btn_show_events.config(command=lambda: btn_show_events_click())
'''
root_init.mainloop()


#print(places)
#print(events)
#file_places.close()
#file_events.close()
print("done")


'''

    listbox_events = Listbox(root, selectmode=SINGLE)   # поле списка событий

btn_dates = Button(root,  text='dates', command=lambda: btn_dates_click(events))                        # показывает мероприятия отсортированные по дате
btn_more = Button(root, width=10, text='more', command=lambda: btn_more_click(listbox_events))
btn_show_events = Button(root, width=10, text='show events', command=lambda: btn_show_events_click(listbox_places, listbox_events, events))    # кнопка для вывода мероприятий
btn_add_place = Button(root, width=10, text='add place', command=lambda: btn_add_place_click(ent_input, places, listbox_places, events))        # кнопка для добавления заведения
btn_add_event = Button(root, width=10, text='add event', command=lambda: btn_add_event_click(listbox_places, events))       # кнопка для добавления события
#btn_show_places = Button(root, width=10, text='show places')    # кнопка для вывода списка заведений


listbox_places.pack(side=RIGHT)
listbox_events.pack(side=RIGHT)
label.pack()
ent_input.pack()
btn_add_place.pack()
btn_show_events.pack()
btn_add_event.pack()
btn_more.pack()
btn_dates.pack()


root.mainloop()
'''
#print(events)
