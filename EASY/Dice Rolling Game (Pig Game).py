import random

total_user_score = 0
total_comp_score = 0
WIN_SCORE = 100

while True:
    
    user_turn_score = 0
    print("\nYOUR TURN")

    while True:
        choice = input("ROLL or PASS: ").strip().upper()

        if choice == "ROLL":
            dice = random.randint(1, 6)
            print(f"You rolled: {dice}")

            if dice == 1:
                user_turn_score = 0
                print("Turn lost! No points added.")
                break
            else:
                user_turn_score += dice
                print(f"Turn score: {user_turn_score}")

        elif choice == "PASS":
            total_user_score += user_turn_score
            print(f"Total score: {total_user_score}")
            break
        else:
            print("Invalid choice.")

    if total_user_score >= WIN_SCORE:
        print("YOU WIN!")
        break

    
    comp_turn_score = 0
    print("\nCOMPUTER'S TURN")

    while comp_turn_score < 20:
        dice = random.randint(1, 6)
        print(f"Computer rolled: {dice}")

        if dice == 1:
            comp_turn_score = 0
            print("Computer lost its turn!")
            break
        else:
            comp_turn_score += dice

    total_comp_score += comp_turn_score
    print(f"Computer total score: {total_comp_score}")

    if total_comp_score >= WIN_SCORE:
        print("COMPUTER WINS!")
        break
