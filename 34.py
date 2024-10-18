#Rock scissor paper game

import random

choices = ["Rock", "Paper", "Scissor"]

while True:
    player = input("Rock, Paper, or Scissor: (Enter 'Exit' to quit the game): ").capitalize()
    if player == "Exit":
        break

    while choice is not choices:
        continue

    computer = random.choice(choices)

    print(f"Player:{player:10}")
    print(f"Computer:{computer:10}")

    if player == 'Rock' and computer == 'Paper':
        print("You lose")

    elif player == 'Paper' and computer == 'Scissor':
        print('You lose')

    elif player == 'Scissor' and computer == 'Rock':
        print("You lose")

    elif player == computer:
        print("It's a draw")

    else:
        print("You win")