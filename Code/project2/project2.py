# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 
# Instructor: Professor 
# Description: Project 2
# Errors: 1) If string is not exact, results will not show. 
# Example: the string in option 3 "Deccan Chargers" will work while "Deccan  Chargers" will not work because of extra space.
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="icl_database"
)

# create database cursor
cursor = db.cursor()

def request_info():
    keepGoing = True

    print("-------------------------------------")
    print("Welcome to the Indian Cricket League database!")
    print("-------------------------------------")
    print("Select an option:")
    print("1) One option to insert data that interacts with at least one table")
    print("2) One option to delete data that interacts with at least one table")
    print("3) One option to output data that interacts with at least one table")
    print("4) One option to insert data that interacts with at least two tables")
    print("5) One option to delete data that interacts with at least two tables")
    print("6) One option to output data that interacts with at least two tables")
    print("7) One option to output data that interacts with three or more tables")
    print("8) Exit the program. (One option should be to exit the program)")

    while (keepGoing == True):
        print("Welcome to the Indian Cricket League! a Note that")
        text = input("Choose any options from 1-8: ")
        choice  = text.strip()
        
        match choice:
            case "1":
                print("You can become a web developer1111.")
            case "2":
                print("You can become a web developer222.")
            case "3":
                team_name = input("Enter team name: ")
                query = ("""select * from teamwise_home_and_away where team = (%s) """)
                val = (team_name,)

                cursor.execute(query,val)

                myResult = cursor.fetchall()
                for rowNum in range(len(myResult)):
                    print(myResult[rowNum])
                print("------------")

            case "4":
                print("You can become a web developer.")
            case "5":
                print("You can become a web developer.")
            case "6":
                print("You can become a web developer.")
            case "7":
                print("You can become a web developer.")
            case "8":
                print("You can become a web developer.")
            case _:
                print("That is not an option.")







def main():
    request_info()

main()
