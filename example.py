user0 = input(">")

if user0.lower() == "help":
    print("start - to start the car")
    print("stop - to stop the car")
    print("quit - to exit")
    while True:
        user = input(">")
        if user.lower() == "start":
            print("car started... and ready to go")
        elif user.lower() == "stop":
            print("car  stopped.")
        elif user.lower()== "quit" or user.lower()== "exit":
            print("GoodBye")
            break
        else:
            print("i can't understand...")
else:
    print("i can't understand...")