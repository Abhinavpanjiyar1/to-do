FILEPATH = "todos.txt"
def get_todos(filepath = FILEPATH):
    with open(filepath, 'r') as file_local :
        new_todos = file_local.readlines()
    return new_todos


def write_todos(todos_arg, filepath = FILEPATH, ):
    with open(filepath, 'w') as file :
        file.writelines(todos_arg)