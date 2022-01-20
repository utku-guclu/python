import random

def compare(user_score, cpu_score):
    if user_score == cpu_score:
        return "Draw"
    elif cpu_score == 0:
        return "Cpu has Blackjack, You Lose"
    elif user_score == 0:
        return "You have a Blackjack! You Win"
    elif user_score > 21:
        return "You went over, you lose"
    elif cpu_score > 21:
        return "Computer went over, you win!"
    elif cpu_score > user_score:
        return "you lose, no luck.."
    else:
        return "you win! lucky."

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def play_game():
    gameover = False
    user_cards = []
    cpu_cards = []

    # deal 2 cards each
    for _ in range(2):
        user_cards.append(deal_card())
        cpu_cards.append(deal_card())

   
    # gameover condition
    while not gameover:
         # add up the users and computers scores
        user_score = calculate_score(user_cards)
        cpu_score = calculate_score(cpu_cards)

        # show cards <<<<
        print(f"your cards: {user_cards}")
        print(f"computer's cards: {cpu_cards}")


        if user_score > 21 or cpu_score == 0:
            gameover = True
        else:
            if input("do you want another card?: (y or n)") == "y":
                user_cards.append(deal_card())
            else:
                gameover = True
    # cpu plays
    while cpu_score < 17 and cpu_score != 0:
        cpu_cards.append(deal_card())
        cpu_score = calculate_score(cpu_cards)

    print("---final hand---")
    print(f"your hand: {user_cards}, your score: {user_score}")
    print(f"computer's hand: {user_cards}, cpu score: {cpu_score}")
    print(compare(user_score, cpu_score))
play_again = input("do you want to play Blackjack? (y or n)")
while play_again != "n":
    play_game()
