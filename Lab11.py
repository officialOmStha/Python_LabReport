# Lab 11:

import sqlite3


class StudentDB:

    def __init__(self, db_name="college.db"):
        self.db_name = db_name

        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()

            # Create table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    roll INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    marks REAL NOT NULL,
                    grade TEXT NOT NULL
                )
            """)

            self.conn.commit()
            print("Database connected and table ready.")

        except sqlite3.DatabaseError as e:
            print("Database error during initialization:", e)

    def insert_student(self, roll, name, marks, grade):
        try:
            self.cursor.execute(
                "INSERT INTO students (roll, name, marks, grade) VALUES (?, ?, ?, ?)",
                (roll, name, marks, grade)
            )
            self.conn.commit()
            print("Student inserted successfully.")

        except sqlite3.IntegrityError:
            print("Error: Roll number already exists.")

        except sqlite3.DatabaseError as e:
            print("Database error:", e)

    def view_all_students(self):
        try:
            self.cursor.execute("SELECT * FROM students")
            rows = self.cursor.fetchall()

            if not rows:
                print("No students found.")
            else:
                print("\nAll Students:")
                for row in rows:
                    print(row)

        except sqlite3.DatabaseError as e:
            print("Database error:", e)

    def update_marks(self, roll, new_marks):
        try:
            self.cursor.execute(
                "UPDATE students SET marks = ? WHERE roll = ?",
                (new_marks, roll)
            )
            self.conn.commit()

            if self.cursor.rowcount == 0:
                print("Student not found.")
            else:
                print("Marks updated successfully.")

        except sqlite3.DatabaseError as e:
            print("Database error:", e)

    def delete_student(self, roll):
        try:
            self.cursor.execute("DELETE FROM students WHERE roll = ?", (roll,))
            self.conn.commit()

            if self.cursor.rowcount == 0:
                print("Student not found.")
            else:
                print("Student deleted successfully.")

        except sqlite3.DatabaseError as e:
            print("Database error:", e)

    def close(self):
        self.conn.close()
        print("Database connection closed.")


# ---------------- MAIN PROGRAM ----------------

db = StudentDB()

while True:
    print("\n===== STUDENT DATABASE MENU =====")
    print("1. Insert Student")
    print("2. View All Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = int(input("Roll: "))
        name = input("Name: ")
        marks = float(input("Marks: "))
        grade = input("Grade: ")
        db.insert_student(roll, name, marks, grade)

    elif choice == "2":
        db.view_all_students()

    elif choice == "3":
        roll = int(input("Enter roll: "))
        new_marks = float(input("Enter new marks: "))
        db.update_marks(roll, new_marks)

    elif choice == "4":
        roll = int(input("Enter roll: "))
        db.delete_student(roll)

    elif choice == "5":
        db.close()
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")