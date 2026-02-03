from db import create_table
from input_handler import get_employee_input
from service import calculate_salary_details
from repository import save_employee, fetch_all_employees

def main():
    create_table()

    employee = get_employee_input()
    if employee is None:
        return
    name, age, salary = employee
    total_salary, category = calculate_salary_details(salary)
    save_employee(name, age, salary, total_salary, category)

    print("\n Employee records:")
    records = fetch_all_employees()

    for record in records:
        print(record)
    
if __name__ == "__main__":
    main()


    
