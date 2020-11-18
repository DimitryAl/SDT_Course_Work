'''
from tkinter import *

from classes import Event


def extract(x):
    q = str(x.type)+str(x.name)+str(x.all_tickets)+str(x.sold_tickets)+str(x.price)+str(x.date)+str(x.time)
    return q


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


def btn_add_click(ttype, name, all_tickets, sold_tickets, price, date, time, events, temp, root2):
    new_event = Event(ttype.get(), name.get(), all_tickets.get(), sold_tickets.get(), price.get(), date.get(), time.get())
    temp2 = events[temp]
    temp2.append(new_event)
    root2.destroy()


def btn_add_event_click(listbox_places, events):
    # ls = ['type', 'name', 'all_tickets', 'sold_tickets', 'price', 'date', 'time']
    temp = listbox_places.get(listbox_places.curselection())

    root2 = Tk()
    root2.title("add event for " + str(temp))
    root2.geometry("400x300")
    label_ttype = Label(root2, text='type')
    ttype = Entry(root2, width=30)
    label_name = Label(root2, text='name')
    name = Entry(root2, width=30)
    label_all_tickets = Label(root2, text='all_tickets')
    all_tickets = Entry(root2, width=30)
    label_sold_tickets = Label(root2, text='sold_tickets')
    sold_tickets = Entry(root2, width=30)
    label_price = Label(root2, text='price')
    price = Entry(root2, width=30)
    label_date = Label(root2, text='date')
    date = Entry(root2, width=30)
    label_time = Label(root2, text='time')
    time = Entry(root2, width=30)
    label_ttype.grid(row=0, column=0)
    ttype.grid(row=0, column=1)
    label_name.grid(row=1, column=0)
    name.grid(row=1, column=1)
    label_all_tickets.grid(row=2, column=0)
    all_tickets.grid(row=2, column=1)
    label_sold_tickets.grid(row=3, column=0)
    sold_tickets.grid(row=3, column=1)
    label_price.grid(row=4, column=0)
    price.grid(row=4, column=1)
    label_date.grid(row=5, column=0)
    date.grid(row=5, column=1)
    label_time.grid(row=6, column=0)
    time.grid(row=6, column=1)

    btn_add = Button(root2, width=10, text='add', command=lambda: btn_add_click(ttype, name, all_tickets, sold_tickets, price, date, time, events, temp, root2))
    btn_add.grid(row=7, column=1)
    root2.mainloop()


def btn_show_events_click(listbox_places, listbox_events, events):
    temp = listbox_places.get(listbox_places.curselection())
    listbox_events.delete(0, last=END)
    for j in events[temp]:
        listbox_events.insert(END, extract(j))


def btn_more_click(listbox_events):
    root3 = Tk()
    root3.title("more")
    root3.geometry("400x300")

    temp = listbox_events.get(listbox_events.curselection())
    label = Label(root3)
    label.config(text=temp)
    label.pack()
    print(temp)


def btn_dates_click(events):
    root2 = Tk()
    root2.geometry("400x300")
    listbox_dates = Listbox(root2, selectmode=SINGLE)
    listbox_dates.pack()
    for j in events:
        for k in events[j]:
            print(extract(k))
            #listbox_dates.insert(extract(k))
            listbox_dates.insert(END, extract(k))
    print()