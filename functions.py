def read_todos(filepath="files/todos.txt"):
    with open(filepath, 'r') as local_file:
        local_todos = local_file.readlines()
    return local_todos


def write_todos(todos_arg, filepath="files/todos.txt"):
    with open(filepath, 'w') as local_file:
        local_file.writelines(todos_arg)