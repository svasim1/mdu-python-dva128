import os

todos = ["[X] Plugga", "[ ] Städa", "[ ] Andas", "[ ] Kalle Kula"]
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
       
def save_todos():
    file = "todos"
    with open(f"{file}.txt", "a", encoding="utf-8") as save_file:
        for todo in todos:
            save_file.write(f"{todo}\n")

def load_todos(file):
    try:
        with open(f"{file}.txt", "r") as load_file:
            for line in load_file:
                todos.append(line.replace("\n", ""))
    except FileExistsError:
        print("ERROR: FILE NOT FOUND")
    
def list_todo():    
    print("-----------------------------")
    for todo in todos:
        print(todo)
    print("-----------------------------")
    
def add_todo():
    print("-----------------------------")
    todo = input("Todo description: ")          
    todos.append(f"[ ] {todo}")
    
def check_todo():
    print("-----------------------------")
    for i in range(len(todos)):
        print(f"{i} | {todos[i]}")
    print("-----------------------------")
    index = int(input("Todo index > "))
    if todos[index][1] == ' ':
        new_line = todos[index].replace(' ','X',1)
        todos[index] = new_line
    else:
        new_line = todos[index].replace('X',' ',1)
        todos[index] = new_line

def delete_todo():
    print("-----------------------------")
    for i in range(len(todos)):
        
        print(f"{i} | {todos[i]}")
    print("-----------------------------")
    index = input("Todo index > ")
    del todos[int(index)]

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
    
close = False
while not close:
    os.system('cls')
    instructions()
    operator = input('Selection > ')
    check_operator(operator)
    input("PRESS ENTER TO CONTINUE...")

         