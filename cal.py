while(True):
    user = input("do you want to use the cal (Y/N): ")
    if user.lower() == "y":
        x = float(input("Entree la valeur de x : "))
        op = input("entree une opereration (+,-,/,*) : ")
        y = float(input("Entree la valeur de y : "))

        if op == "+":
            sum = x + y
            print(f"la somme des deux nombres x et y est: {sum}")
        elif op == "*":
            pro = x*y
            print(f"le produit des deux nombres x et y est: {pro}")
        elif op == "/":
            div = x/y
            print(f"le resultat de la division des deux nombres x et y est: {div}")
        elif op == "-":
            sous = x-y
            print(f"le resultat de la soustraction des deux nombres x et y est: {sous}")
        else:
            print("invalid value!")
    elif user.lower() == "n":
        print("Good Bye")
        break
    else:
        print("invalid Value!")
