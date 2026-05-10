import sqlite3

db = sqlite3.connect("student.db")
cursor = db.cursor()

student_name = input("Enter the name of the student: ")

sql = "SELECT * FROM grade WHERE student_name = ?"
cursor.execute(sql, (student_name,))

results = cursor.fetchall()

if results:
    print(results)
else:
    print("No records found.")

db.close()
