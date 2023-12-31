def get_todo_tasks(filepath):
    with open(filepath, 'r') as local_file:
        local_todos = local_file.readlines()
    return local_todos

def set_todo_tasks(filepath, todos_arg):
    with open(filepath, 'w') as local_file:
        local_file.writelines(todos_arg)

# def set_todo_tasks():
#     with open("./todo_list.txt", 'w') as file:
#         todos = file.writelines(todos)

while True:
    user_action = input("Type add or show or edit or complete or exit ")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
            #todo = input("Enter a todo:") + '\n'
            todo = user_action[4:]
            todos = get_todo_tasks("todo_list.txt")

            todos.append(todo + '\n')
            set_todo_tasks("todo_list.txt", todos)

    elif user_action.startswith('show'):
            #file = open("./todo_list.txt",'r')
        todos= get_todo_tasks("todo_list.txt")
            #file.close()
            #new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item=item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todo_tasks("todo_list.txt")
                #print("Todos before the modification",todos)

            new_task = input('Enter the new task:')
            todos[number] = new_task + '\n'

            set_todo_tasks("todo_list.txt",todos)

        except ValueError:
            print("Your command is not valid:")
            continue

    elif user_action.startswith('complete'):
        try:
            num = int(user_action[9:])
            del_num = num - 1
            get_todo_tasks("todo_list.txt")
            todos.pop(del_num)
            set_todo_tasks("todo_list.txt",todos)

        except IndexError:
            print(f"There is no task with the number {num}")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid")

