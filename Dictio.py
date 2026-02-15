# Dictionary Application
dictionary = {
    "Python": "A high-level programming language.",
    "Algorithm": "A step-by-step procedure to solve a problem.",
    "Database": "An organized collection of data."
}

def search_word():
    word = input("Enter word to search: ")
    print(dictionary.get(word, "Word not found in dictionary."))

def add_word():
    word = input("Enter new word: ")
    meaning = input("Enter meaning: ")
    dictionary[word] = meaning
    print("Word added successfully!")

while True:
    print("\n--- Dictionary Application ---")
    print("1. Search Word\n2. Add Word\n3. Exit")
    choice = input("Enter choice: ")
    if choice == "1": search_word()
    elif choice == "2": add_word()
    elif choice == "3": break
    else: print("Invalid choice!")

