def chack_win(player,computer):

    print(f"you chose {player} ,computer chose {computer}")
    if player==computer:
        return "its a tie!"
    elif player=="rock" and computer=="paper":
        return "paper covers rock, you lose!"
    elif player=="paper" and computer=="rock":
        return "paper covers rock, you lose!"
    elif player=="scissors" and computer=="rock":
        return "scissors smashes rock, you win!"
    elif player=="rock" and computer=="scissors":
        return "scissors smashes rock, you lose!"
    elif player=="scissors " and computer=="paper":
        return "scissors cut paper, you win!"
    else:
        return "scissors cut paper, you lose!"
    

import random
player_choice=input("Enter your choice(rock,paper,scissors):")

options=["rock","paper","scissors"]
computer_choice=random.choice(options)
result=chack_win(player_choice,computer_choice)
print(result)