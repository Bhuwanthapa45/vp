from typing import Optional, Tuple

def get_employee_input() -> Optional[Tuple[str, int, float]]:
    try:
        name = input("Enter employee name: ").strip()
        if not name or len(name) < 2:
            print("Name should be at least 2 characters long.")
            return None
        
        age = int(input("Enter employee age: "))
        if age < 18 or age > 65:
            print("Invalid age")
            return None
        salary = float(input("Enter employee salary: "))
        if salary <= 0:
            print("Salary must be greater than 0.")
            return None
        return name, age, salary
    except ValueError:
        print("Invalid input. Please enter correct data types.")
        return None
    