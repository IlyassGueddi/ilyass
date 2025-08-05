import random

pc = random.randint(1,10)
user = int(input( "what you think the number is? (1-10): "))


while user != pc:
    user = int(input( "what you think the number is? (1-10) (press q if you want to quick): "))
    if pc > user :
        print("bigger")
    elif user > pc :
        print("smaller")
    elif user == pc :
        print("you win")
    elif user == "q":
        print("good bye")
        break

