import streamlit as st
import functions as f

todos = f.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]+'\n'
    todos.append(todo)
    f.write_todos(todos)

def complete_todo():
    pass

st.title("My Todo App")
st.subheader("This is my to-do App")
st.write("This app is to improve you productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        f.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a To-Do", placeholder="Add a new To-Do..",
              on_change=add_todo, key='new_todo')
