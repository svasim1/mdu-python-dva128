# Import necessary modules
import os
import json

# Initialize an empty list to store todos
todos = []

# Function to display instructions for using the application
def instructions():
    header = """
    *****************************
               TODOIFY
    -----------------------------
    list   | List todos
    add    | Add todo
    check  | Check todo
    delete | Delete todo
    -----------------------------
    save   | Save todos to file
    load   | Load todos from file
    -----------------------------
    """
    print(header)

# Function to save the todos to a file in JSON format
def save_todos():
    file = "todos"
    with open(f"{file}.txt", "w", encoding="utf-8") as save_file:
        save_file.write(json.dumps(todos))

# Function to load todos from a file
def load_todos(file):
    try:
        with open(f"{file}.txt", "r") as load_file:
            global todos
            todos = json.loads(load_file.readline())
    except FileNotFoundError:
        print("ERROR: FILE NOT FOUND")

# Function to list all the todos
def list_todo():
    print("-----------------------------")
    for todo in todos:
        print(todo)
    print("-----------------------------")

# Function to add a new todo
def add_todo():
    print("-----------------------------")
    todo = input("Todo description: ")
    todos.append(f"[ ] {todo}")

# Function to check/uncheck a todo as done
def check_todo():
    
    print("-----------------------------")
    for i in range(len(todos)):
        print(f"{i} | {todos[i]}")
    print("-----------------------------")
    
    try:
        index = int(input("Todo index > "))
    except ValueError:
        print(f'ERROR: Please input a valid number')
        return
    
    try:
        if todos[index][1] == ' ':
            new_line = todos[index].replace(' ', 'X', 1)
            todos[index] = new_line
        else:
            new_line = todos[index].replace('X', ' ', 1)
            todos[index] = new_line
    except IndexError:
        print(f"ERROR: Index ({index}) out of range")

# Function to delete a todo
def delete_todo():
    
    print("-----------------------------")
    for i in range(len(todos)):
        print(f"{i} | {todos[i]}")
    print("-----------------------------")
    
    try:
        index = int(input("Todo index > "))
    except ValueError:
        print(f'ERROR: Please input a valid number')
        return
    
    try:
        del todos[index]
    except IndexError:
        print(f'ERROR: Index ({index}) out of range')

# Check the input and choose the right operator
def check_operator(input):
    if input.lower() == 'list':
        list_todo()
    elif input.lower() == 'add':
        add_todo()
    elif input.lower() == 'check':
        check_todo()
    elif input.lower() == 'delete':
        delete_todo()
    elif input.lower() == 'save':
        save_todos()
    elif input.lower() == 'load':
        load_todos("todos")
    elif input.lower() == 'exit':
        exit()
    else:
        print(f'ERROR: Invalid operator ({operator})')

# Define a variable to control the loop
close = False

# Main loop for user interaction
while not close:
    os.system('cls')  # Clears the screen
    instructions()  
    operator = input('Selection > ')
    check_operator(operator)
    input("PRESS ENTER TO CONTINUE...")
