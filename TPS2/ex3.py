def ajouter_id(nouvel_id , liste_ids=None):
    if liste_ids == None:
        liste_ids = []
    liste_ids.append(nouvel_id)
    return liste_ids


groupe1 = ajouter_id(101)
groupe2 = ajouter_id(102)
groupe3 = ajouter_id(103, [999])

print("Groupe 1 :", groupe1)
print("Groupe 2 :", groupe2)
print("Groupe 3 :", groupe3)