
# 1. num
# 2. add people
# 3. pop after 2 min

def finish (mystack):
  while True:
    if len(mystack) < 10:
        # add the 10 first names
        name = str(input("\nentre the full name of the customer: "))
        mystack.append(name)
        ava = len(mystack)
        print(f"your number is {ava}, wait for your turn.")
    else:
        # searching to remove from the list
        print("Queue is full. Someone needs to be removed.")

        customer_name = mystack[0] 
        print(f"\nNow serving {customer_name}.")
        balance = float(input(f"Enter current balance for {customer_name}: "))
        while True:
          print(f"\nChoose an action for {customer_name}:")
          print("1. Add money")
          print("2. Withdraw money")
          print("3. Check balance")
          print("4. Finish service")
          choice = input("Enter choice (1-4): ")

          if choice == "1":
              amount = float(input("Amount to add: "))
              balance += amount
              print(f"New balance: {balance} MAD")
          elif choice == "2":
              amount = float(input("Amount to withdraw: "))
              if amount <= balance:
                  balance -= amount
                  print(f"New balance: {balance} MAD")
              else:
                  print("Insufficient funds.")
          elif choice == "3":
              print(f"Current balance: {balance} MAD")
          elif choice == "4":
              print(f"Service completed for {customer_name}.")
              break
          else:
              print("Invalid option.")

        
          # removing the first person and adding an other one
          removed_name = mystack.pop(0)
          print(f"{removed_name} has been served and removed.")
          name = str(input("entre the full name of the new customer: "))
          mystack.append(name)
          ava = len(mystack)
          print(f"your number is {ava}, wait for your turn.")
        else:
          # waithing for a customer to be served and adding someone in his place
          print(input("Waiting until a customer is served... (if someone has been served print yes): ").lower())
          name = str(input("enter the full name of the new customer: "))
          mystack.append(name)
          ava = len(mystack)
          print(f"your number is {ava}, wait for your turn.")
    
mystack = []
finish(mystack)

'''
print("initial stack: ", mystack)
print(mystack.pop())
print(mystack.pop())
print("the new stack after pop: ", mystack)
mystack.append(78)
print("the new stack after push: ", mystack)
'''
'''
j1 = [1, 2, 66, 29]
j12 = [33, 1, 2, 66, 29]
def afficher(A):
  i=0
  for i in range(0, len(A)):
    i+=1
  return i

print(afficher(j1))
afficher(j12)
'''