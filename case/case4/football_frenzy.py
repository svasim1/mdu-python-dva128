import requests
import os
import json

base_url = 'http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api'

def request_handler(api_url):
    request = requests.get(api_url)
    request = json.loads(request.text)
    return request

def save_season_data(api_url):
    print(api_url)
    data = request_handler(api_url)
    print(data)
    gamedays = data["gamedays"]
    print(gamedays)
    teams = data["teams"]
    scoretable = {}
    for team in teams:
        scoretable[team] = [0, 0, 0, 0]
    for date in gamedays:
        change_results(scoretable, request_handler(api_url + "/" + date))
    print(scoretable)

def change_results(dic, data):
    matches = data["games"]
    for key in matches:
        home_score = matches[key]["score"]["home"]["goals"]
        home_team = matches[key]["score"]["home"]["team"]
        away_score = matches[key]["score"]["away"]["goals"]
        away_team = matches[key]["score"]["home"]["team"]


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
            dic[home_team][2] += 1
            dic[away_team][2] += 1

            
def list_seasons():
    seasons = request_handler(base_url)["seasons"]
    print("-"*40)
    for key in seasons:
        print(f"| {seasons[key]}")
    
def view_season():
    selected_year = input("| Year > ")
    save_season_data(base_url + "/" + selected_year)


operations = {
    "list": list_seasons,
    "view": view_season
}

score = {
    
}

view_season()
#request_handler(base_url + "/2018")
while not True:
    os.system("cls" if os.name == "nt" else "clear")
    print("-"*40)
    operator = input("Selection > ")
    operations[operator]()
    input("Press enter to continue...")
    