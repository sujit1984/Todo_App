import streamlit as st
import methods


tasks = methods.get_todo_tasks()
def add_task():
    task = st.session_state["new_task"] + "\n"
    tasks.append(task)
    methods.set_todo_tasks(tasks)

st.title("My Daily Tasklist")

#st.checkbox("First task")

for task in tasks:
    st.checkbox(task)

st.text_input(label="Add a new task", placeholder="New task",
              on_change=add_task, key="new_task")