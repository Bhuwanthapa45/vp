# service.py
from typing import Tuple

def calculate_salary(salary: float) -> Tuple[float, str]:
    bonus = salary * 0.10
    total_salary = salary + bonus
    category = "Senior" if total_salary >= 50000 else "Junior"
    return total_salary, category

