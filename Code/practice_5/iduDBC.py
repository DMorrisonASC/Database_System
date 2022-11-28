
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
  database="characters"
)

# create database cursor
cursor = db.cursor()

# queries
query = ("""
select * 
from npcs
""")

query2 = ("""
Insert into npcs (id, `first name`, `last name`, race, age, occupation, alignment)
values ("11", "Breia", "De marlo", "gnome", "120", "bard", "good");
""")

query3 = ("""
delete from npcs where id = "11"
""")

query4 = ("""
Insert into npcs (id, `first name`, `last name`, race, age, occupation, alignment)
values ("{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}");
""")

query5 = ("""
delete from npcs where id = "{}"
""")
# Execute a query that would select all attributes from the npcs table
# Using a for loop, iterate through your results 
# printing out each record on a new line.
cursor.execute(query)
records = cursor.fetchall()

for each_record in records:
    print(each_record)
print("---------------1")

# Execute insert query.
# cursor.execute(query2)
# db.commit()
# print("Row(s) affected: ", cursor.rowcount)

# # Print results.
# cursor.execute(query)
# records2 = cursor.fetchall()

# for each_record in records2:
#     print(each_record)
# print("---------------2")
# Execute a query that would delete npcs from that table if their id is 11
cursor.execute(query3)
db.commit()
print("Row(s) affected: ", cursor.rowcount)
# Print results.
cursor.execute(query)
records2 = cursor.fetchall()

for each_record in records2:
    print(each_record)
print("---------------3")
# Create a variable that stores insert portion of the previous query and use 
# format specifiers asplaceholders for the values
insert_query4 = ["11", "Breia", "De marlo", "gnome", "120", "bard", "good"]
cursor.execute(query4.format(insert_query4[0], insert_query4[1], insert_query4[2], insert_query4[3], insert_query4[4], insert_query4[5], insert_query4[6]));
db.commit()
print("Row(s) affected: ", cursor.rowcount)

# Print results.
cursor.execute(query)
records4 = cursor.fetchall()

for each_record in records4:
    print(each_record)
print("---------------4")
# Execute a query that would delete npcs from that table if their id is 11 using format specifier
cursor.execute(query5.format("11"))
db.commit()
print("Row(s) affected: ", cursor.rowcount)
# Print results.
cursor.execute(query)
records5 = cursor.fetchall()

for each_record in records5:
    print(each_record)
print("---------------5")

# Close connections
cursor.fetchall()
cursor.close()
db.close()

# What is cursor rowcount? 
# do you need to store cursor info in variable?
# what does fetchall do when not selecting all?
# 