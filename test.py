import random
user=0
question="yes"
pc = random.randint(1, 10)
while user!=pc and question != "no" :
      user = int(input("what you think the number use: "))

      
      if pc>= user :
       print("bigger")
      if pc<=user:
       print("lowwer")
      if pc==user:
       print("you win.")
      question = input("can we play again? ")