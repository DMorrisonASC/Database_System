# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 
# Instructor: Professor 
# Description: Project 2
# Errors: 1) If string is not exact, results will not show. 
# Example: the string in option 3 "Deccan Chargers" will work while "Deccan  Chargers" will not work because of extra space.
# 2) Users can in
import mysql.connector
from decimal import Decimal

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="icl_database"
)

# create database cursor
cursor = db.cursor()


def main():
    print("main")
main()
