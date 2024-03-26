# build rock, paper, and scissor game.
# 0 for rock, 1 for scissior and 2 for paper

import random

rock = '''
    _________
---'    _____)   
        (_____)
        (______)
        (_____)
----.____(____)

'''

paper = '''
    ___________
---'    _______)   
        _________)
        ___________)
        _________)
----.________)

'''

scissors = '''
    _________
---'    _____)___   
        _________)
        ___________)
        (_____)
----.___(____)

'''

player1 = random.randint(0,2)
player2 = int(input("Choose 0 for Rock, 1 for Scissors and 2 for Paper!!! :"))

item_list =  [rock, scissors, paper] 




if player2<0 or player2>2:
    print("Wrong selection!") 
else:
    print(f"Computer choose: {player1} \n {item_list[player1]} \n")

    print(f"I choose: {player2} \n {item_list[player2]} \n")

    if player1 == player2:
        print("It's DRAW")
    elif player1==0 and player2==1:
        print("Computer won!")
    elif player1==1 and player2==2:
        print("Computer won!")
    elif player1==2 and player2==0:
        print("Computer won!")
    else:
        print("I win!")
