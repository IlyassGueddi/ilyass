import random



while True :
    start = int(input("Enter the start point: "))
    end = int(input("Enter the end point: "))
    pc = random.randint(start, end)
    while True:
        user = int(input("what you think the number is : "))
        if user > pc :
            print("too hight!")
        elif user < pc :
            print("too low!")
        elif user == pc :
            print(f"you win the number is {pc}.")
            break
        else:
            print("invalide value")
    answer = input("want you to play again? (y/n): ")
    if answer == "y" or answer == "Y":
        continue
    elif answer == "n" or answer == "N":
        print("GoodBye")
        break