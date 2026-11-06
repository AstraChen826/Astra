
import json
import csv
import os

DATA_FILE = "students.json"


# 1. Load student data
def load_students():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not load student data.")
    return []


# 2. Save student data
def save_students(students):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4, ensure_ascii=False)


# 3. Get a valid score
def get_score():
    while True:
        try:
            score = float(input("Enter score (0-100): "))
            if 0 <= score <= 100:
                return score
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


# 4. Add a student
def add_student(students):
    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if any(s["id"] == student_id for s in students):
        print("Student ID already exists.")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    score = get_score()

    student = {
        "id": student_id,
        "name": name,
        "score": score
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


# 5. Display all students
def display_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n" + "=" * 55)
    print(f"{'ID':<15}{'Name':<25}{'Score':<10}")
    print("=" * 55)

    for student in students:
        print(
            f"{student['id']:<15}"
            f"{student['name']:<25}"
            f"{student['score']:<10.2f}"
        )

    print("=" * 55)


# 6. Search for a student
def search_student(students):
    student_id = input("Enter student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Score:", student["score"])
            return

    print("Student not found.")


# 7. Update student information
def update_student(students):
    student_id = input("Enter student ID to update: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("Leave the input blank to keep the current value.")

            new_name = input(
                f"New name ({student['name']}): "
            ).strip()

            if new_name:
                student["name"] = new_name

            change_score = input(
                "Update score? (y/n): "
            ).strip().lower()

            if change_score == "y":
                student["score"] = get_score()

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found.")


# 8. Delete a student
def delete_student(students):
    student_id = input("Enter student ID to delete: ").strip()

    for student in students:
        if student["id"] == student_id:
            confirm = input(
                f"Delete {student['name']}? (y/n): "
            ).strip().lower()

            if confirm == "y":
                students.remove(student)
                save_students(students)
                print("Student deleted successfully!")
            else:
                print("Deletion cancelled.")
            return

    print("Student not found.")


# 9. Calculate average score
def calculate_average(students):
    if not students:
        print("No student records available.")
        return

    average = sum(
        student["score"] for student in students
    ) / len(students)

    print(f"Class average score: {average:.2f}")


# 10. Display student ranking
def display_ranking(students):
    if not students:
        print("No student records available.")
        return

    ranked_students = sorted(
        students,
        key=lambda student: student["score"],
        reverse=True
    )

    print("\n===== Student Ranking =====")

    for rank, student in enumerate(ranked_students, start=1):
        print(
            f"{rank}. {student['name']} "
            f"- {student['score']:.2f}"
        )


# 11. Export data to CSV
def export_csv(students):
    if not students:
        print("No data to export.")
        return

    with open(
        "students_export.csv",
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["id", "name", "score"]
        )

        writer.writeheader()
        writer.writerows(students)

    print("Data exported to students_export.csv!")


# 12. Main menu
def display_menu():
    print("\n" + "=" * 40)
    print("   STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Average Score")
    print("7. Display Ranking")
    print("8. Export CSV")
    print("0. Exit")
    print("=" * 40)


# 13. Main program
def main():
    students = load_students()

    print("Welcome to Student Management System!")

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            calculate_average(students)

        elif choice == "7":
            display_ranking(students)

        elif choice == "8":
            export_csv(students)

        elif choice == "0":
            save_students(students)
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
