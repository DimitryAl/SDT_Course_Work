from base_func import create_window, create_button, create_listbox
from main import listbox_places

y_init = 50
x_init = 10
x_listbox = 400 


# окно с событиями
root_add = create_window("Add event", str(600), str(400), str(600), str(300))
listbox_events = create_listbox(root_add, 'type, name', 'Events', 30)
btn_add_event = create_button(root_add, "Add event", 25)
bnt_delete_event = create_button(root_add, "delete event", 25)