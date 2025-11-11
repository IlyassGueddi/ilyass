
user = int(input("Entre le nbr des notes n tu va entrer: "))
somme = 0
for i in range(0,user):
    note = int(input("Entre la note : "))
    somme += note 

moyenne = somme / user
print(f"la moyenne des notes est: {moyenne}")