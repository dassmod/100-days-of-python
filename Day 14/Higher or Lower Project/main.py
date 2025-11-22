import art
import game_data
import random

def clear_screen():
    print("\n" * 100)

game_over = False
score = 0
option_a = random.choice(game_data.data)
option_b = random.choice(game_data.data)

while not game_over:

    print(art.logo)

    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
    print(art.vs)
    print(f"Compare B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")


    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice == "A":
        if option_a['follower_count'] > option_b['follower_count']:
            score += 1
            clear_screen()
            print(f"You`re right! Current score: {score}")
            option_b = random.choice(game_data.data)
            while option_a == option_b:
                option_b = random.choice(game_data.data)
            continue
        else:
            clear_screen()
            print(f"Sorry, that`s wrong. Final score: {score}")
            break
    elif choice == "B":
        if option_a['follower_count'] < option_b['follower_count']:
            score += 1
            clear_screen()
            print(f"You`re right! Current score: {score}")
            option_a = option_b
            option_b = random.choice(game_data.data)
            while option_a == option_b:
                option_b = random.choice(game_data.data)
            continue
        else:
            clear_screen()
            print(f"Sorry, that`s wrong. Final score: {score}")
            break
