somme = 0
conteur = 0
while(somme < 100):
    user = int(input("entre une n entier: "))
    somme += user 
    conteur += 1 

print(f"le somme est {somme}")
print(f"le nbr des entiers entre est {conteur}")