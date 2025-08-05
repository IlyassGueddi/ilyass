import random

num1 = random.randint()
num2 = int(input("what you think the number use: "))
print(num1)

while num1<= 10 :
 if num1 + 2 >= num2 > num1 or num2 - 2 <= num1 < num2 :
    print("you are close!")
    num2 = int(input("what you think the number use: "))
 elif num1 > num2 + 2 or num1 < num2 -2 :
    print("false")
    num2 = int(input("what you think the number use: "))
 elif num1 == num2:
    print("you win.")
    question = str(input("can we play againhhhh? (yes/no)"))
   
   
   
    if question == "yes" :
     num1 =1
     num2 = int(input("what you think the number use: "))
    while num1<= 10 and question != "no" :
        num2 = int(input("what you think the number use: "))
        if num1 + 2 >= num2 > num1 or num2 - 2 <= num1 < num2 :
          print("you are close!")

        elif num1 > num2 + 2 or num1 < num2 -2 :
          print("false")
        if num1== num2:
          print("you win.")
        
        question = input("can we play again? ")
    
    print("end")
    break