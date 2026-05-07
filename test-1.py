#imports
import sqlite3

db = sqlite3.connect ("student.db")
cursor = db.cursor()
sql = "SELECT * FROM grade"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close
