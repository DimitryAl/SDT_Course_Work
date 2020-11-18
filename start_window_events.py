from tkinter import *


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


def btn_delete_place_click(listbox_, places, events):
    temp = listbox_.curselection()
    if temp == ():
        return
    temp = listbox_.get(temp)
    places.pop(places.index(temp))
    events.pop(temp)
    listbox_.delete(0, END)
    for i in places:
        listbox_.insert(END, i)   
