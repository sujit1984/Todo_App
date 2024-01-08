def get_todo_tasks(filepath="todo_list.txt"):
    """ Read the current content of the todo_list.txt file and return its contents"""
    with open(filepath, 'r') as local_file:
        local_todos = local_file.readlines()
    return local_todos

def set_todo_tasks(todos_arg,filepath="todo_list.txt"):
    """ Write the new or updated tasks to a file todo_list.txt"""
    with open(filepath, 'w') as local_file:
        local_file.writelines(todos_arg)