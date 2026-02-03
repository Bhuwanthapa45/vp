# input_handler.py
from typing import Optional, Tuple

def get_student_input() -> Optional[Tuple[str, int, float]]:
    try:
        name = input("Student Name: ").strip()
        if not name or len(name) > 30:
            print("Invalid name")
            return None

        age = int(input("Age: "))
        if age < 5 or age > 25:
            print("Invalid age")
            return None

        marks = float(input("Marks: "))
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100")
            return None

        return name, age, marks

    except ValueError:
        print("Invalid input type")
        return None
