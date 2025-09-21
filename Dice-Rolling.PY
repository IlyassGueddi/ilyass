import random

count = 0

while True:
    user = input("Roll the dice? (y/n): ")
    if user == "y" or user == "Y":
        dice = int(input("how many dice you want to rolle? ")) 
        for i in range(dice):
            roll = random.randint(1, 6)
            print ("Die", i +1, ":", roll)
        count = count + dice
        print(f"you roll the dice {count} times")
    elif user == "n" or user == "N":
        print ("Thanks for playing!")
        break
    else:
        print("invalide choice!")


