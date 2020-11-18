#from main import places, events
from tkinter import *





def create_listbox(root, places, w):
    listbox_places = Listbox(root, selectmode=SINGLE, width=w)   # поле списка заведений
    for i in places:
        listbox_places.insert(END, i)   
    return listbox_places



