import requests
import os
import json

base_url = 'http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api'

def request_handler(api_url):
    request = requests.get(api_url)
    request = json.loads(request.text)
    return request

def save_season_data(api_url):
    data = request_handler(api_url)
    gamedays = data["gamedays"]
    teams = data["teams"]
    scoretable = {}
    for team in teams:
        scoretable[team] = [0, 0, 0, 0]
    for date in gamedays:
        change_results(scoretable, request_handler(api_url + "/" + date))
    return scoretable

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


        # TODO: fixa pa battre satt
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

            
def list_seasons():
    seasons = request_handler(base_url)["seasons"]
    print("-"*40)
    for key in seasons:
        print(f"| {seasons[key]}") 
    
def view_season():
    selected_year = input("| Year > ")
    scoretable = save_season_data(base_url + "/" + selected_year)
    
    print("|" + " "*39)
    print(f"| {'Team'.ljust(26)}{'W'.ljust(7)}{'D'.ljust(7)}{'L'.ljust(7)}{'P'.ljust(7)}")
    print("| ".ljust(25, '-')  + "  ---    ---    ---    ---")
    
    for team_name in scoretable:
        team_data = scoretable[team_name]
        team_data = [str(x) for x in team_data]

        
        
        print("|", team_name.ljust(25), team_data[0].ljust(6), team_data[1].ljust(6), team_data[2].ljust(6), team_data[3].ljust(6))


operations = {
    "list": list_seasons,
    "view": view_season
}

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("-"*40)
    operator = input("| Selection > ")
    operations[operator]()
    input("Press enter to continue...")
    

    