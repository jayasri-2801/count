from src.student import add_student
from src.attendance import mark_attendance, view_attendance

while True:
    print("\n--- Student Attendance Management System ---")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        view_attendance()
    elif choice == "4":
        print("Exiting system...")
        break
    else:
        print("Invalid choice")
