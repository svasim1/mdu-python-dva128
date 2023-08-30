import math

# Print header and ask for input
print(".:HOTDOG PLANNER:." + "\n" + "---------------------" + "\n" + "How many students wants...")
try:
    two_meat = int(input("2 hot dogs (meat) > "))
    if two_meat < 0:
        print("Please enter a valid number")
        exit()
    three_meat = int(input("3 hot dogs (meat) > "))
    if three_meat < 0:
        print("Please enter a valid number")
        exit()
    two_vegan = int(input("2 vegan hot dogs > "))
    if two_vegan < 0:
        print("Please enter a valid number")
        exit()
    three_vegan = int(input("3 vegan hot dogs > "))
    if three_vegan < 0:
        print("Please enter a valid number")
        exit()
except ValueError:
    print("Please enter a valid number")
    exit()
    
# Calculate quantities and packages
drinks = two_meat+three_meat+two_vegan+three_vegan
total_meat = two_meat*2+three_meat*3
meat_packages = math.ceil(total_meat/8)
total_vegan = two_vegan*2+three_vegan*3
vegan_packages = math.ceil(total_vegan/4)

# Calculate the price and round it to two decimal places
price = round(meat_packages*20.95+vegan_packages*34.95+drinks*13.95, 2)

# Print the output
print("---------------------" + "\n" + "| Meat: " + str(meat_packages) + " packages" + "\n" + "| Vegan: " + str(vegan_packages) + " packages" + "\n" + "| Drinks: " + str(drinks) + " drinks" + "\n" + "---------------------" + "\n" + str(price) + " SEK" + "\n" + "---------------------")