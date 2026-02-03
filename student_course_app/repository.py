# repository.py
from db import get_db_connection

# CREATE
def add_student(name, age, marks, grade):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students (name, age, marks, grade)
    VALUES (?, ?, ?, ?)
    """, (name, age, marks, grade))

    conn.commit()
    conn.close()

# READ
def fetch_all_students():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    conn.close()
    return rows

# UPDATE
def update_student_marks(student_id, new_marks, new_grade):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE students
    SET marks = ?, grade = ?
    WHERE id = ?
    """, (new_marks, new_grade, student_id))

    conn.commit()
    conn.close()

# DELETE
def delete_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()

# WHERE + ORDER BY
def students_with_min_marks(min_marks):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM students
    WHERE marks >= ?
    ORDER BY marks DESC
    """, (min_marks,))

    rows = cursor.fetchall()
    conn.close()
    return rows

# GROUP BY
def count_students_by_grade():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT grade, COUNT(*)
    FROM students
    GROUP BY grade
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows

# JOIN
def students_with_courses():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT s.name, c.course_name
    FROM students s
    JOIN enrollments e ON s.id = e.student_id
    JOIN courses c ON e.course_id = c.id
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows

