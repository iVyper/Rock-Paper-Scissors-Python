# Import the random module.
import random

# The choices a player could make is put into the player_choices list.
players_choices = ['Rock', 'Paper', 'Scissors']
# Take the players choice as input into the user_input variable.
user_input = int(input("What do you choose?\nType '0' for Rock, '1' for Paper, or '2' for Scissors: "))

# Check to see if the user's input is within the bounds of choices a player can make.
if user_input < 0 or user_input > len(players_choices) - 1:
    # If it is outside the bounds, tell the player.
    print("You entered an invalid choice. Please try again.")
else:
    # If it is not, then we continue with the game.
    user_choice = players_choices[user_input]

    # Generate the computers choice by using the random modules choice function
    # so that a choice from the list of possible player choices is selected.
    computers_choice = random.choice(players_choices)

    # Print the user's choice.
    print(f"You chose: {user_choice}")
    # Print the computer's choice.
    print(f"The computer chose: {computers_choice}")

    # Account for the possibility of both players having the same choice.
    if user_choice == computers_choice:
        print("It's a tie!")

    # Account for the possibility of both players having different choices.
    else:
        # Account for situations where the user can win.
        # Rock beats Scissors
        if user_choice == 'Rock' and computers_choice == 'Scissors':
            print("You win!")
        # Scissors beats Paper
        elif user_choice == 'Scissors' and computers_choice == 'Paper':
            print("You win!")
        # Paper beats Rock
        elif user_choice == 'Paper' and computers_choice == 'Rock':
            print("You win!")
        # If none of the above situations happen, then it means the computer
        # has beaten the user since the opposite possibilities no matter the order
        # mean the computer has won.
        else:
            print("You lose!")