from db import get_db_connection

def save_employee(name, age, salary, total_salary, category):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO employees (name, age, salary, total_salary, category)
                   VALUES(?, ?, ?, ?, ?)
                   """, (name, age, salary, total_salary, category)
                   )
    conn.commit()
    conn.close()

def fetch_all_employees():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    records = cursor.fetchall()

    conn.close()
    return records

def update_employee_salary(employee_id, new_salary):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE employees
    SET salary = ?
    WHERE id = ?
    """, (new_salary, employee_id))
    conn.commit()
    conn.close()

def delete_employee(employee_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM employees WHERE id = ?
                   
    """, (employee_id))

    conn.commit()
    conn.close()

def fetch_employees_with_min_salary(min_salary: float):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM employees
    WHERE salary >= ?
    ORDER BY salary DESC
    """, (min_salary,))

    records = cursor.fetchall()
    conn.close()
    return records

def count_employees_by_category():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT category, COUNT(*)
    FROM employees
    GROUP BY category
    """)

    result = cursor.fetchall()
    conn.close()
    return result





