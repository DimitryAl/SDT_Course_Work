from base_func import create_window, create_button, create_listbox
from main import listbox_places

y_init = 50
x_init = 10
x_listbox = 400 


# окно с событиями
root_events = create_window("Events", str(600), str(400), str(600), str(300))
listbox_events = create_listbox(root_events, 'type, name', 'Events', 30)
btn_add_event = create_button(root_events, "Add event", 25)
bnt_delete_event = create_button(root_events, "delete event", 25)
#btn_more = create_button(root_events, "show more", 25)



# размещение виджетов
btn_add_event.place(x=x_init, y=y_init+30)
bnt_delete_event.place(x=x_init, y=y_init+80)
#btn_more.place(x=x_init, y=y_init+130)
listbox_events.place(x=x_init+300,y=y_init)

#события


root_events.mainloop()