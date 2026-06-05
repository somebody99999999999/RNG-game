# The name of the program
# RNG Game

# The import of the random module
import random

# Intro and Instructions to the program / game
print("Hello and welcome to RNG Game press Enter / Return")
input()
print("🔴 INSTRUCTIONS 🔴")
print(" You need to get the same pair of numbers on top of each other to win! ")
print("Press Enter / Return to start the game ")
input()

# Generate the first random pair numbers from between one and any number
first_num = random.randint(1, 10)

 # Generate the second random pair numbers between one and any number
second_num = random.randint(1, 10)

reset_game = True


while True:
        # Ask the user for a re-roll
        reroll = input("You want to get a reroll? (y/n) ").lower()

        if reroll == "n":
            print("Bye but thanks for playing my RNG game")
            
            # Breaks out of the loop
            break

        if reroll == "y" and "Y":

            # Checks if the user won
            if first_num == 10 and second_num == 10 and reset_game == True:
                print("Congratulations")
                print("You beat my game")
                reset_game = True

            else:

                # Prints out the first and second set of random numbers
                print("The numbers you got is ...")
                print(first_num)
                print(second_num)
                
                # So it doesn't reroll if there is a ten aleady on the board 
                if first_num != 10:
                    first_num = random.randint(1, 10)

                if second_num != 10:
                    second_num = random.randint(1, 10)

        # The Anti Cheat so they can't just spam space to win everytime
        if reroll ==  "":
            print("")
            print("Nice try play the game the right way ")
            print("")
            break
