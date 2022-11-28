# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 11/21/2022
# Instructor: Professor Helsing
# Description: Practice Problems 5
# Errors: 
# Access "world", "characters" database set-up
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="world"
)

# create database cursor
cursor = db.cursor()

# queries
query = ("""select * from city 
""")

cursor.execute(query)
# Print out all of the column names currently stored in your cursor, with a suitable message
numOfFields = len(cursor.description)
col_names = [i[0] for i in cursor.description]
print("Column names: ", col_names)
print("------------")

# Fetch all of the results from the query and store them in a new variable
myresult = cursor.fetchall()
# Print row count
print("Row count: ", len(myresult))
# Using a for loop, iterate through your results printing out each record on a new line
# for x in myresult:
#   print(x)

cursor.close()
db.close()
