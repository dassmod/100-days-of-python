import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors\n"))

options = [rock, paper, scissors]
comp_choice = random.randint(0, 2)

print(options[choice])
print(f"\nComputer choose: ")

if choice == 0:
    if comp_choice == 0:
        print(f"{options[comp_choice]}\nDraw.")
    elif comp_choice == 1:
        print(f"{options[comp_choice]}\nYou lose :(")
    elif comp_choice == 2:
        print(f"{options[comp_choice]}\nYou win :(")
elif choice == 1:
    if comp_choice == 0:
        print(f"{options[comp_choice]}\nYou win!.")
    elif comp_choice == 1:
        print(f"{options[comp_choice]}\nDraw.")
    elif comp_choice == 2:
        print(f"{options[comp_choice]}\nYou lose :(")
elif choice == 2:
    if comp_choice == 0:
        print(f"{options[comp_choice]}\nYou lose :(.")
    elif comp_choice == 1:
        print(f"{options[comp_choice]}\nYou win!")
    elif comp_choice == 2:
        print(f"{options[comp_choice]}\nDraw.")