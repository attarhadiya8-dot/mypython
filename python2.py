import random
def get_choices():
    player_choice=input("enter a choice(rock,paper,scissors):")
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices
choices=get_choices()
print(choices)

def chack_win(player,computer):
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)

    print(f"you chose {player} ,computer chose {computer}")
    if player=="rock" and computer=="paper":
        return "paper covers rock, you lose"
    elif player=="paper" and computer=="rock":
        return "paper covers rock, you lose"
    elif player=="scissors" and computer=="rock":
        return "scissors smashes rock, you win"
    elif player=="rock" and computer=="scissors":
        return "scissors smashes rock, you lose"
    elif player=="scissors " and computer=="paper":
        return "scissors cut paper, you win"
    else:
        return "scissors cut paper, you lose"
    


result=chack_win("rock","paper")
print(result)