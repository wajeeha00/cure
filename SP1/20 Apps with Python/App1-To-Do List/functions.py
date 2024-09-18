FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    with open(filepath,'r') as file:
        todos_temp = file.readlines()
    return todos_temp

def write_todos(todos_arg,filepath = FILEPATH):
    with open(filepath,'w') as file:
        file.writelines(todos_arg)