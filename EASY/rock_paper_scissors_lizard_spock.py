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

