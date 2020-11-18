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


<<<<<<< HEAD
def create_listbox(root, w):
    listbox_ = Listbox(root, selectmode=SINGLE, width=w)   # поле списка заведений
=======
def create_listbox(root, text, w):
    listbox_ = Listbox(root, selectmode=SINGLE, width=w)   # поле списка 
>>>>>>> 418d6b0ab9b66f7d24d84c3a2f49b8d57b34a7f7
    '''
    for i in listbox:
        listbox_.insert(END, i)   
    '''
    conn = sqlite3.connect("Data.bd")
    c = conn.cursor()
    c.execute(f"""SELECT {text} FROM table1""")
    places = set(c.fetchall())
    print(places)
    for place in places:
        listbox_.insert(END, place[0])    
    conn.commit()
    conn.close()
    return listbox_