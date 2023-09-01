# List of possible matches
people = [
    {"name": "Daniel Radcliffe", "gender": "male", "hair color": "brown", "eye color": "brown"},
    {"name": "Rupert Grint", "gender": "male", "hair color": "red", "eye color": "blue"},
    {"name": "Emma Watson", "gender": "female", "hair color": "brown", "eye color": "brown"},
    {"name": "Selena Gomez", "gender": "female", "hair color": "brown", "eye color": "brown"},
    {"name": "Jennifer Lawrence", "gender": "female", "hair color": "blonde", "eye color": "blue"},
    {"name": "Keanu Reeves", "gender": "male", "hair color": "brown", "eye color": "brown"},
    {"name": "Brad Pitt", "gender": "male", "hair color": "blonde", "eye color": "blue"},
    {"name": "Leonardo DiCaprio", "gender": "male", "hair color": "brown", "eye color": "blue"},
    {"name": "Johnny Depp", "gender": "male", "hair color": "brown", "eye color": "brown"}
]

# Print header
print(".: FAME MATCHER :." + "\n" + "---------------------" + "\n" + "Search of the day!" + "\n" + "female, brown, brown" + "\n" + "---------------------")

# Inputs
gender = input("Gender: ").lower()
hair_color = input("Hair color: ").lower()
eye_color = input("Eye color: ").lower()

# Filter the list of people
matching_people = []
for person in people:
    if (not gender or person["gender"] == gender) and \
       (not hair_color or person["hair color"] == hair_color) and \
       (not eye_color or person["eye color"] == eye_color):
        matching_people.append(person)

# Print the output
if matching_people:
    # Formatting the output
    matches = ", ".join([person["name"] for person in matching_people])
    print("---------------------" + "\n" + "Match: " + matches)
else:
    print("---------------------" + "\n" + "No matching celebrities found.")