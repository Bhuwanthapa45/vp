# Import Flask framework utilities
from flask import Flask, render_template, request, redirect, url_for

# Import SQLite database module
import sqlite3

# Create Flask application instance
app = Flask(__name__)

# Database file name (SQLite database stored locally)
DB = "candidates.db"


# ---------------- DATABASE UTILITIES ----------------

def get_conn():
    """
    Creates and returns a database connection.
    This function centralizes DB access so it can be reused everywhere.
    """
    return sqlite3.connect(DB)


def create_table():
    """
    Creates the candidates table if it does not already exist.
    This runs once when the application starts.
    """
    conn = get_conn()                  # Open DB connection
    cursor = conn.cursor()             # Create cursor to execute SQL

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT,
            college_name TEXT,
            round1 FLOAT,
            round2 FLOAT,
            round3 FLOAT,
            technical FLOAT,
            total FLOAT,
            result TEXT
        )
    """)

    conn.commit()                      # Save table creation
    conn.close()                       # Close DB connection


# ---------------- BUSINESS LOGIC ----------------

def evaluate_candidate(r1, r2, r3, tech):
    """
    Calculates total marks and determines result.
    Business rules are isolated here.
    """
    total = r1 + r2 + r3 + tech
    result = "Selected" if total >= 35 else "Rejected"
    return total, result


# ---------------- ROUTES ----------------

@app.route("/", methods=["GET"])
def index():
    """
    Home page route.
    Fetches candidates sorted by rank using DENSE_RANK.
    """
    conn = get_conn()
    cursor = conn.cursor()

    # SQL window function calculates rank dynamically
    cursor.execute("""
        SELECT
            id,
            student_name,
            college_name,
            total,
            result,
            DENSE_RANK() OVER (ORDER BY total DESC) AS rank
        FROM candidates
        ORDER BY rank
    """)

    candidates = cursor.fetchall()     # Fetch all rows
    conn.close()

    # Send data to HTML template
    return render_template("index.html", candidates=candidates)

@app.route("/delete/<int:id>")
def delete_candidate(id):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM candidates WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect(url_for("index"))





@app.route("/submit", methods=["POST"])
def submit():
    """
    Handles form submission from frontend.
    Reads user input, validates, stores in DB.
    """

    # Read and clean input values from HTML form
    name = request.form["name"].strip()
    college = request.form["college"].strip()

    # Convert numeric inputs to float
    r1 = float(request.form["r1"])
    r2 = float(request.form["r2"])
    r3 = float(request.form["r3"])
    tech = float(request.form["tech"])

    # Apply business rules
    total, result = evaluate_candidate(r1, r2, r3, tech)

    # Insert record into database
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO candidates
        (student_name, college_name, round1, round2, round3, technical, total, result)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, college, r1, r2, r3, tech, total, result))

    conn.commit()
    conn.close()

    # Redirect to homepage (Post-Redirect-Get pattern)
    return redirect(url_for("index"))

@app.route("/filter", methods=["GET"])
def filter_candidates():
    """Filter candidates by total marks"""
    min_marks = request.args.get("min", 0)
    max_marks = request.args.get("max", 100)

    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            student_name,
            college_name,
            total,
            result,
            DENSE_RANK() OVER (ORDER BY total DESC) AS rank
        FROM candidates
        WHERE total BETWEEN ? AND ?
        ORDER BY rank
    """, (min_marks, max_marks))

    candidates = cursor.fetchall()
    conn.close()

    return render_template("index.html", candidates=candidates)

@app.route("/edit/<int:id>")
def edit_candidate(id):
    conn = get_conn()
    cursor = conn.cursor()
    
    # Fetch all details for this specific student to pre-fill the form
    cursor.execute("SELECT * FROM candidates WHERE id = ?", (id,))
    student = cursor.fetchone()
    conn.close()

    if student:
        return render_template("edit.html", s=student)
    return redirect(url_for("index"))

@app.route("/update/<int:id>", methods=["POST"])
def update_candidate(id):
    # Get updated values from the form
    name = request.form["name"].strip()
    college = request.form["college"].strip()
    r1 = float(request.form["r1"])
    r2 = float(request.form["r2"])
    r3 = float(request.form["r3"])
    tech = float(request.form["tech"])

    # Recalculate total and result
    total, result = evaluate_candidate(r1, r2, r3, tech)

    conn = get_conn()
    cursor = conn.cursor()
    
    # Update the existing record
    cursor.execute("""
        UPDATE candidates 
        SET student_name=?, college_name=?, round1=?, round2=?, round3=?, technical=?, total=?, result=?
        WHERE id=?
    """, (name, college, r1, r2, r3, tech, total, result, id))
    
    conn.commit()
    conn.close()
    
    return redirect(url_for("index"))







# ---------------- APPLICATION ENTRY POINT ----------------

if __name__ == "__main__":
    """
    Ensures code runs only when file is executed directly.
    """
    create_table()         # Ensure table exists
    app.run(debug=True, port=5001)    # Start Flask development server
