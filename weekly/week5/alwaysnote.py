import os
import json

notes = {}

def instructions():
    header = """.: ALWAYSNOTE :.
-- gold edition --
******************
- Important
- Notes from lecture
------------------
view | view note
add  | add note
rm   | remove note
exit | exit program
------------------
"""
    print(header)
    
def view_note():
    
    try:
        with open("notes.json", "r", encoding="utf-8") as notes_file:
            notes = json.load(notes_file)
    except FileNotFoundError:
        print("ERROR: FILE NOT FOUND")

    view_title = input("title > ")
    
    for note_title, note_desc in notes.items():
        if note_title == view_title:
            print(f"""------------------
{note_desc}
------------------""")
        else:
            print("""------------------
ERROR: Unknown note
------------------""")
    
def add_note():
    print("------------------")
    title = input("title > ")
    desc = input("descr > ")
    
    notes[title] = desc
    
    print("""------------------
INFO: Note added
------------------""")
    
    try:
        with open("notes.json", "w", encoding="utf-8") as notes_file:
            json.dump(notes, notes_file)
    except FileNotFoundError:
        print("ERROR: FILE NOT FOUND")
        
def rm_note():
    try:
        with open("notes.json", "r", encoding="utf-8") as notes_file:
            notes = json.load(notes_file)
    except FileNotFoundError:
        print("ERROR: FILE NOT FOUND")

    rm_title = input("title > ")
    
    if rm_title in notes:
        del notes[rm_title]
        print("""------------------
INFO: Note removed
------------------""")
        
        try:
            with open("notes.json", "w", encoding="utf-8") as notes_file:
                json.dump(notes, notes_file)
        except FileNotFoundError:
            print("ERROR: FILE NOT FOUND")
    else:
        print(f'ERROR: Note "{rm_title}" not found')
    
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
        print(f'ERROR: Invalid operator ({operator})')

while True:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    instructions()
    operator = input("menu > ")
    check_operator(operator)
    input("PRESS ENTER TO CONTINUE...")
