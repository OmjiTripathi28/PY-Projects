#yes sir/ma'am...i'm a fan of TBBT "the big bang theory!!"
import random

choices = ["rock", "paper", "scissors", "lizard", "spock"]

win_rules = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["rock", "scissors"]
}

def play():
    user = input("Enter rock / paper / scissors / lizard / spock: ").lower()

    if user not in choices:
        print("Invalid choice!")
        return

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif computer in win_rules[user]:
        print("You win!")
    else:
        print("Computer wins!")

while True:
    play()
    again = input("Play again? (y/n): ").lower()
    if again != "y":
        break

print("Thanks for playing!")
