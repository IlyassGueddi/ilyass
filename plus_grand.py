while(True):
    user = input("Entre Y to continue et N to exit: (Y/N) ")
    if user.lower() == "y":
        a = float(input("give me a number: "))
        b = float(input("give me a number: "))
        c = float(input("give me a number: "))

        if a > b and a  > c :
            print(f"Le plus grand nombre est {a}")
        elif b > a and b  > c :
            print(f"Le plus grand nombre est {b}")
        elif c > b and c  > a :
            print(f"Le plus grand nombre est {c}")
        else:
            print("il exist au moins deux nombres grandes et egaux: ")
    elif user.lower() == "N":
        print("Good Bye")
        break

    else:
        print("invalid value!")