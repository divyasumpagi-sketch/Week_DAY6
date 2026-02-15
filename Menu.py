# Menu-driven program
def greet(): print("Hello! Welcome to the program.")
def square():
    num = int(input("Enter a number: "))
    print("Square:", num ** 2)
def cube():
    num = int(input("Enter a number: "))
    print("Cube:", num ** 3)

while True:
    print("\n--- Menu ---")
    print("1. Greet\n2. Square\n3. Cube\n4. Exit")
    choice = input("Enter choice: ")
    if choice == "1": greet()
    elif choice == "2": square()
    elif choice == "3": cube()
    elif choice == "4": break
    else: print("Invalid choice!")