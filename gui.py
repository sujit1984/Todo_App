from methods import get_todo_tasks, set_todo_tasks
import PySimpleGUI as sg


label = sg.Text("Enter the Task")
input_box = sg.InputText(tooltip="Enter the todo task", key = "Task")
add_button = sg.Button("Add")
window = sg.Window("To Do App",
                   layout = [[label],[input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = get_todo_tasks()
            new_task = values["Task"] + "\n"
            todos.append(new_task)
            set_todo_tasks(todos)
        case sg.WIN_CLOSED:
            break

window.close()
