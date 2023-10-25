import requests
import os
import json

base_url = 'http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api'

# Function to print the header
def instructions():
    header = f"""{("*")*40}
{"FOOTBALL FRENZY".center(40)}
{"STAT VIEWER".center(40)}
{"1.0.0".center(40)}
{("-")*40}
| list | List all available seasons
| view | View table for season
{("-")*40}"""
    print(header)

# Function to fetch data from selected API
def request_handler(api_url):
    request = requests.get(api_url)
    
    if(request.status_code != 200):
        print("-"*40 + f"\n| API ERROR: {request.status_code}. \n| Please restart and try again.\n" + "-"*40)
        input("Press enter to continue...")
        exit()
    
    request = json.loads(request.text)
    return request

# Function to get wins, draws, losses and points
def save_season_data(api_url):
    data = request_handler(api_url)
    
    gamedays = data["gamedays"]
    teams = data["teams"]
    scoretable = {}
    
    # Creates a scorecard for each team
    for team in teams:
        scoretable[team] = [0, 0, 0, 0]
    
    # Updates the scorecard using the change_results() function
    for date in gamedays:
        change_results(scoretable, request_handler(api_url + "/" + date))
    return scoretable

# Function to change the values of the scorecard
def change_results(dic, data):
    # Takes out the list of games for the day that wass passed in
    matches = data["games"]
    
    # Loops through each match for the day
    for match in matches:
        # Saves the name of the home team, and their score
        home_score = match["score"]["home"]["goals"]
        home_team = match["score"]["home"]["team"]
        
        # Saves the name of the away team, and their score
        away_score = match["score"]["away"]["goals"]
        away_team = match["score"]["away"]["team"]

        if home_score > away_score:
            # Increse W by 1 and P by 3
            dic[home_team][0] += 1
            dic[home_team][3] += 3
            
            # Increase L by 1
            dic[away_team][2] += 1
            
        elif home_score < away_score:
            # Increase W by 1 and P by 3
            dic[away_team][0] += 1
            dic[away_team][3] += 3
            
            # Increase L by 1
            dic[home_team][2] += 1
            
        elif home_score == away_score:
            # Increase D by 1
            dic[home_team][1] += 1
            dic[away_team][1] += 1
            
            # Increase P by 1
            dic[home_team][3] += 1
            dic[away_team][3] += 1

# Function to list all available seasons
def list_seasons():
    seasons = request_handler(base_url)["seasons"]
    
    print("-"*40)
    for season in seasons:
        print("| " + season)
    print("-"*40)
    
# Function to view data from selected season
def view_season():
    print("-"*40)
    selected_year = input("| Year > ")
    if selected_year not in request_handler(base_url)["seasons"]:
        print("-"*40 + f"\n| ERROR: Season '{selected_year}' not found\n" + "-"*40)
        return
    
    scoretable = save_season_data(base_url + "/" + selected_year)
    
    # Recreates the dictionary in order by the fourth value in the array of value
    scoretable = dict(sorted(scoretable.items(), key=lambda item: item[1][3], reverse=True))
    
    print("*"*40 + "\n|")
    print(f"| {'Team'.ljust(26)}{'W'.ljust(7)}{'D'.ljust(7)}{'L'.ljust(7)}{'P'.ljust(7)}")
    print("| ".ljust(25, '-')  + "  ---    ---    ---    ---")
    
    for team_name in scoretable:
        team_data = scoretable[team_name]
        team_data = [str(x) for x in team_data]

        print("|", team_name.ljust(25), team_data[0].ljust(6), team_data[1].ljust(6), team_data[2].ljust(6), team_data[3].ljust(6))
    
    print("*"*40)

# Dictionary of operators
operations = {
    "list": list_seasons,
    "view": view_season
}

# Main loop
while True:
    os.system("cls" if os.name == "nt" else "clear")
    instructions()
    operator = input("| Selection > ").lower().strip()
    
    try:
        operations[operator]()
    except KeyError:
        print("-"*40 + f"\n| Unknown operator ({operator})\n" + "-"*40)
        
    input("Press enter to continue...")
    

    