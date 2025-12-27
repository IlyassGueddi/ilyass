students = {
    "std1" : [10,18,19,20,5,12],
    "std2" : [6,16,11,15,9,15],
    "std3" : [14,18,10,15,11,14],
}
somme = 0
moyenne = 0
sumg = 0
moyg = 0
index = 0
def mpyenne(sudent,moy,som,sumg,moyg,index):
    for i in sudent:
        som = 0
        for j in range(len(i)):
            som += sudent[i][j]
        moy = som / len(i)
        sumg += moy
        index += 1
        moyg = sumg / index
        print(f"la moyenne de {i} est : {moy}")
    print(f"le moyenne general est: {moyg}")

mpyenne(students,moyenne,somme,moyg,sumg,index)