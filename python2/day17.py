import functions
from functions import get_todos, write_todos

import PySimpleGUI as aa

label = aa.Text("type in todo")
input_box = aa.InputText(tooltip ="enter todo", key = "todo")
add_button = aa.Button("add")
list_box = aa.Listbox(values = functions.get_todos(), key = 'todos',
                      enable_events =True, size = [45, 10])
edit_button = aa.Button('edit')

window = aa.Window("my todo app",
                   layout = [[label], [input_box, add_button], [list_box, edit_button]],
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

        case "edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values = todos)

        case "todo":
            window['todos'].update(value= values[todos])

        case aa.WIN_CLOSED:
            break



window.close()


