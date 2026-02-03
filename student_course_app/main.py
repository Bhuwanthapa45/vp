# main.py
from db import create_tables
from input_handler import get_student_input
from service import calculate_grade
from repository import *

def main():
    create_tables()

    while True:
        print("""
1. Add Student
2. View Students
3. Update Student Marks
4. Delete Student
5. Filter by Min Marks
6. Count by Grade
7. Students with Courses
0. Exit
""")

        choice = input("Choose option: ")

        if choice == "1":
            data = get_student_input()
            if not data:
                continue

            name, age, marks = data
            grade = calculate_grade(marks)
            add_student(name, age, marks, grade)

        elif choice == "2":
            for student in fetch_all_students():
                print(student)

        elif choice == "3":
            sid = int(input("Student ID: "))
            new_marks = float(input("New Marks: "))
            new_grade = calculate_grade(new_marks)
            update_student_marks(sid, new_marks, new_grade)

        elif choice == "4":
            delete_student(int(input("Student ID: ")))

        elif choice == "5":
            for s in students_with_min_marks(float(input("Min Marks: "))):
                print(s)

        elif choice == "6":
            for row in count_students_by_grade():
                print(row)

        elif choice == "7":
            for row in students_with_courses():
                print(row)

        elif choice == "0":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
