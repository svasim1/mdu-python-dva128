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

def openfile(file, mode):
    with open(f"{file}.txt", mode) as open_file:
        return
       
def save_todos(file, todos):
    with open(f"{file}.txt", "a") as save_file:
        for todo in todos:
            save_file.write(todo)

def load_todos(file):
    try:
        with open(f"{file}.txt", "r") as load_file:
            for line in load_file:
                todos.append(line)
    except FileExistsError:
        print("ERROR: FILE NOT FOUND")
    
def list_todo():    
    print("-----------------------------")
    for todo in todos:
        print(todo)
    print("-----------------------------")
def add_todo(todo):
    print("-----------------------------")
    todo = input("Todo description: ")
    return
def check_todo(todos):
    print('check')
    return
def delete_todo():
    print('delete')
    return

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

         