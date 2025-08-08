import random
import json

def load_flashcards(flashcards):
    try:
        with open(flashcards, 'r') as file:
            flashcards = json.load(file)
        return flashcards
    except FileNotFoundError:
        return {}
    except json.decoder.JSONDecodeError:
        return {}
    
def save_flashcards(flashcard, flashcards):
    with open(flashcards, 'w') as file:
        json.dump(flashcard, file, indent=4)

while True:
    print("\n----------FlashCards----------")
    print("\nWhat do you ask for?")
    print("\n1.Add a flash card")
    print("2.view flash cards")
    print("3.start challenge")
    choice =str(input("\nenter the number of your choice: "))
    if choice == "1":
        question = print(str(input("\n entre the question here: ")))
        reponce = print(str(input("\n entre the reponse here: ")))
        save_flashcards(question)
        save_flashcards(reponce)
    elif choice == "2":
        print("\n ----------Those Are Your FlashCards----------")
        load_flashcards()
    