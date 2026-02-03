import sqlite3

DB_NAME = "employee.db"

def get_db_connection():
    return sqlite3.connect(DB_NAME)

def create_table() -> None:
    """
    Creates the employees table if it does not already exist.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            salary REAL NOT NULL,
            total_salary REAL NOT NULL,
            category TEXT NOT NULL
        )
        """)

        conn.commit()

    except sqlite3.DatabaseError as e:
        print(f"[DB ERROR] Failed to create table: {e}")

    finally:
        conn.close()
