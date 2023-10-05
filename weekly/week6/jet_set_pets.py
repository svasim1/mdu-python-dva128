import os
import json
import requests

base_url = "https://8fzqlwv0jd.execute-api.eu-north-1.amazonaws.com/"

# Get the list of cities and pets
data = requests.get(base_url)
data = json.loads(data.text)
cities = data["cities"]
pets = ["bird", "cat", "dog", "fish", "mouse", "rabbit"]

# Function to print the header
def header():
    print(".: JET SET PETS :.")

# Function to get the city input
def get_city():
    print("------------------")
    for c in cities:
        print(f"- {c.title()}")
    print("------------------")

    # Get the city and replace å, ä and ö with a and o
    city = input("Select city: ").lower().strip()
    city = city.replace("å", "a")
    city = city.replace("ä", "a")
    city = city.replace("ö", "o")

    # Check if the city is in the list of cities
    if city not in cities:
        print("ERROR: Unknown city")
        get_city()
        return
    
    return city

# Function to get the pet input
def get_pet():
    print("------------------")
    for p in pets:
        print(f"- {p}")
    print("------------------")

    # Get the pet and replace å, ä and ö with a and o
    pet = input("Select pet: ").lower().strip()
    if pet not in pets:
        print("ERROR: Unknown pet")
        get_pet()
        return
    
    return pet

# Function to display the info
def display_info(city, pet):
    # Navigate to selected city in the API
    data = requests.get(f"{base_url}/{city}")
    data = json.loads(data.text)
    
    # Get the users in the city
    users = data["users"]

    # Loop through the users
    for user in users:
        user_id = user["id"]
        data = requests.get(f"{base_url}/{city}/{user_id}")
        data = json.loads(data.text)

        # Get the user info
        forename = data["forename"]
        surname = data["surname"]
        animals = data["animals"]

        # Loop through the animals and check if the animal is the same as the pet input
        for animal in animals:
            if animal["type"] == pet:
                print(f"{forename} {surname} has a {pet} named {animal['name']}")

# Main loop
while True:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    header()
    city = get_city()
    pet = get_pet()
    display_info(city, pet)
    input("Press enter to continue...")