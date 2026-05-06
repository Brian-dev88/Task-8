#imports
import _sqlite3

#variables
DATABASE = "student.db"



#function




#main code
db = _sqlite3.connect(DATABASE)
cursor = db.cursor()
sql = "SELECT * FROM student;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close