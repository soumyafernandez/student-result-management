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
        while True:
            try:
                mark = int(input(f"Enter marks for subject {i} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

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
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
	search_student()
    elif choice == "4":
        print("Exiting program...")
        break
    else: print("Invalid choice. Try again.")

def search_student():
	search_name = input("Enter student name to search: ").lower()
	found = False

	try:
		with open("students.txt", "r") as file:
			for line in file:
				name, total, percentage, grade = line.strip().split(",")
				if name.lower() == search_name:
					print("\n--- Student Found ---")
					print(f"Name: {name}")
					print(f"Total: {total}")
					print(f"Percentage: {percentage}%")
					print(f"Grade: {grade}")
					found = True
					break
	except FileNotFoundError:
		print("No records found.")

	if not found:
		print("Student not found.")
