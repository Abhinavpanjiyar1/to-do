import functions
from functions import get_todos, write_todos

import PySimpleGUI as aa

label = aa.Text("type in todo")
input_box = aa.InputText(tooltip ="enter todo", key = "todo")
add_button = aa.Button("add")

window = aa.Window("my todo app",
                   layout = [[label], [input_box, add_button]],
                   font =('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case aa.WIN_CLOSED:
            break



window.close()


