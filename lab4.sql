import sqlite3

# Connect to database
conn = sqlite3.connect("college.db")

# Create cursor
cursor = conn.cursor()

# Create Students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT
)
""")

# Create Courses table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    duration TEXT
)
""")

# Create Enrollments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    enrollment_date TEXT,
    
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
)
""")

# Insert data
cursor.execute("""
INSERT OR IGNORE INTO Students VALUES
(1, 'Anushka', 'anushka@gmail.com', '9876543210')
""")

cursor.execute("""
INSERT OR IGNORE INTO Students VALUES
(2, 'Rahul', 'rahul@gmail.com', '9876543211')
""")

cursor.execute("""
INSERT OR IGNORE INTO Courses VALUES
(101, 'Python Programming', '3 Months')
""")

cursor.execute("""
INSERT OR IGNORE INTO Courses VALUES
(102, 'Database Management', '2 Months')
""")

cursor.execute("""
INSERT OR IGNORE INTO Enrollments VALUES
(1, 1, 101, '2026-08-31')
""")

cursor.execute("""
INSERT OR IGNORE INTO Enrollments VALUES
(2, 2, 102, '2026-08-31')
""")

conn.commit()

# Display Students table
print("\nSTUDENTS TABLE")
cursor.execute("SELECT * FROM Students")
for row in cursor.fetchall():
    print(row)

# Display Courses table
print("\nCOURSES TABLE")
cursor.execute("SELECT * FROM Courses")
for row in cursor.fetchall():
    print(row)

# Display Enrollments table
print("\nENROLLMENTS TABLE")
cursor.execute("SELECT * FROM Enrollments")
for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()
