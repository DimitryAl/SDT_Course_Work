import sqlite3

from tkinter import *

def create_window(txt, width, height, x, y):
    root = Tk()                 # создаём окно
    root.title(txt)
    root.geometry(width+"x"+height+"+"+x+"+"+y)    # указываем размер окна
    root.resizable(False, False)
    # root.grab_set()
    root.focus_set()
    return root


def create_label(root, w, txt):
    label = Label(root, width=w, text=txt)         # поле для вывода текста 
    return label


def create_entry(root, w):
    ent = Entry(root, width=w)                        # строка для ввода текста
    return ent


def create_button(root, txt, w):
    btn = Button(root,  text=txt, width=w)
    return btn


def create_listbox(root, c_name, t_name, w):
    listbox_ = Listbox(root, selectmode=SINGLE, width=w)   # поле списка 
    conn = sqlite3.connect("Data.bd")
    c = conn.cursor()
    c.execute(f"""SELECT {c_name} FROM {t_name}""")
    places = c.fetchall()
    places = set(places)
    for place in places:
        listbox_.insert(END, place[0])    
    conn.close()
    return listbox_
