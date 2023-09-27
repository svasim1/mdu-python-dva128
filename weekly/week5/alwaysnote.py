# Imports necessary modules
import os
import json

# Opens notes.json and loads the contents into notes 
try:
    with open("notes.json", "r+", encoding="utf-8") as notes_file:
        notes = json.load(notes_file)
except FileNotFoundError:
    with open("notes.json", "w", encoding="utf-8") as notes_file:
        notes = {}
        print("INFO: Created notes.json, please restart the program.")

# Function to print the instructions
def instructions():
    header = """.: ALWAYSNOTE :.
-- gold edition --
******************
"""
    for note in notes:
        header += f"- {note}\n"
    header += """------------------
view | view note
add  | add note
rm   | remove note
exit | exit program
------------------"""
    print(header)
    
# Function to view a note
def view_note():
    print("------------------")
    search = input("title > ")

    note_desc = notes.get(search)
    if note_desc is not None:
        print(f"""------------------
{note_desc}
------------------""")
    else:
        print("""------------------
ERROR: Unknown note
------------------""")
    
# Function to add a note
def add_note():
    print("------------------")
    title = input("title > ")
    desc = input("descr > ")
    
    notes[title] = desc
    
    print("""------------------
INFO: Note added
------------------""")
    with open("notes.json", "w", encoding="utf-8") as notes_file:
        json.dump(notes, notes_file)

# Function to remove a note 
def rm_note():
    rm_title = input("title > ")
    
    if rm_title in notes:
        del notes[rm_title]
        print("""------------------
INFO: Note deleted
------------------""")
        with open("notes.json", "w", encoding="utf-8") as notes_file:
            json.dump(notes, notes_file)
    else:
        print(f"ERROR: Unknown note")

# Function to check the user input
def check_operator(operator):
    if operator.lower() == "view":
        view_note()
    elif operator.lower() == "add":
        add_note()
    elif operator.lower() == "rm":
        rm_note()
    elif operator.lower() == "exit":
        exit()
    else:
        print(f"ERROR: Invalid operator ({operator})")

# Main loop
while True:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    instructions()
    operator = input("menu > ")
    check_operator(operator)
    input("Press enter to continue...")
