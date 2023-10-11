import os
import artist_database as db

# This program demonstrates the get_artist(), and the list_artists() methods from artist_database.py

# Function to print the header instructions
def instructions():
    header = ("""------------------------------------------------------------
This program helps you search a database for a specific artist.
Here are a list of available artists:
------------------------------------------------------------""")
    print(header)

    print(', '.join(db.list_artists()))
    print("------------------------------------------------------------")

# Get information for a specific artist
def search():
    search = input("Enter name of artist: ").strip().lower().title()
    
    try:
        artist_info = db.get_artist(search)
        
        # Print the artist information
        print("------------------------------------------------------------")
        print(f"Members: {', '.join(artist_info['members'])}")
        print(f"Genres: {', '.join(artist_info['genres'])}")
        print(f"Years Active: {', '.join(artist_info['years_active'])}")
        print("------------------------------------------------------------")

    # Error handling
    except KeyError:
        print(f"ERROR: Unknown artist ({search})")

# Main loop
while True:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    instructions()
    search()
    input("Press enter to continue...")