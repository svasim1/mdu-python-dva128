import random

def higher_lower_game():
    
    # Print header
    print(".: THE HIGHER LOWER GAME :." + "\n" + "---------------------------" + "\n" + "Welcome to The Higher Lower" + "\n" + "Game. I will randomize a" + "\n" + "number between 0 and 99." + "\n" + "Can you guess it?" + "\n" + "---------------------------")

    # Generate a random number between 0 and 99
    secret_number = random.randint(0, 99)
    guesses = 0

    while True:
        try:
            user_guess = int(input("Your guess > "))
            guesses += 1

            if user_guess < secret_number:
                print("HIGHER!")
            elif user_guess > secret_number:
                print("LOWER!")
            else:
                print(f"{user_guess} is correct!")
                print(f"It took you {guesses} guesses.")
                print("Good job!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    higher_lower_game()
