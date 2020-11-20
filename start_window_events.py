from tkinter import *
import sqlite3

def btn_show_events_click():
    import event_window


def btn_add_place_click(text, places, listbox_places, events):
    if text.get() == "":
        return
    if text.get() not in places:
        places.append(text.get())
    events.update({text.get(): []})
    text.delete(0, last=END)
    listbox_places.delete(0, last=END)
    for i in places:
        listbox_places.insert(END, i)


def btn_delete_place_click(listbox_):
    temp = listbox_.curselection()
    if temp == ():
        return
    temp = listbox_.get(temp)
    listbox_.delete(listbox_.curselection())
    
    conn = sqlite3.connect("Data.bd")
    c = conn.cursor()
    #c.execute("""DELETE FROM table1 WHERE place LIKE '%temp%'""")
    c.execute("DELETE FROM table1 where place = ? ", (temp,))
    conn.commit()
    conn.close()   
    
