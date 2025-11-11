'''year = int(input("Give me a year: "))

if (year % 400 == 0) or (year % 4 == 0 and not year % 100 == 0):
    print(f"{year} is bissextile")
else :
    print(f"{year} is not bissextile")'''

start = int(input("Enter the starting year : "))
end = int(input("Enter the end year : "))

for start in range(start,end):
    if (start % 400 == 0) or (start % 4 == 0 and not start % 100 == 0):
        print(start)
        start += 1
    else :
        continue