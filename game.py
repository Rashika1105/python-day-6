import random

def game():
    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    try:
        user = int(input("Enter your choice: "))

        # Base case (stop recursion)
        if user == 4:
            print("Game ended")
            return

        if user not in [1, 2, 3]:
            print("Invalid choice")
            game()
            return

        # Convert number to choice
        if user == 1:
            user_choice = "Rock"
        elif user == 2:
            user_choice = "Paper"
        else:
            user_choice = "Scissors"

        computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        # Decide winner
        if user_choice == computer_choice:
            print("Tie")
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            print("You win")
        else:
            print("Computer wins")

        # Recursive call
        game()

    except ValueError:
        print("Enter a number only")
        game()

# Start game
game()
