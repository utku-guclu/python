from art import logo, vs
# from replit import clear
from game_data import data
import random

""" format """
def format(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a/an {description}, from {country}"


def check_answer(guess, a, b):
    if a > b:
        return guess == "a"
    else:
        return guess == "b"

def game():  

    
    is_gameover = False
    score = 0
    against = random.choice(data)

    while not is_gameover:
        compare = against
        against = random.choice(data)
        while compare == against:
            against = random.choice(data)

        print(f"Compare A: {format(compare)}.")
        print(vs)
        print(f"Compare B: {format(against)}.")
    
        print(logo)
        guess = input("Who has more followers? 'A' or 'B' ? \n").lower()
        a_follower_count = compare["follower_count"]
        b_follower_count = against["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        # clear()

        if is_correct:
            print("You're right!")
            score += 1
        else:
            is_gameover = True
            print(f"Sorry, that's wrong. Final score: {score}.")

game()