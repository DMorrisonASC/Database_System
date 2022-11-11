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
# for column in data.
# print(data.description)
# for x in myresult:
#   print(x)
for item in range(6):
  print(myresult[item])
