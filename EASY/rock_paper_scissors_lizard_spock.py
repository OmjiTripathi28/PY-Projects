#yes sir/ma'am...fan of TBBT "the big bang theory!!"
import random
sheldons_version = ["rock" , "paper" , "scissors" , "lizard" , "spock"]


while True:
    user = input("Enter rock/paper/scissors/lizard/spock: ").strip().lower()
    comp = "lizard"
    print(f" Computer's action :{comp}")
    if user == comp:
        break
    elif user == "rock" and comp == {"lizard" , "scissors"}:
        print("you won")