import _sqlite3

db = _sqlite3.connect("student.db")
cursor = db.cursor()
sql = "SELECT * FROM student;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close