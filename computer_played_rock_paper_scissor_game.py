print("Rock....")
print("Paper...")
print("Scissors...")
player1= input("player1 Enter your choice: ")
from random import randint
computer_player= randint(0,2)
if computer_player==0:
    computer = "rock"
elif computer_player==1:
    computer="paper"
elif computer_player==2:
    computer="scissors"
print(f"Computer plays {computer}")
if player1==computer:
    print("players draw")
elif player1 == "rock":
    if computer=="paper":
        print("computer wins")
    elif computer=="scissors":
        print("player1 wins")
elif player1 == "paper":
    if computer=="rock":
        print("player1 wins")
    elif computer=="scissors":
        print("computer wins")
elif player1 == "scissors":
    if computer=="rock":
        print("player1 wins")
    elif computer=="paper":
        print("computer wins")
else:
    print("Something is wrong!")
