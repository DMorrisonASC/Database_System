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
# Execute the query that would provide all of the attributes for all cities where the country code is AFG
query = ("""
select * 
from city 
where countrycode = "AFG"
""")

query2 = ("""
select * 
from city 
where countrycode = "GGG"
""")

query3 = ("""
select avg(population), CountryCode 
from city 
group by CountryCode;
""")

query4 = ("""
select avg(population) as avgPop, CountryCode 
from city 
group by CountryCode;
""")

cursor.execute(query)
# Fetch all of the results from the query and store them in a new variable
myResult = cursor.fetchall()

for rowNum in range(len(myResult)):
    print(myResult[rowNum][1])
print("------------")

# Fetch one record from the query and store it in a new variable using the fetchone() function from your cursor
cursor.execute(query)
row = cursor.fetchone()
while row is not None:
  print(row[1])
  row = cursor.fetchone()
print("------------")
# Execute the query that would provide all 
# of the attributes for all cities where the country code is GGG
cursor.execute(query2)
result_GGG = cursor.fetchall()
print("Row count: ", len(result_GGG))
for rowNum in range(len(result_GGG)):
    print(result_GGG[rowNum][1])
print("------------")
cursor.close()
# -------
cursor = db.cursor(dictionary=True)
cursor.execute(query)

results_dict = cursor.fetchall()
for item in results_dict:
    print(item['Name'])
print("------------")
# Execute the query that would provide the average population and 
# country code for each city, grouped 
# by country code
cursor.execute(query3)
cursor.fetchall()
numOfFields = len(cursor.description)
col_names = [i[0] for i in cursor.description]
print("Column names: ", col_names)
print("------------")
# Execute the same query but rename the average population attribute to “avgPop”
cursor.execute(query4)
avg_city_records = cursor.fetchall()
numOfFields = len(cursor.description)
col_names = [i[0] for i in cursor.description]
print("Column names: ", col_names)
print("------------")
# Using a for loop, iterate through your results 
# printing out the average population, with two 
# decimal points of precision, and country code on a new line;
for eachPop in avg_city_records:
    txt = "Average population is {pop:.2f} in country code: {countryCode}"
    print(txt.format(pop = eachPop["avgPop"], countryCode = eachPop["CountryCode"]))



# Empty cursor & close connections
cursor.fetchall()
cursor.close()
db.close()