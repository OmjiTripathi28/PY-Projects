import random

def play_game(max_attempts=None):
    attempts = 0

    while True:
        n = int(input("Enter the number (1–100): "))

        if n < 1 or n > 100:
            print("Invalid range")
            continue

        attempts += 1

        if n == random_integer:
            print(f"Correct! You guessed it in {attempts} attempts")
            break

        if max_attempts and attempts >= max_attempts:
            print("LIMITS REACHED")
            print(f"The number was {random_integer}")
            break

        print("TOO HIGH" if n > random_integer else "TOO LOW")

random_integer = random.randint(1, 100)

print("WELCOME TO THE GUESSING GAME")
difficulty = input("choose the difficulty you want EASY/MODERATE/HARD: ")
difficulty = difficulty.upper()

    
if difficulty == "EASY":
    play_game()
elif difficulty == "MODERATE":
    play_game(10)
elif difficulty == "HARD":
    play_game(5)
