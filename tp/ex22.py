liste = [1,2,3,4,5,7,6]
defr = []

def deffirent(listt, defr):
    for i in listt :
        if i in defr:
            print("the array elements arren't different!")
            break
        elif (i == len(listt)-1) and (not i in defr):
            print("the array elements are different.")
        else:
            defr.append(i)
            i += 1

deffirent(liste,defr)