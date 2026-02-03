# main.py
from db import create_table
from input_handler import get_employee_input
from service import calculate_salary
from repository import *

def main():
    create_table()

    while True:
        print("""
1. Add Employee
2. View Employees
3. Update Salary
4. Delete Employee
5. Filter by Min Salary
6. Count by Category
7. Employees with Department
0. Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            data = get_employee_input()
            if not data:
                continue

            name, age, salary, dept_id = data
            total_salary, category = calculate_salary(salary)
            add_employee(name, age, salary, total_salary, category, dept_id)

        elif choice == "2":
            for emp in fetch_all_employees():
                print(emp)

        elif choice == "3":
            update_salary(int(input("Emp ID: ")), float(input("New Salary: ")))

        elif choice == "4":
            delete_employee(int(input("Emp ID: ")))

        elif choice == "5":
            for emp in employees_with_min_salary(float(input("Min Salary: "))):
                print(emp)

        elif choice == "6":
            for row in count_by_category():
                print(row)

        elif choice == "7":
            for row in employees_with_department():
                print(row)

        elif choice == "0":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
