import random



while True :
    start = int(input("Enter the start point: "))
    end = int(input("Enter the end point: "))
    pc = random.randint(start, end)
    max_tries = 5
    attempts = 0
    while True:
        user = int(input("what you think the number is : "))
        attempts += 1
        if user > pc :
            print("too hight!")
        elif user < pc :
            print("too low!")
        elif user == pc :
            print(f"you win the number is {pc}.")
            break
        else:
            print("invalide value")
        if attempts >= max_tries :
            print(f"Out of tries! The number was {pc}.")
            break
    answer = input("want you to play again? (y/n): ")
    if answer == "y" or answer == "Y":
        continue
    elif answer == "n" or answer == "N":
        print("GoodBye")
        break