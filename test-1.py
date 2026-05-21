import sqlite3

db = sqlite3.connect("student (1).db")
cursor = db.cursor()

print('1. Search by student name')
print('2. Search by student ID')
print('3. Show all students and grade score')

choice = input("Enter Option (1/2/3): ")

while True:
    try:
        if choice == "1":
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
                print("No further records found.")
            break

        elif choice == "2":
            value = int(input('Enter student ID: '))
            sql = "SELECT grade.student_id, student.student_name, grade.grade_score FROM grade, student WHERE grade.student_id = student.student_id AND grade.student_id = ?"
            cursor.execute(sql, (value,))

            results = cursor.fetchall()
            if results:
                print(f"{'student_id':<15}{'student_name':<25}{'grade_score':<25}")
                print("-" * 50)

            for row in results:
                print(f"{row[0]:<15}{row[1]:<25}{row[2]:<25}")
            else:
                print("No further records found.")
            break

        elif choice == "3":
            sql = "SELECT grade.student_id, student.student_name, grade.grade_score FROM grade, student WHERE grade.student_id = student.student_id "
            cursor.execute(sql)
            results = cursor.fetchall()

            if results:
                print(f"{'student_id':<15}{'student_name':<25}{'grade_score':<25}")
                print("-" * 50)

            for row in results:
                print(f"{row[0]:<15}{row[1]:<25}{row[2]:<25}")
            else:
                print("No further records found.")
            break

    except ValueError:
        print("Invalid input. Please try again.")