import sqlite3
import os


def create_database():
    if os.path.exists("students.db"):
        os.remove("students.db")

    conn = sqlite3.connect("students.db") # Create a new database or connect to an existing one
    cursor = conn.cursor() # Create a cursor object to execute SQL commands
    return conn, cursor


def create_tables(cursor):

    cursor.execute('''
        CREATE TABLE Students
        (
            id INTEGER PRIMARY KEY,
            name VARCHAR NOT NULL,
            age INTEGER,
            email VARCHAR UNIQUE,
            city VARCHAR
        )
    ''')

    cursor.execute('''
            CREATE TABLE Courses
            (
                id INTEGER PRIMARY KEY,
                course_name VARCHAR NOT NULL,
                instructor TEXT,
                credits INTEGER
            )
        ''')

def insert_sample_data(cursor):

    students = [
        (1, 'Alice Jonson', 20, 'alice@gmail.com', 'New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle'),
    ]

    cursor.executemany(" INSERT INTO Students VALUES (?, ?, ?, ?, ?)", students)

    courses = [
        (1, 'Mathematics', 'Dr. John Doe', 4),
        (2, 'Physics', 'Dr. Jane Smith', 3),
        (3, 'Chemistry', 'Dr. Emily Johnson', 4),
        (4, 'Biology', 'Dr. Michael Brown', 3),
        (5, 'Computer Science', 'Dr. Sarah Davis', 4),
    ]

    cursor.executemany(" INSERT INTO Courses VALUES (?, ?, ?, ?)", courses)

    print("Sample data inserted successfully.")

def basic_sql_operations(cursor):

    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()

    for row in students:
        print(row[1], row[2], row[3], row[4])

def main():

    print("SQL with Python")

    conn, cursor = create_database() # Create or connect to the database

    try:

        create_tables(cursor) # Create the necessary tables
        insert_sample_data(cursor) # Insert sample data into the tables
        basic_sql_operations(cursor) # Perform basic SQL operations


        conn.commit() # Commit the changes to the database

    except sqlite3.Error as e:

        print("An error occurred:", e)

    finally:

        cursor.close()
        conn.close()





if __name__ == "__main__":
    main()
