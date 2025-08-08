
tasks = []

def show_menu():
  print("\n----------To Do List----------")
  print("1. Show tasks")
  print("2. Add tasks")
  print("3. Remove task")
  print("4. Exit")
  return input("\n Entre a number: ")


def show_tasks():
  if not tasks:
    print("No tasks yet.")
  else:
    for i, task in enumerate(tasks, 1):
      print(f"{i}. {task}")


while True:
  choice = show_menu()

  if choice == '1':
    print("\n-----Todays List-----")
    show_tasks()
  elif choice == '2':
    #Add New Task Here
    print("\n-----Add New Task-----")
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added.")
  elif choice == '3':
    #Remove A Task
    show_tasks()
    try:
      task_number = int(input("Enter task number to remove: "))
      if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Removed: {removed}")
      else:
        print("Invalid number.")
    except ValueError:
      print("Please enter a number.")
  elif choice == '4':
    # Exist the program
    print("good bye")
    break
  else:
    print("Invalid choice.")