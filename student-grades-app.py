import sqlite3

db = sqlite3.connect("student (1).db")
cursor = db.cursor()

# asking questions in a loop
while True:
    try:
        #options to choose from
        print('1. Search by student name')
        print('2. Search by student ID')
        print('3. Show all students that got A- or above')
        print('4. Show all students and grade score')
        print('5. Exit the app')

        # User input options 1,2,3,4,5
        choice = input("Enter Option (1/2/3/4/5): ")

        #option 1 asking for student name then printing out there grade
        if choice == "1":
            grade = input("Enter the name of the student: ")
            sql = "SELECT * FROM student, grade WHERE student_name = ? AND student.student_id = grade.student_id"
            cursor.execute(sql, (grade,))

            # Prints a table lsiting the students id name and score
            results = cursor.fetchall()
            if results:
                print(f"{'student_id':<15}{'student_name':<25}{'grade_score':<25}")
                print("-" * 50)

            # selecting for SQl 
            for row in results:
                print(f"{row[0]:<15}{row[1]:<25}{row[5]:<25}")
            else:
                print("No further records found.\n")
                
            
        # Asks user to enter via student id then prints out there student id student name and the grade they got
        elif choice == "2":
            value = int(input('Enter student ID: '))
            sql = "SELECT grade.student_id, student.student_name, grade.grade_score FROM grade, student WHERE grade.student_id = student.student_id AND grade.student_id = ?"
            cursor.execute(sql, (value,))
            
            # Prints a table that includes student id, name and then there score
            results = cursor.fetchall()
            if results:
                print(f"{'student_id':<15}{'student_name':<25}{'grade_score':<25}")
                print("-" * 50)

            # selecting for SQl 
            for row in results:
                print(f"{row[0]:<15}{row[1]:<25}{row[2]:<25}")
            else:
                print("No further records found.\n")

        # Shows all students that got A- or above
        elif choice =="3":
            sql = 'SELECT grade.*, student.student_name FROM grade, student WHERE grade.grade_score IN ("A-", "A", "A+") AND grade.student_id = student.student_id;'
            cursor.execute(sql)
            results = cursor.fetchall()

            # Pinting out all students that got A-,A,A+ lising then form studenty Id then name and lastly there score
            if results:
                print(f"{'student_id':<15}{'student_name':<25}{'grade_score':<25}")
                print("-" * 50)
            
            # selecting for SQl 
            for row in results:
                print(f"{row[1]:<15}{row[4]:<25}{row[3]:<25}")
            else:
                print("No further records found.\n")

        # Shows everyones score 
        elif choice == "4":
            sql = "SELECT grade.student_id, student.student_name, grade.grade_score FROM grade, student WHERE grade.student_id = student.student_id "
            cursor.execute(sql)
            results = cursor.fetchall()

            # printing them in order of student ID name then score
            if results:
                print(f"{'student_id':<15}{'student_name':<25}{'grade_score':<25}")
                print("-" * 50)

            # selecting for SQl 
            for row in results:
                print(f"{row[0]:<15}{row[1]:<25}{row[2]:<25}")
            else:
                print("No further records found.\n")
        
        # Gives the user the option to exit the code
        elif choice == "5":
            break

        else:
            print("Enter a number between 1 and 5.")


    except ValueError:
        print("Invalid input. Please try again.")
    
# Short remark saying thank you
print("Thanks for using!")