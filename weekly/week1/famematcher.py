print("---------------------" + "\n" + "Search of the day!" + "\n" + " " + "\n" + "---------------------")

try:
    gender = str(input("Gender: "))
    if gender == "male" or "female":
        exit()
        
    
        
    hair_color = str(input("Hair color: "))
    eye_color = str(input("Eye color: "))

except ValueError:
    print("Please enter a valid answer")
    exit()

# Output