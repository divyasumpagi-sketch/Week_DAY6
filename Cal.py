# Calculator using functions
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error! Division by zero."

while True:
    print("\n--- Calculator ---")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = input("Enter choice: ")
    if choice in ["1", "2", "3", "4"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if choice == "1": print("Result:", add(a, b))
        elif choice == "2": print("Result:", subtract(a, b))
        elif choice == "3": print("Result:", multiply(a, b))
        elif choice == "4": print("Result:", divide(a, b))
    elif choice == "5":
        break
    else:
        print("Invalid choice!")
