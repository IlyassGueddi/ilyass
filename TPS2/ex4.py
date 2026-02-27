donnees_brutes = [
("Amine", "14, 12, 16"),
("Fatima", "8, 9, 11"),
("Youssef", "15, 18, 14"),
("Khadija", "10, 10, 9")
]

def calculer_moyenne(chaine_notes = [], dictt = []):
    i = 0
    for student in chaine_notes:
        # les notes 
        studentL = list(student)
        studentN = studentL[1]
        studentN = studentN.split(",")

        #students name
        student_name = studentL[1]

        #calcule la somme
        somme = 0
        for i in range(3):
            studentN[i] = int(studentN[i])
            somme = studentN[i] + somme
        moyenne = somme / 3

        #dict
        lis = []
        lis.append(moyenne)
        if moyenne >= 10:
            lis.append("valid")
        elif moyenne < 10:
            lis.append("ratt")

        dictt[i] = (student_name, lis)
        i += 1
        lis = []

        return moyenne
    

students = []
calculer_moyenne(donnees_brutes)