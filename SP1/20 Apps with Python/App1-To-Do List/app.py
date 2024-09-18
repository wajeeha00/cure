import functions as f
import FreeSimpleGUI as gui
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt",'w') as file:
        pass

gui.theme("DarkPurple4")

clock = gui.Text("", key = "clock")
label = gui.Text("Type in a To-Do")
input_box = gui.InputText(tooltip = "Enter To-Do", key = "todo")
add_button = gui.Button("Add")
list_box = gui.Listbox(values=f.get_todos(), key = "todos", enable_events=True, size=[45,10], font=("",20,"italic"))
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")

window = gui.Window("My To-Do App", layout = [[clock],
                                              [label], 
                                              [input_box, add_button],
                                              [list_box, edit_button, complete_button],
                                              [exit_button]], font = ("Helvetica",20))

while True:
    event, values = window.read(timeout = 200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = f.get_todos()
            todos.append(values["todo"]+'\n')
            f.write_todos(todos)    
            window['todos'].update(values = todos)

        case "Edit":
            try:
                todos = f.get_todos()
                todos[todos.index(values['todos'][0])] = values["todo"]+'\n'
                f.write_todos(todos)
                window['todos'].update(values = todos)
            except IndexError:
                gui.popup("Please select an item first", font = ("Helvetica",20))

        case "Complete":
            try:
                todos = f.get_todos()
                todos.remove(values['todos'][0])
                f.write_todos(todos)
                window["todos"].update(values = todos)
                window["todo"].update("")
            except IndexError:
                gui.popup("Please select an item first", font = ("Helvetica",20))

        case "todos":
            window['todo'].update(value = values['todos'][0])

        case gui.WIN_CLOSED | "Exit":
            break
window.close()