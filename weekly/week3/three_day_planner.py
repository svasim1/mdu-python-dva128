import os

goal_today = "Run 5km"
goal_tomorrow = "Swim 1km"
goal_later = "Bike 10km"

def instructions():
    header = f""".: THREE DAY PLANNER :.
-----------------------
     WORKOUT GOALS!
   ONE DAY AT A TIME.
-----------------------
TODAY:      {goal_today} 
TOMORROW:   {goal_tomorrow}
LATER:      {goal_later}
-----------------------
n | Next day
c | Change goal
e | Exit program
-----------------------"""
    print(header)

def cycle():
    global goal_today
    global goal_tomorrow
    global goal_later
    goal_today = goal_tomorrow
    goal_tomorrow = goal_later
    goal_later = ""

def change_goal():
    global goal_today
    global goal_tomorrow
    global goal_later
    print("""-----------------------
0 | TODAY
1 | TOMORROW
2 | LATER
-----------------------""")
    index = input("Change goal for day > ")
    if index == "0":
        goal_today = input("Goal for today > ")
    elif index == "1":
        goal_tomorrow = input("Goal for tomorrow > ")
    elif index == "2":
        goal_later = input("Goal for later > ")
    else:
        print("""-----------------------
ERROR: Bad day
INFO:  Please enter a valid integer between 0 and 2.
-----------------------""")
        input("Press enter to continue...")

def check_operator(operator):
        if operator.lower() == "n":
            cycle()
        elif operator.lower() == "c":
            change_goal()
        elif operator.lower() == "e" or operator.lower() == "exit":
            exit()
        else:
            print(f"""-----------------------
ERROR: Unknown operator ({operator})
-----------------------""")
            input("Press enter to continue...")
            
os.system("cls")
while True:
    os.system("cls")
    instructions()
    operator = input("Operator > ")
    check_operator(operator)
