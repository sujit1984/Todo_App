from methods import get_todo_tasks, set_todo_tasks
import PySimpleGUI as sg


label = sg.Text("Enter the Task")
input_box = sg.InputText(tooltip="Enter the todo task", key = "Task")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=get_todo_tasks(), key="Task_List",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window("To Do App",
                   layout=[[label],[input_box, add_button],[list_box, edit_button]],
                   font=('Helvetica', 16))

while True:
    event, values = window.read()
    print(1,event)
    print(2, values)
    print(3, values["Task_List"])
    match event:
        case "Add":
            todos = get_todo_tasks()
            new_task = values["Task"] + "\n"
            todos.append(new_task)
            set_todo_tasks(todos)
            window['Task_List'].update(values=todos)
        case "Edit":
            task_to_edit = values["Task_List"][0]
            new_task = values["Task"]
            tasks = get_todo_tasks()
            index = tasks.index(task_to_edit)
            tasks[index] = new_task
            set_todo_tasks(tasks)
            window['Task_List'].update(values=tasks)
        case "Task_List":
            window['Task'].update(value=values['Task_List'][0])
        case sg.WIN_CLOSED:
            break

window.close()
