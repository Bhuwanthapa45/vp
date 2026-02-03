# input_handler.py
from typing import Optional, Tuple

def get_employee_input() -> Optional[Tuple[str, int, float, int]]:
    try:
        name = input("Name: ").strip()
        if not name or len(name) > 30:
            print("Invalid name")
            return None

        age = int(input("Age: "))
        if age < 18 or age > 65:
            print("Invalid age")
            return None

        salary = float(input("Salary: "))
        if salary <= 0:
            print("Invalid salary")
            return None

        dept_id = int(input("Department ID: "))
        return name, age, salary, dept_id

    except ValueError:
        print("Invalid input type")
        return None

