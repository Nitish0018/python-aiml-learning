import random

def play_game():
    choices = {0: "Stone", 1: "Paper", -1: "Scissor"}
    computer = random.choice([0, 1, -1])

    try:
        you = int(input("Enter your choice — 0 for Stone, 1 for Paper, -1 for Scissor: "))
        if you not in choices:
            raise ValueError
        print(f"You chose: {choices[you]}")
        print(f"Computer chose: {choices[computer]}")

        if you == computer:
            print("It's a tie!")
        elif (you == 0 and computer == -1) or (you == 1 and computer == 0) or (you == -1 and computer == 1):
            print("You won!")
        else:
            print("You lost ,Better Luck Next Time!")
    except ValueError:
        print("Invalid choice. Please enter 0, 1, or -1.")

while True:
    play_game()
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break