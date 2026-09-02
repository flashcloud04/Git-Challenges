from datetime import datetime
import json
import os


# ============================================================
# APPLICATION CONFIGURATION
# ============================================================

APP_NAME = "Student Management System"
APP_VERSION = "1.0.0"

DATA_FILE = "students.json"


# ============================================================
# STUDENT CLASS
# ============================================================

class Student:
    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 80:
            return "A+"
        elif self.marks >= 90:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

    def to_dictionary(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks,
            "grade": self.calculate_grade()
        }

    def display(self):
        print("-" * 70)
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Course     : {self.course}")
        print(f"Marks      : {self.marks}")
        print(f"Grade      : {self.calculate_grade()}")
        print("-" * 60)


# ============================================================
# SAMPLE STUDENT DATA
# ============================================================

students = [
    Student(101, "Adnan", 20, "Python", 91),
    Student(102, "zufi", 21, "Cloud Computing", 84),
    Student(103, "Ali", 19, "Cyber Security", 76),
    Student(104, "Fatima", 22, "Data Science", 68),
    Student(105, "Usman", 20, "Artificial Intelligence", 55),
]


# ============================================================
# APPLICATION FUNCTIONS
# ============================================================

def show_header():
    print()
    print("=" * 70)
    print(APP_NAME)
    print(f"Version: {APP_VERSION}")
    print("=" * 70)
    print(f"Server Time: {datetime.now()}")
    print()


def show_all_students():
    print("\nALL STUDENTS")
    print("=" * 70)

    if not students:
        print("No students available.")
        return

    for student in students:
        student.display()


def search_student():
    print("\nSEARCH STUDENT")
    print("=" * 70)

    student_id = input("Enter Student ID: ")

    for student in students:
        if str(student.student_id) == student_id:
            print("\nStudent found:")
            student.display()
            return

    print("Student not found.")


def add_student():
    print("\nADD NEW STUDENT")
    print("=" * 70)

    try:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        new_student = Student(
            student_id,
            name,
            age,
            course,
            marks
        )

        students.append(new_student)

        print("\nStudent added successfully!")
        new_student.display()

    except ValueError:
        print("Invalid input. Please enter valid values.")


def delete_student():
    print("\nDELETE STUDENT")
    print("=" * 70)

    student_id = input("Enter Student ID: ")

    for student in students:
        if str(student.student_id) == student_id:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def show_statistics():
    print("\nSTUDENT STATISTICS")
    print("=" * 70)

    if not students:
        print("No data available.")
        return

    total_students = len(students)

    total_marks = sum(student.marks for student in students)

    average_marks = total_marks / total_students

    highest_student = max(
        students,
        key=lambda student: student.marks
    )

    lowest_student = min(
        students,
        key=lambda student: student.marks
    )

    print(f"Total Students : {total_students}")
    print(f"Average Marks  : {average_marks:.2f}")

    print(
        f"Highest Marks  : "
        f"{highest_student.name} "
        f"({highest_student.marks})"
    )

    print(
        f"Lowest Marks   : "
        f"{lowest_student.name} "
        f"({lowest_student.marks})"
    )


# ============================================================
# FILE HANDLING
# ============================================================

def save_students():
    data = []

    for student in students:
        data.append(student.to_dictionary())

    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

        print("\nStudent data saved successfully.")

    except Exception as error:
        print(f"Error while saving data: {error}")


def load_students():
    global students

    if not os.path.exists(DATA_FILE):
        print("No saved student file found.")
        return

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        students = []

        for item in data:
            student = Student(
                item["student_id"],
                item["name"],
                item["age"],
                item["course"],
                item["marks"]
            )

            students.append(student)

        print("Student data loaded successfully.")

    except Exception as error:
        print(f"Error while loading data: {error}")


# ============================================================
# MENU
# ============================================================

def show_menu():
    print("\n")
    print("=" * 70)
    print("MAIN MENU")
    print("=" * 70)

    print("1. Show All Students")
    print("2. Search Student")
    print("3. Add Student")
    print("4. Delete Student")
    print("5. Show Statistics")
    print("6. Save Data")
    print("7. Load Data")
    print("8. Exit")

    print("=" * 70)


# ============================================================
# MAIN APPLICATION
# ============================================================

def main():
    show_header()

    print("Application started successfully.")
    print("Initializing student management system...")

    while True:

        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            show_all_students()

        elif choice == "2":
            search_student()

        elif choice == "3":
            add_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            show_statistics()

        elif choice == "6":
            save_students()

        elif choice == "7":
            load_students()

        elif choice == "8":
            print("\nThank you for using the application.")
            print("Application shutting down...")
            break

        else:
            print("\nInvalid choice.")
            print("Please select an option from 1 to 8.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
