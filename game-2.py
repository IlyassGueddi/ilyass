import random
def fonctionname(user,pc):
  
        if user == "rock" and pc == "paper":
          print(pc)
          print("i win.")
        elif user == "paper" and pc == "paper":
          print(pc)
          print("no one wins.")
        elif user == "scissors" and pc == "paper":
          print(pc)
          print("you win.")
        elif user == "rock" and pc == "rock":
          print(pc)
          print("no one wins.")
        elif user == "paper" and pc == "rock":
          print(pc)
          print("you win.")
        elif user == "scissors" and pc == "rock":
          print(pc)
          print("i win.")
        elif user == "rock" and pc == "scissors":
          print(pc)
          print("you win.")
        elif user == "paper" and pc == "scissors":
          print(pc)
          print("i win.")
        elif user == "scissors" and pc == "scissors":
          print(pc)
          print("no one wins.")


while True :

    arr = ["rock", "paper", "scissors" ]
    pc = random.choice(arr)
    user = str(input("choose rock, paper or scissors: "))
    fonctionname(user,pc)
    
"""
    while True :
        user = str(input("choose rock, paper or scissors: "))
        if user == "rock" and pc == "paper":
          print(pc)
          print("i win.")
        elif user == "paper" and pc == "paper":
          print(pc)
          print("no one wins.")
        elif user == "scissors" and pc == "paper":
          print(pc)
          print("you win.")
        elif user == "rock" and pc == "rock":
          print(pc)
          print("no one wins.")
        elif user == "paper" and pc == "rock":
          print(pc)
          print("you win.")
        elif user == "scissors" and pc == "rock":
          print(pc)
          print("i win.")
        elif user == "rock" and pc == "scissors":
          print(pc)
          print("you win.")
        elif user == "paper" and pc == "scissors":
          print(pc)
          print("i win.")
        elif user == "scissors" and pc == "scissors":
          print(pc)
          print("no one wins.")
"""

    