txt = "i use arch btw"
word = []
voy = ["a", "e", "i", "o", "u", "y"]
nbrv = 0

def Lng_nb_voy(txt,word,voy,nbr):
    for i in range(len(txt)):
        if txt[i] != " ":
            word.append(txt[i])
        elif txt[i] == " ":
            for i in word:
                if i in voy:
                    nbr += 1
                else:
                    continue
            
            print(len(word))
            print(f"{nbr}\n\n")
            word = []
        nbr = 0
Lng_nb_voy(txt,word,voy,nbrv)