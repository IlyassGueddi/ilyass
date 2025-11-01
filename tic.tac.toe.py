play =input("do you want to play (yes/no): ")

if play.lower() == "yes":
    while True:
        print("-----Welcome to tic-tac-toe-----")
        print("            1 | 2 | 3 \n            4 | 5 | 6 \n            7 | 8 | 9 ")
        player1 = int(input("Player 1 ||| What's your first move: "))            

elif play.lower() == "no":
    print("Got it \nGood Bye ")
else:
    print("invalid value! ")