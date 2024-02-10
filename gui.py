from methods import get_todo_tasks, set_todo_tasks
import PySimpleGUI as sg
import time

sg.theme("White")
clock = sg.Text('', key='clock')
label = sg.Text("Enter the Task")
input_box = sg.InputText(tooltip="Enter the todo task", key = "Task")
add_button = sg.Button(size=1, image_source='add.png',mouseover_colors="White",
                       tooltip="Add a new task", key='Add')
list_box = sg.Listbox(values=get_todo_tasks(), key="Task_List",
                      enable_events=True, size=[60, 10])
edit_button = sg.Button("Edit")
complete_button=sg.Button(size=1,image_source='complete.png',
                          tooltip="Complete the task", mouseover_colors="White", key="Complete")
exit_button=sg.Button("Exit")

window = sg.Window("To Do App",
                   layout=[[clock],
                       [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                            [exit_button]],
                   font=('Helvetica', 16))

while True:
    event, values = window.read(timeout=500)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
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
            try:
                task_to_edit = values["Task_List"][0]
                new_task = values["Task"]
                tasks = get_todo_tasks()
                index = tasks.index(task_to_edit)
                tasks[index] = new_task
                set_todo_tasks(tasks)
                window['Task_List'].update(values=tasks)
            except IndexError:
                sg.popup('Please select a task to edit', font=('Helvetica',16))

        case "Complete":
            try:
                task_to_complete = values["Task_List"][0]
                #new_task = values["Task"]
                tasks = get_todo_tasks()
                tasks.remove(task_to_complete)
                #tasks[index] = new_task
                set_todo_tasks(tasks)
                window['Task_List'].update(values=tasks)
                window['Task'].update(value='')
            except IndexError:
                sg.popup('Please select a task to complete', font=('Helvetica', 16))


        case "Task_List":
            window['Task'].update(value=values['Task_List'][0])

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()
