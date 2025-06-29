import random

# Dictionary to map choices
game_choices = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

while True:
    user_input = input("Enter your choice: (1) for Rock, (2) for Paper, (3) for Scissors. Type 'exit' to quit: ").lower()

    if user_input == "exit":
        print("Thanks for playing!")
        break

    if not user_input.isdigit():
        print("Invalid input. Please enter 1, 2, or 3.")
        continue

    player_choice = int(user_input)

    if player_choice not in game_choices:
        print("Invalid choice. Please select 1 for Rock, 2 for Paper, or 3 for Scissors.")
        continue

    computer_choice = random.randint(1, 3)

    print(f"You chose {game_choices[player_choice]}. The computer chose {game_choices[computer_choice]}.")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (
        (player_choice == 1 and computer_choice == 2) or
        (player_choice == 2 and computer_choice == 3) or
        (player_choice == 3 and computer_choice == 1)
    ):
        print("The computer wins!")
    else:
        print("You win!")
