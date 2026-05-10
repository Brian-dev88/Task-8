import sqlite3

db = sqlite3.connect("student.db")
cursor = db.cursor()

student_name = input("Enter the name of the student: ")

sql = "SELECT * FROM student WHERE student_name = ?"
cursor.execute(sql, (student_name,))

results = cursor.fetchall()

if results:
    for row in results:
        print(row)
else:
    print("No records found.")

db.close()
