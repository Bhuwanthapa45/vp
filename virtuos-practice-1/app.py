import sqlite3

def create_table():
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   age INTEGER,
                   salary REAL,
                   total_salary REAL,
                   category TEXT
                   )
                   """)
    conn.commit()
    conn.close()

def get_employee_input():
        name = input("Enter employee name: ")
        if len(name) > 30:
            print("Name should not exceed 30 characters.")
            return None
        
        age = int(input("Eneter employee age: "))
        if age < 18 or age > 65:
            print("Age should be between 18 and 65.")
            return None
        
        salary = float(input("Enter salary: "))
        if salary <= 0:
            print("Salary should be greater than 0 it can be 0.")
            return None
        
        return name, age, salary
    
def calculate_salary_details(salary):
        bonus = salary * 0.10
        total_salary = salary + bonus

        if total_salary > 50000:
            category = "senior"
        else: 
            category = "junior"

        return bonus, total_salary, category
    
def save_employee(data):
        name, age, salary, total_salary, category = data

        conn = sqlite3.connect("employee.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO employees(name, age, salary, total_salary, category)
                       VALUES (?, ?, ?, ?, ?)

                       """, data)
        
        conn.commit()
        conn.close()

def display_employees():
        conn = sqlite3.connect("employee.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()

        print("\n Emplyee Records")
        for row in rows:
            print(row)

        conn.close()

def main():
        create_table()

        employee = get_employee_input()
        if not employee:
            return 
        
        name, age, salary = employee
        bonus, total_salary, category = calculate_salary_details(salary)

        save_employee((name, age, salary, total_salary, category))
        display_employees()

if __name__ == "__main__":
        main()



