import sqlite3

DB_NAME = "employee.db"

def get_db_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        salary REAL NOT NULL,
        total_salary REAL NOT NULL,
        category TEXT NOT NULL,
        department_id INTEGER,
        FOREIGN KEY (department_id) REFERENCES departments(id)
    )
    """)

    conn.commit()
    conn.close()

    