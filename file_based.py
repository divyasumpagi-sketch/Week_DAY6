# File-based record system
filename = "records.txt"

def add_record():
    with open(filename, "a") as f:
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        f.write(f"{name},{age}\n")
    print("Record added successfully!")

def view_records():
    with open(filename, "r") as f:
        print("\n--- Records ---")
        for line in f:
            name, age = line.strip().split(",")
            print(f"Name: {name}, Age: {age}")

while True:
    print("\n--- File Record System ---")
    print("1. Add Record\n2. View Records\n3. Exit")
    choice = input("Enter choice: ")
    if choice == "1": add_record()
    elif choice == "2": view_records()
    elif choice == "3": break
    else: print("Invalid choice!")