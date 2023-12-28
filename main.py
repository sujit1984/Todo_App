#user_prompt="Type add of show:"
#todos=[]
while True:
    user_action = input("Type add or show or edit or complete or exit ")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
            #todo = input("Enter a todo:") + '\n'
            todo = user_action[4:]
            file = open('./todo_list.txt','r')
            todos = file.readlines()
            file.close()

            todos.append(todo + '\n')
            file = open('./todo_list.txt','w')
            file.writelines(todos)
            file.close()
    elif user_action.startswith('show'):
            #file = open("./todo_list.txt",'r')
        with open("./todo_list.txt",'r') as file:
            todos = file.readlines()
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

            with open("./todo_list.txt",'r') as file:
                todos = file.readlines()
                #print("Todos before the modification",todos)

            new_task = input('Enter the new task:')
            todos[number] = new_task + '\n'

            with open("./todo_list.txt",'w') as file:
                todos = file.writelines(todos)

        except ValueError:
            print("Your command is not valid:")
            continue

    elif user_action.startswith('complete'):
        #num = int(input("Enter the task number to complete:"))'

        num = int(user_action[9:])
        del_num = num - 1
        with open("./todo_list.txt",'r') as file:
            todos = file.readlines()
        todos.pop(del_num)
        with open("./todo_list.txt",'w') as file:
            todos = file.writelines(todos)

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid")



#name = input("Enter your name:")
#print(name.capitalize())
