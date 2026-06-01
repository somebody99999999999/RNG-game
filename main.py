# The name of the program
# RNG Game

# The import of the random module
import random

# Intro and Instructions to the program
print("Hello and welcome to RNG Game press Enter / Return")
input()
print("🔴 INSTRUCTIONS 🔴")
print(" You need to get the same pair of numbers on top of each other to win! ")
print("Press Enter / Return to start the game ")
input()

# Generate the first random pair numbers from between one and ten
first_num = random.randint(1, 10)

# Generate the second random pair numbers between one and ten
second_num = random.randint(1, 10)

reset_game = True

while True:
    # Checks if the user won
    if first_num == 10 and second_num == 10 and reset_game == True:
        print("Congratulations")
        input()
        print("You beat my game once hwo many times you can you beat it?")
        reset_game = True
    else:
        # Prints out the first and second set of random numbers
        print("You got 🥁")
        print(first_num)
        print(second_num)
        
        # So it doesn't reroll if there is a ten aleady on the board 
        if first_num != 10:
            first_num = random.randint(1, 10)

        if second_num != 10:
            second_num = random.randint(1, 10)

    # Ask the user for a re-roll
    reroll = input("You want to reroll that 🤔 (y/n) ").lower()

    if reroll == "n":
        print("Thanks for playing my RNG game")
        
        # Breaks out of the loop
        break

