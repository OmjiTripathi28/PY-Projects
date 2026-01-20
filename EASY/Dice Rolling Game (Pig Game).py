import random

total_user_score = 0
total_comp_score = 0
WIN_SCORE = 100

while True:
    
    user_turn_score = 0
    print("\nYOUR TURN")

    while True:
        choice = input("ROLL or PASS : ").strip().upper()
        if choice == "ROLL":
            dice = random.randint(1,6)
            print(f"You rolled: {dice}")

            if dice == 1 :
                user_turn_score = 0
                print("YOU LOST THE TURN! No points added.")
                break

            else:
                user_turn_score += dice
                print(f"TURN SCORE : {user_turn_score}")
        elif choice == "PASS":
            total_user_score += user_turn_score
            print(f"YOUR TOTAL SCORE : {total_user_score}")
            break
        else:
            print("INVALID INPUT")

    if total_user_score >= WIN_SCORE:
        print("YOU WIN!!")
        break
    
    comp_turn_score = 0
    print("\nCOMPUTER'S TURN")

    while comp_turn_score < 20:
        dice = random.randint(1,6)
        print(f"Computer rolled: {dice}")
        if dice == 1 :
            comp_turn_score = 0
            print("COMPUTER LOST THE TURN!")
            break
        else:
            comp_turn_score += dice
            print(f"COMPUTER TURN SCORE : {comp_turn_score}")

    total_comp_score += comp_turn_score
    print(f"COMPUTER TOTAL SCORE : {total_comp_score}")

    if total_comp_score >= WIN_SCORE:
        print("COMPUTER WINS!")
        break