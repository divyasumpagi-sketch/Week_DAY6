# Student Management System
students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    students[roll] = {"Name": name, "Course": course}
    print("Student added successfully!")

def view_students():
    for roll, info in students.items():
        print(f"Roll: {roll}, Name: {info['Name']}, Course: {info['Course']}")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student\n2. View Students\n3. Delete Student\n4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
