import os
import json

class tasks:
    def __init__(self, ID, title=None, description=None, done=False):
        # If creating from saved data, use provided values
        if title is not None and description is not None:
            self.title = title
            self.description = description
        else:
            # If creating new task, ask user for input
            self.title = input("\n \nset a title for the new task: ")
            self.description = input("\nset a description for the new task: ")
        
        self.ID = ID
        self.done = done

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
    
    @classmethod
    def from_dict(cls, data):
        """Create a task object from dictionary data"""
        return cls(data["ID"], data["title"], data["description"], data["done"])
    
def save_tasks(tasks_list, filename="tasks.json"):
    """Save tasks to a JSON file"""
    try:
        with open(filename, 'w') as f:
            # Convert all task objects to dictionaries
            tasks_data = [task.to_dict() for task in tasks_list]
            json.dump(tasks_data, f, indent=2)
        print(f"Tasks saved to {filename}")
    except Exception as e:
        print(f"Error saving tasks: {e}")


def load_tasks(filename="tasks.json"):
    """Load tasks from a JSON file"""
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                tasks_data = json.load(f)
                # Convert dictionaries back to task objects
                loaded_tasks = [tasks.from_dict(data) for data in tasks_data]
                print(f"Loaded {len(loaded_tasks)} tasks from {filename}")
                return loaded_tasks
        else:
            print(f"No saved tasks found. Starting fresh.")
            return []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []
    

def get_next_task_id(tasks_list):
    """Get the next available task ID"""
    if not tasks_list:
        return 1
    return max(task.ID for task in tasks_list) + 1


# Load existing tasks at startup
tasks_gr = load_tasks()
the_task_ID = get_next_task_id(tasks_gr)
    

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
        print("5- Back tomain menu")
        user_choice_task = str(input("choose a number from 1 to 5: "))

        if user_choice_task == "1":
             # Create a new task (this will ask the user for title and description)
            new_task = tasks(the_task_ID)
            # Add it to the tasks list
            tasks_gr.append(new_task)
            # Confirm to the user
            new_task.add_task()
            # Increment task_ID for the next task
            the_task_ID += 1
            # Save tasks after adding
            save_tasks(tasks_gr)

        elif user_choice_task == "2":
            if not tasks_gr:
                print("No tasks available to mark as done.")
            else:
                print("\nAvailable tasks:")
                for task in tasks_gr:
                    status = "✓" if task.done else "○"
                    print(f"{status} ID: {task.ID} - {task.title}")
                
                try:
                    task_id = int(input("Enter task ID to mark as done: "))
                    task_found = False
                    for task in tasks_gr:
                        if task.ID == task_id:
                            task.mark_as_done()
                            print(f"Task '{task.title}' marked as done!")
                            task_found = True
                            save_tasks(tasks_gr)  # Save after marking done
                            break
                    if not task_found:
                        print("Task not found!")
                except ValueError:
                    print("Please enter a valid task ID number.")
        
        elif user_choice_task == "3":
            if not tasks_gr:
                print("No tasks available.")
            else:
                print("\n--- ALL TASKS ---")
                for task in tasks_gr:
                    status = "✓ DONE" if task.done else "○ PENDING"
                    print(f"{status} | ID: {task.ID} | {task.title} - {task.description}")
        
        elif user_choice_task == "4":
            if not tasks_gr:
                print("No tasks available to delete.")
            else:
                print("\nAvailable tasks:")
                for task in tasks_gr:
                    status = "✓" if task.done else "○"
                    print(f"{status} ID: {task.ID} - {task.title}")
                
                try:
                    task_id = int(input("Enter task ID to delete: "))
                    task_found = False
                    for i, task in enumerate(tasks_gr):
                        if task.ID == task_id:
                            deleted_task = tasks_gr.pop(i)
                            print(f"Task '{deleted_task.title}' deleted!")
                            task_found = True
                            save_tasks(tasks_gr)  # Save after deleting
                            break
                    if not task_found:
                        print("Task not found!")
                except ValueError:
                    print("Please enter a valid task ID number.")
        
        elif user_choice_task == "5":
            continue  # Go back to main menu
        
        else:
            print("Invalid choice. Please choose 1-5.")

    elif user_choice == "5":
        # Save tasks before exiting
        save_tasks(tasks_gr)
        print("Tasks saved. Goodbye!")
        break
    
    else:
        if user_choice in ["2", "3", "4"]:
            print(f"Feature {user_choice} not implemented yet.")
        else:
            print("Invalid choice. Please choose 1-5.")