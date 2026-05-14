import sqlite3

db = sqlite3.connect("student (1).db")
cursor = db.cursor()

grade = input("Enter the name of the student: ")

sql = "SELECT * FROM student WHERE student_name = ?"
cursor.execute(sql, (grade,))

results = cursor.fetchall()

if results:
    print(f"{'student_id':<15}{'student_name':<25}")
    print("-" * 40)

    for row in results:
        print(f"{row[0]:<15}{row[1]:<25}")
else:
    print("No records found.")

