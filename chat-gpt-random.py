import random  # we use this to generate random numbers

# this will keep the game running forever until the user quits
while True:
    pc = random.randint(1, 10)  # computer picks a number from 1 to 10
    print("I picked a number between 1 and 10.")

    while True:
        user_input = input("What do you think the number is? (or 'q' to quit): ")

        # check if user wants to quit
        if user_input == "q":
            print("Goodbye!")
            exit()  # this stops the whole program

        # turn the input into a number
        user = int(user_input)

        # compare the user's guess with the pc number
        if user < pc:
            print("My number is bigger.")
        elif user > pc:
            print("My number is smaller.")
        else:
            print("🎉 You guessed it!")
            break  # you guessed right → break this round and start a new one
