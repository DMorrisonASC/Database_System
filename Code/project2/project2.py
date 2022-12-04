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
                player_name = input("Enter player name: ")
                # Check if records exist already
                check_records_query=""" SELECT player_Name FROM players WHERE EXISTS(SELECT * FROM players WHERE player_Name = "{}") """
                cursor.execute(check_records_query.format(player_name))

                rows=cursor.fetchall()

                if (len(rows) == 0):
                    Batting_hand = input('Enter Batting_hand("Right_Hand" or "Left_Hand"): ')
                    Bowling_Skill = input('Enter Bowling_Skill("Right_Arm" or "Left_Arm"): ')
                    Country = input("Enter country: ")
                    query1 = ("""
                    Insert into players (player_Name, Batting_hand, Bowling_Skill, Country)
                    VALUES (%s, %s, %s, %s)
                    """)

                    val = (player_name, Batting_hand, Bowling_Skill, Country)
                    
                    cursor.execute(query1, val)
                    db.commit()
            
                else:
                    print("record already exists!")


            case "2":
                player_name = input("Enter player name: ")
                # Check if records exist already
                check_records_query2 = """ SELECT player_Name FROM players WHERE EXISTS(SELECT * FROM players WHERE player_Name = "{}") """
                cursor.execute(check_records_query2.format(player_name))

                rows=cursor.fetchall()

                if (len(rows) != 0):
                    query2 = (""" Delete from players
                    where player_Name = %s 
                     """)

                    val = (player_name,)
                    
                    cursor.execute(query2, val)
                    db.commit()
            
                else:
                    print("record does not exists!")

            case "3":
                team_name = input("Enter team name: ")
                query3 = ("""select * from teamwise_home_and_away where team = (%s) """)
                val = (team_name,)

                cursor.execute(query3,val)

                myResult = cursor.fetchall()
                for rowNum in range(len(myResult)):
                    print(myResult[rowNum])
                print("------------")

            case "4":
                print("You can become a web developer.")
            case "5":
                print("You can become a web developer.")
            case "6":
                player_name = input("Enter player name: ")
                query6 = ("""select * from players join most_runs_average_strikerate on players.player_Name = batsman where player_Name = (%s) """)
                val = (player_name,)

                cursor.execute(query6,val)

                myResult = cursor.fetchall()
                for rowNum in range(len(myResult)):
                    print(myResult[rowNum])
                print("------------")
            case "7":
                print("You can become a web developer.")
            case "8":
                print('See all matches where a player was earned "player of the match"!')
                player_name = input("Enter player name: ")
                # query_playerInfo = ("""select * from players join most_runs_average_strikerate""")
                query_matches_POG = ("""
                with player_stats_info(Player_Name, DOB, Batting_Hand, Bowling_Skill, Country, batsman, total_runs_ever, `out`, numberofballs, average, strikerate) as (select * from players join most_runs_average_strikerate on players.player_Name = batsman)
                select * from matches join 
                player_stats_info
                on matches.player_of_match = player_stats_info.player_Name 
                where player_of_match = (%s) 
                """)
                
                val = (player_name,)

                cursor.execute(query_matches_POG,val)

                myResult = cursor.fetchall()
                for rowNum in range(len(myResult)):
                    print(myResult[rowNum])
                print("------------")
            case _:
                print("That is not an option.")







def main():
    request_info()

main()
