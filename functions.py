FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text filo and return the list of to-do items"""  # it is called doc-strings.
    # filepath = 'todos1.txt' will create an error, if reassigning a new value to variable, with not existing filo.
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


#  print(help(get_todos))  #  you can write doc-strings in your function like inbuilt func.


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to do items list in text filo."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


#  print("hello")

#  print(__name__)

if __name__ == "__main__":
    print("Hello")
