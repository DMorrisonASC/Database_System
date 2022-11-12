# Access "world", "characters" database set-up
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="world"
)

query = ("""
Select * 
from city

""")

cursor = db.cursor()

data=cursor.execute(query)

myresult = cursor.fetchall()
# for x in myresult:
#   print(x)

#for item in range(6):
  # print(myresult[item])

# for col in myresult.columns:
#   print(col)

num_fields = len(cursor.description)
field_names = [i[0] for i in cursor.description]
print(field_names)

