rock =('''
     _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
paper = (''' 
          _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
         ''')

scissors = ('''
                _______
---'        ____)____
          ______)
            __________)
      (____)
---.__(___)
            ''')

import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, You lose1")
elif user_choice == 0:
    print(rock)
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print("Computer chose.")
        print(rock)
        print("It's a draw")
    elif computer_choice ==1:
        print("Computer  chose.")
        print(paper)
        print("You lose")
    else:
        print("Computer chose.")
        print(scissors)
        print("You win")
elif user_choice == 1:
    print(paper)
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print("Computer chose.")
        print(rock)
        print("You Win")
    elif computer_choice == 1:
        print("Computer chose.")
        print(paper)
        print("It's a draw")
    else:
        print("Computer chose.")
        print(scissors)
        print("You lose")
else:
    print(scissors)
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print("Computer chose.")
        print(rock)
        print("You lose")
    elif computer_choice == 1:
        print("Computer chose.")
        print(paper)
        print("You win")
    else:
        print("Computer chose.")
        print(scissors)
        print("It's a draw")
    
