FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Gets to do list from text file"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Writes to do list to text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)



if __name__ == "__main__":
    print("Hello")
    print(get_todos())