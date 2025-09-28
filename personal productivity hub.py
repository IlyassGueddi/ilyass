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






class notes:
    def __init__(self, NID, note_title = None, note = None):
        if note_title is not None and note is not None:
            self.note_title = note_title
            self.note = note
        else:
            self.note_title = input("\n \nset a title for the new note: ")
            self.note = input("\nwrite your note: ")

        self.NID = NID

    def add_note(self):
        print(f"\ntask added: {self.note_title} (NID: {self.NID})")

    def note_dict(self):
        return{
            "NID": self.NID,
            "note_title": self.note_title,
            "note": self.note
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a note object from dictionary data"""
        return cls(data["NID"], data["note_title"], data["note"])
    
def save_notes(notes_list, filename ="notes.json"):
    """Save notes to a JSON file"""
    try:
        with open(filename, 'w') as f:
            # Convert all notes objects to dictionaries
            notes_data = [note.note_dict() for note in notes_list]
            json.dump(notes_data, f, indent=2)
        print(f"note saved to {filename}")
    except Exception as e:
        print(f"Error saving notes: {e}")

def load_notes(filename="notes.json"):
    """Load notes from a JSON file"""
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                notes_data = json.load(f)
                # Convert dictionaries back to notes objects
                loaded_notes = [notes.from_dict(data) for data in notes_data]
                print(f"Loaded {len(loaded_notes)} tasks from {filename}")
                return loaded_notes
        else:
            print(f"No saved notes found. Starting fresh.")
            return []
    except Exception as e:
        print(f"Error loading notes: {e}")
        return []
    
def get_next_note_nid(notes_list):
    """Get the next available note NID"""
    if not notes_list:
        return 1
    return max(note.NID for note in notes_list) + 1





class journals:
    def __init__(self, JID, date=None, title=None, main=None):
        # If creating from saved data, use provided values
        if date is not None and main is not None:
            self.date = date
            self.main = main
            self.title = title
        else:
            # If creating new journal, ask user for input
            self.date = input("\n \nset today's date: ")
            self.title = input("\n \nset today's title: ")
            self.description = input("\nfeel free to say what's in your heart: ")
        
        self.JID = JID

    def add_journal(self):
        print(f"\njournal added: {self.date} - {self.title}  (JID: {self.JID})")
    
    def to_dict(self):
        return{
            "JID": self.JID,
            "date": self.date,
            "title": self.title,
            "main": self.main,
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a journal object from dictionary data"""
        return cls(data["JID"], data["date"], data["title"], data["main"])
    
def save_journals(journals_list, filename="journals.json"):
    """Save journals to a JSON file"""
    try:
        with open(filename, 'w') as f:
            # Convert all journal objects to dictionaries
            journals_data = [journal.to_dict() for journal in journals_list]
            json.dump(journals_data, f, indent=2)
        print(f"journals saved to {filename}")
    except Exception as e:
        print(f"Error saving journals: {e}")


def load_journals(filename="journas.json"):
    """Load journals from a JSON file"""
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                journals_data = json.load(f)
                # Convert dictionaries back to journal objects
                loaded_journals = [journals.from_dict(data) for data in journals_data]
                print(f"Loaded {len(loaded_journals)} journals from {filename}")
                return loaded_journals
        else:
            print(f"No saved journals found. Starting fresh.")
            return []
    except Exception as e:
        print(f"Error loading journals: {e}")
        return []
    
def get_next_journal_jid(journals_list):
    """Get the next available journal JID"""
    if not journals_list:
        return 1
    return max(journal.JID for journal in journals_list) + 1




# Load existing journals at startup
journals_gr = load_journals()
the_journal_JID = get_next_journal_jid(journals_gr)


# Load existing tasks at startup
tasks_gr = load_tasks()
the_task_ID = get_next_task_id(tasks_gr)


# Load existing notes at startup
notes_gr = load_notes()
the_note_NID = get_next_note_nid(notes_gr)



while True:

    # Main Menu
    print("\n__________HELLO__________")
    print("1- Tasks")
    print("2- Notes")
    print("3- Journaling")
    print("4- Timer")
    print("5- Exit")
    user_choice = str(input("choose a number from 1 to 5: "))

    # Tasks 
    if user_choice == "1":

        # Tasks Menu
        print("\n \n__________TASKS__________")
        print("1- Add new task")
        print("2- Mark a task as done")
        print("3- Show tasks")
        print("4- Delete task")
        print("5- Back to main menu")
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

    
    # Notes
    elif user_choice == "2":
        print("\n \n__________NOTES__________")
        print("1- Add note")
        print("2- Show notes")
        print("3- Delete note")
        print("4- Back to main menu")
        user_choice_note = str(input("choose a number from 1 to 4: "))
        if user_choice_note == "1":
        # Create a new note (this will ask the user for note title and note)
                new_note = notes(the_note_NID)
                # Add it to the notes list
                notes_gr.append(new_note)
                # Confirm to the user
                new_note.add_note()
                # Increment note_NID for the next note
                the_note_NID += 1
                # Save notes after adding
                save_notes(notes_gr)

        elif user_choice_note == "2":
                    if not notes_gr:
                        print("No notes available.")
                    else:
                        print("\n--- ALL NOTES ---")
                        for note in notes_gr:
                            print(f"NID: {note.NID} | {note.note_title} - {note.note}")

        elif user_choice_note == "3":
                    if not notes_gr:
                        print("No notes available to delete.")
                    else:
                        print("\nAvailable notes:")
                        for note in notes_gr:
                            print(f"NID: {note.NID} - {note.note_title}")
                        
                        try:
                            note_nid = int(input("Enter note NID to delete: "))
                            note_found = False
                            for i, note in enumerate(notes_gr):
                                if note.NID == note_nid:
                                    deleted_note = notes_gr.pop(i)
                                    print(f"note '{deleted_note.note_title}' deleted!")
                                    note_found = True
                                    save_notes(notes_gr)  # Save after deleting
                                    break
                            if not note_found:
                                print("note not found!")
                        except ValueError:
                            print("Please enter a valid note NID number.")

        elif user_choice_note == "4":
            continue  # Go back to main menu
                
        else:
            print("Invalid choice. Please choose 1-4.")


    elif user_choice == "3":
        print("\n \n__________JOURNALING__________")
        print("1- create a new journal entry")
        print("2- display all entries")
        print("3- remove an entry")
        print("4- Back to main menu")
        user_choice_journal = str(input("choose a number from 1 to 4: "))
        if user_choice_journal == "1":
        # Create a new journal (this will ask the user for journal title, date and note)
                new_journal = journals(the_journal_JID)
                # Add it to the journales list
                journals_gr.append(new_journal)
                # Confirm to the user
                new_journal.add_journal()
                # Increment journal_JID for the next journal
                the_note_NID += 1
                # Save notes after adding
                save_journals(journals_gr)

        elif user_choice_journal == "2":
                    if not journals_gr:
                        print("No journals available.")
                    else:
                        print("\n--- ALL JOURNALS ---")
                        for journal in journals_gr:
                            print(f"JID: {journal.JID} - {journal.date} | {journal.title} - {journal.main}")

        elif user_choice_journal == "3":
                    if not journals_gr:
                        print("No journals available to delete.")
                    else:
                        print("\nAvailable journals:")
                        for journal in journals_gr:
                            print(f"JID: {journal.JID} | {journal.date} - {journal.title}")
                        
                        try:
                            journal_jid = int(input("Enter Journal JID to delete: "))
                            journal_found = False
                            for i, journal in enumerate(journals_gr):
                                if journal.JID == journal_jid:
                                    deleted_journal = journals_gr.pop(i)
                                    print(f"journal '{deleted_journal.title}' deleted!")
                                    journal_found = True
                                    save_journals(journals_gr)  # Save after deleting
                                    break
                            if not journal_found:
                                print("journal not found!")
                        except ValueError:
                            print("Please enter a valid journal JID number.")

        elif user_choice_journal == "4":
            continue  # Go back to main menu
                
        else:
            print("Invalid choice. Please choose 1-4.")
            


    # Exit
    elif user_choice == "5":
        # Save tasks before exiting
        save_tasks(tasks_gr)
        print("Tasks saved. Goodbye!")
        break
    
    else:
        if user_choice in ["4"]:
            print(f"\n Feature {user_choice} not implemented yet.")
        else:
            print("Invalid choice. Please choose 1-5.")