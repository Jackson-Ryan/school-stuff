import random # This line imports the random module, which is used to generate random numbers for the computer's choice in the game.
import time # This line imports the time module, which is used to pause the execution of the program for a specified amount of time, allowing for a delay between rounds of the game.
game = "Ongoing" # This variable is used to track the state of the game. It can be set to "Ongoing", or "Finished" to indicate whether the game is still in progress or has ended.
while game == "Ongoing":
    computer_choice = random.randint(1, 3) # This line generates a random integer between 1 and 3 to represent the computer's choice in the game. The choices correspond to Rock (1), Paper (2), and Scissors (3).
    player_choice = int(input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): ")) # This line prompts the player to input their choice and converts it to an integer.
    if player_choice == computer_choice: # This condition checks if the player's choice is the same as the computer's choice, indicating a tie.
        print("It's a tie!")
    elif (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2): #This condition checks if the player has won based on the rules of Rock, Paper, Scissors. The player wins if they choose Rock (1) and the computer chooses Scissors (3), or if they choose Paper (2) and the computer chooses Rock (1), or if they choose Scissors (3) and the computer chooses Paper (2).
        print("You win!")
    else:
        print("Computer wins!")
        print("Computer chose:", computer_choice) # This line prints the computer's choice after the game round is completed, allowing the player to see what the computer selected.
    again = input("Do you want to play again? (yes/no): ") # This line prompts the player to decide if they want to play another round of the game.
    if again.lower() != "yes": # This condition checks if the player's response is not "yes". If the player does not want to play again, the game state is set to "Finished", ending the loop and the game.
        game = "Finished"
    else:
        print("Starting a new game!") # This line prints a message indicating that a new game will start, and the loop continues for another round
        time.sleep(3) # This line pauses the execution of the program for 3 seconds before starting a new round, allowing the player to prepare for the next game.