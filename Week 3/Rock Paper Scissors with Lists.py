from datetime import datetime
choices = ["Rock", "Paper", "Scissors"]

now = datetime.now()
current_second = now.second

computer_choice = choices[current_second % 3]
player_choice = input("Enter your choice (1. Rock, 2. Paper, or 3. Scissors): ")
player_choice = int(player_choice) - 1

if player_choice < 0 or player_choice > 2:
    print("Invalid choice. Please choose 1, 2, or 3.")
else:
    print("Computer chose:", computer_choice)
    print("Player chose:", choices[player_choice])

    if player_choice == current_second % 3:
        print("It's a tie!")
    elif (player_choice == 0 and current_second % 3 == 2) or (player_choice == 1 and current_second % 3 == 0) or (player_choice == 2 and current_second % 3 == 1):
        print("You win!")
    else:
        print("Computer wins!")
