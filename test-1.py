import sqlite3

db = sqlite3.connect("student (1).db")
cursor = db.cursor()

grade = input("Enter the name of the student: ")

sql = "SELECT * FROM student, grade WHERE student_name = ? AND student.student_id = grade.student_id"
cursor.execute(sql, (grade,))

results = cursor.fetchall()

if results:
    print(f"{'student_id':<15}{'student_name':<25}{'grade_score':<25}")
    print("-" * 50)

    for row in results:
        print(f"{row[0]:<15}{row[1]:<25}{row[5]:<25}")
else:
    print("No records found.")