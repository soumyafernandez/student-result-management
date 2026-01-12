def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"


def add_student():
    name = input("Enter student name: ")
    marks = []

    for i in range(1, 6):
        mark = int(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / 5
    grade = calculate_grade(percentage)

    with open("students.txt", "a") as file:
        file.write(f"{name},{total},{percentage},{grade}\n")

    print("\nStudent record added successfully!\n")


def view_students():
    print("\n--- Student Records ---")
    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, total, percentage, grade = line.strip().split(",")
                print(f"Name: {name} | Total: {total} | Percentage: {percentage}% | Grade: {grade}")
    except FileNotFoundError:
        print("No records found.")


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
