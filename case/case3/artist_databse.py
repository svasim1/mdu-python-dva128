# Import required modules
import os
import json
import requests

# Create 2 empty string variables for printing info 
artist_data = ""
artist_list = ""

# Save url in variable
base_url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

def instructions():
    # Saves the first 3 rows as header
    header = f"""{("-")*40}
{"Artist Database".center(40)}
{("-")*40}"""
    
    # Saves the last 4 lines in instructions
    instructions = f"""| L | List artists
| V | View artist profile
| E | Exit application
{("-")*40}"""
    
    print(header)   
    
    # Prints artist_data if it has any content
    if artist_data != "":
        print(artist_data)
        print("*"*40)
    
    # Prints artist_list if it has any content
    elif artist_list != "":
        print(artist_list)
        print("*"*40)

    print(instructions)
    
def list_artist():
    # Set artist data to an empty string so it doesn't get printed
    global artist_data
    artist_data = ""

    data = requests.get(base_url)  # Saves raw data to data variable
    
    # Exits the function if the status code shows an error
    if(data.status_code != 200):
        print(f"| ERROR: {data.status_code}")
        input("Press enter to continue...")
        return
    
    data = json.loads(data.text)  # Formats the data variable

    # Gets the artist list and loops through it
    artists = data["artists"]
    for artist in artists:
        
        # Adds the artist to the artist list
        global artist_list
        artist_list += f"| {artist['name']}"

        # Adds newline if it isn't the last item
        if artists.index(artist) != len(artists) - 1:
            artist_list += "\n" 

def view_artist():
    global artist_data
    global artist_list
    artist_list = ""
    
    artist_name = input("| Artist name > ")
    base_data = requests.get(base_url)
    
    if(base_data.status_code != 200):
        print(f"| ERROR: {base_data.status_code}")
        input("Press enter to continue...")

        return
    
    base_data = json.loads(base_data.text)

    for artists in base_data["artists"]:
        if artist_name.title().strip() == artists["name"]:
            artists_id = artists["id"]
            break
    else:
        print(f"| ERROR: Artist '{artist_name}' not found")
        input("Press enter to continue...")

        return
    
    artist_info = requests.get(base_url + artists_id)
    artist_info = json.loads(artist_info.text)
    artist_info = artist_info['artist']
    
    artist_data = f"""{('*')*40}
{artist_info['name'].center(40)}
{('*')*40}
| Members:      {', '.join(artist_info["members"])}
| Genres:       {', '.join(artist_info["genres"])}
| Years active: {artist_info['years_active'][0]}"""
    return

def check_operator(operator):
    if(operator.lower().strip() == "l"):
        list_artist()
    elif(operator.lower().strip() == "v"):
        view_artist()
    elif(operator.lower().strip() == "e"):
        exit()
    else:
        print(f"| ERROR: Unknown command '{operator}'")
        input("Press enter to continue...")

        return

while True:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
    instructions()
    operator = input("| Selection > ")
    check_operator(operator)