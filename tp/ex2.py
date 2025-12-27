scores = (45,78,90,56,67)
scores_5 = []

for i in scores:
    scores_5.append(i-5)

scores_5 = tuple(scores_5)

for i in scores:
    if i > 60:
        print(i)
        break

if 50 in scores:
    print("50 existe")
else :
    print ("no")