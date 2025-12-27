temp_max = {
    "lundi": 22,
    "mardi": 24,
    "mercredi": 21,
    "jeudi": 26,
}

temp_max_2 = {
}

for jour in temp_max:
    temp_max_2[jour] = temp_max[jour]

tempbase = 100
tempbasej = 0

for temp in temp_max_2:
    if temp_max_2[temp] < tempbase:
        tempbase = temp_max_2[temp]
        tempbasej = temp
    else:
        continue

print(f"le jour de plus base {tempbasej} et de tempurature {tempbase}C. ")

for jr in temp_max:
    if jr == "vendredi":
        print("vendredi existe!")
    else :
        continue