import random


while True:
    guess1 = random.randint(1, 6)
    guess2 = random.randint(1, 6)
    user = input("Roll the dice? (y/n): ")
    if user == "y" or user == "Y":
        print (f"({guess1}, {guess2})")
    elif user == "n" or user == "N":
        print ("good bye")
        break
    else:
        print("invalide choice!")
