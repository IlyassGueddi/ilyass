import os
import json

class tasks:
    def __init__(self, ID):
        self.title = input("\n \nset a title for the new task: ")
        self.description = input("\nset a description for the new task: ")
        self.ID = ID
        self.done = False

    def add_task(self):
        print(f"\ntask added: {self.title} - {self.description} (ID: {self.ID})")
    
    def mark_as_done(self):
        self.done = True
    
    def to_dict(self):
        return{
            "ID": self.ID,
            "title": self.title,
            "description": self.description,
            "done": self.done
        }

tasks_gr = []
the_task_ID = 1

while True:

    # Main Menu
    print("\n__________HELLO__________")
    print("1- Tasks")
    print("2- Notes")
    print("3- Journaling")
    print("4- Timer")
    print("5- Exist")
    user_choice = str(input("choose a number from 1 to 5: "))

    # Tasks 
    if user_choice == "1":

        # Tasks Menu
        print("\n \n__________TASKS__________")
        print("1- Add new task")
        print("2- Mark a task as done")
        print("3- Show tasks")
        print("4- Delete tassk")
        user_choice_task = str(input("choose a number from 1 to 4: "))

        if user_choice_task == "1":
             # Create a new task (this will ask the user for title and description)
            new_task = tasks(the_task_ID)
            # Add it to the tasks list
            tasks_gr.append(new_task)
            # Confirm to the user
            new_task.add_task()
            # Increment task_ID for the next task
            the_task_ID += 1
        
        else:
            break 

    elif user_choice == "5":
        break

with open("tasks.json", "w") as f:
    json.dump([t.to_dict() for t in tasks], f, indent=4)