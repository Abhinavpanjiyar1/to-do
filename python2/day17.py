import functions
from functions import get_todos, write_todos

import PySimpleGUI as aa
import time

aa.theme('black')
clock = aa.Text('' ,key ='clock')
label = aa.Text("type in todo")
input_box = aa.InputText(tooltip ="enter todo", key = "todo")
add_button = aa.Button("add")
list_box = aa.Listbox(values = functions.get_todos(), key = 'todos',
                      enable_events =True, size = [45, 10])
edit_button = aa.Button('edit')
complete_button = aa.Button('complete')
exit_button = aa.Button("exit")

window = aa.Window("my todo app",
                   layout = [[clock],
                             [label],
                             [input_box, add_button],
                             [list_box, edit_button, complete_button],
                             [exit_button]],
                   font =('Helvetica', 20))

while True:
    event, values = window.read(timeout = 500)
    window["clock"].update(value = time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values = todos)
            except IndexError:
                aa.popup("pls select an item first")
        case "complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values = todos)
                window['todo'].update(value = '')
            except IndexError:
                aa.popup("pls select an item first")
        case "exit":
            break

        case "todo":
            window['todos'].update(value= values['todos'][0])

        case aa.WIN_CLOSED:
            break



window.close()


