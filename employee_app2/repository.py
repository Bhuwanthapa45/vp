# repository.py
from db import get_db_connection

# CREATE
def add_employee(name, age, salary, total_salary, category, dept_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO employees
    (name, age, salary, total_salary, category, department_id)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, age, salary, total_salary, category, dept_id))

    conn.commit()
    conn.close()

# READ
def fetch_all_employees():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()
    return rows

# UPDATE
def update_salary(emp_id, new_salary):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE employees SET salary = ?
    WHERE id = ?
    """, (new_salary, emp_id))

    conn.commit()
    conn.close()

# DELETE
def delete_employee(emp_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
    conn.commit()
    conn.close()

# WHERE + ORDER BY
def employees_with_min_salary(min_salary):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM employees
    WHERE salary >= ?
    ORDER BY salary DESC
    """, (min_salary,))

    rows = cursor.fetchall()
    conn.close()
    return rows

# GROUP BY
def count_by_category():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT category, COUNT(*)
    FROM employees
    GROUP BY category
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows

# JOIN
def employees_with_department():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT e.name, e.salary, d.name
    FROM employees e
    JOIN departments d
    ON e.department_id = d.id
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows

