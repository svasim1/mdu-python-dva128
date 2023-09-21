import os
import csv

people = {}

# Read the database
try:
    with open("database.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            people[row[0]] = {"forename": row[1], "surname": row[2], "gender": row[3], "year": row[4]}
except FileNotFoundError:
    print("ERROR: The 'database.csv' file was not found. Make sure it exists in the same directory as this script.")

# Print instructions
def instructions():
    header = """.: PEOPLE'S DATABASE :.
-----------------------
| get_id | Get person by ID
| scan_f | LIST PEOPLE BY FORENAME
| scan_s | LIST PEOPLE BY SURNAME
| exit   | Exit program
-----------------------"""
    print(header)

# Function to get person by ID
def get_id():
    id = input("ID = ")
    if id in people:
        print(f"""-----------------------
| ID:       {id}
| FORENAME: {people[id]["forename"]}
| SURNAME:  {people[id]["surname"]}
| GENDER:   {people[id]["gender"]}
| YEAR:     {people[id]["year"]}
-----------------------""")
    else:
        print(f"""-----------------------
| ERROR: ID not found ({id})
-----------------------""")
        
# Function to list people by forename
def scan_f():
    forename = input("FORENAME = ")
    print(f"""-----------------------
| SEARCH: {forename}
-----------------------""")
    for id in people:
        if people[id]["forename"] == forename:
            print(f"""| ID:       {id}
| FORENAME: {people[id]["forename"]}
| SURNAME:  {people[id]["surname"]}
| GENDER:   {people[id]["gender"]}
| YEAR:     {people[id]["year"]}
-----------------------""")
            
# Function to list people by surname
def scan_s():
    surname = input("SURNAME = ")
    print(f"""-----------------------
| SEARCH: {surname}
-----------------------""")
    for id in people:
        if people[id]["surname"] == surname:
            print(f"""| ID:       {id}
| FORENAME: {people[id]["forename"]}
| SURNAME:  {people[id]["surname"]}
| GENDER:   {people[id]["gender"]}
| YEAR:     {people[id]["year"]}
-----------------------""")

# Check operator
def check_operator(input):
    if input.lower() == "get_id":
        get_id()
    elif input.lower() == "scan_f":
        scan_f()
    elif input.lower() == "scan_s":
        scan_s()        
    elif input.lower() == "exit":
        exit()
    else:
        print(f'ERROR: Invalid operator ({operator})')

close = False

# Main loop for user interaction
while not close:
    os.system("cls")
    instructions()  
    operator = input('| menu > ')
    check_operator(operator)
    input("PRESS ENTER TO CONTINUE...")
