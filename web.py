import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():  # when user presses enter or any other key function is called
    todo = st.session_state["new_todo"] + "\n"  # session_state is a dictionary name
    # print(todo)  # prints whatever value in text_input
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app will increase the productivity.")

for index, todo in enumerate(todos):
    # st.checkbox(todo, key="hello")
    checkbox = st.checkbox(todo, key=todo)  # key=todo represents all todos with true or false
    if checkbox:
        # print(checkbox)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label='', placeholder="add new todo",  # label argument is compulsory
              on_change=add_todo, key="new_todo")  # on_change is for calling add_todo function

# print(st.session_state)  # session_state is a dictionary
# print("Hello")

# st.session_state  # shows the value of all widgets with key on the browser page
