import random

length = int(input("set the number of characthers you want in your code: "))
 
characthers = "qwertyuiopasdfghjklzxcvbnm"
numbers = "1234567890"
others = "!@#$%^&*>?<<"

password = ""

for i in range(length):
  passw1 = random.choice(characthers)
  passw2 = random.choice(numbers)
  passw3 = random.choice(others)
  password += passw1 + passw3 + passw2

print(f"your password is {password}")
