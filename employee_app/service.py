from typing import Tuple

def calculate_salary_details(salary: float) -> Tuple[float, str]:
    bonus = salary * 0.10
    total_salary = salary + bonus

    if total_salary > 50000:
        category = "semnior"
    else:
        category = "junior"

    return total_salary, category
