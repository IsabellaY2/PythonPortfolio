#Isabella Yan
import random
user = 0
computer = 0
CS= ["Rock", "Paper", "Scissor"]
computer_choice= random.choice(CS)

def choices():
    global user
    global computer
    if message== "Rock" and computer_choice == "Rock":
        print (f"Computer chose: {computer_choice}")
        print (f"tie {user}-{computer}")

    if message == "Paper" and computer_choice == "Paper":
        print (f"Computer chose: {computer_choice}")
        print (f"tie {user}-{computer}")

    if message == "Scissors" and computer_choice == "Scissors":
        print (f"Computer chose: {computer_choice}")
        print (f"tie {user}-{computer}")

    if message == "Rock" and computer_choice == "Scissors":
        print (f"Computer chose: {computer_choice}")
        user = user+1
        print (f"You won! {user}-{computer}")

    if message == "Paper" and computer_choice == "Rock":
        print (f"Computer chose: {computer_choice}")
        user = user+1
        print (f"You won! {user}-{computer}")

    if message == "Scissors" and computer_choice == "Paper":
        print (f"Computer chose: {computer_choice}")
        user = user+1
        print (f"You won! {user}-{computer}")

    if message == "Rock" and computer_choice == "Paper":
        print (f"Computer chose: {computer_choice}")
        computer = computer+1
        print (f"You lost! {user}-{computer}")

    if message == "Paper" and computer_choice == "Scissors":
        computer = computer+1
        print (f"Computer chose: {computer_choice}")
        print (f"You lost! {user}-{computer}")

    if message == "Scissors" and computer_choice == "Rock":
        print (f"Computer chose: {computer_choice}")
        computer = computer+1
        print (f"You lost! {user}-{computer}")


for i in range (1,100):
    message=input ("Rock Paper Scissors? If you want to exit, type e " )
    if message == "Rock" or message== "Paper" or message == "Scissors":
        computer_choice = random.choice(CS)
        choices()
        continue

    if message == "e":
        break

    else:
        print ("Error. Please try Again.")
        continue




