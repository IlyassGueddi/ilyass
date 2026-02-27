ma_liste = [1, 2, 3]
mon_tuple = (10, 20, ma_liste)

mon_tuple[2].append(4)
print(mon_tuple)

#ma_liste is just a pointer so it's not considered as a value of a tuple so we can change it ma_liste



etudiant_A = {"nom": "Ali", "notes": [12, 14]}
etudiant_B = etudiant_A
etudiant_B["nom"] = "Sara"
etudiant_B["notes"].append(16)

print(etudiant_A["nom"], etudiant_A["notes"])

#in python etudiant_B = etudiant_A did not copy etudiant_A to etudiant_B 
#unlike other languages like C