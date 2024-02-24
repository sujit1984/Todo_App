import streamlit as st

import methods
from methods import set_todo_tasks, get_todo_tasks


tasks = get_todo_tasks()
st.title("My Daily Tasklist")

#st.checkbox("First task")

for task in tasks:
    st.checkbox(task)

st.text_input(label="Add a new task", placeholder="New task")