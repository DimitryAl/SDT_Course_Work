from tkinter import *
import sqlite3

def btn_show_events_click():
    import event_window


def btn_add_place_click(text, listbox_):
    if text.get() == "":
        return
    conn = sqlite3.connect("Data.bd")
    c = conn.cursor()
    c.execute("""SELECT name FROM Places""")
    places = c.fetchall()
    for i in range(len(places)):
        if text.get() in places[i]:
            return
    if len(places) == 0:
        ID = 0
    else:
        c.execute("""SELECT id FROM Places """)
        ids = c.fetchall()
        ID = -1 
        for i in range(len(ids)):
            temp = max(ids[i])
            if temp > ID:
                ID = temp
    ID += 1
    c.execute("""INSERT INTO Places VALUES (?, ?)""", (ID, text.get(),))
    conn.commit()
    conn.close()
    listbox_.delete(0, last=END)
    for i in places:
       listbox_.insert(END, i)
    listbox_.insert(END, text.get())
    text.delete(0, last=END)


def btn_delete_place_click(listbox_):
    temp = listbox_.curselection()
    if temp == ():
        return
    if type(listbox_.get(temp)) == str:
        temp = listbox_.get(temp)
    elif type(listbox_.get(temp)) == tuple:
        temp = listbox_.get(temp)[0]
    listbox_.delete(listbox_.curselection())
    conn = sqlite3.connect("Data.bd")
    c = conn.cursor()
    c.execute("""DELETE from Places WHERE name = (?)""", (temp,))
    conn.commit()
    conn.close()