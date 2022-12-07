# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 
# Instructor: Professor 
# Description: Project 2
# Errors: 1) If string is not exact, results will not show. 
# Example: the string in option 3 "Deccan Chargers" will work while "Deccan  Chargers" will not work because of extra space.
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
                    print("------------")
            
                else:
                    print("record already exists!")
                    print("------------")


            case "2":
                player_name = input("Enter player name: ")
                # Check if records exist already
                check_records_query2 = (""" SELECT player_Name FROM players WHERE EXISTS(SELECT * FROM players WHERE player_Name = "{}") """)
                cursor.execute(check_records_query2.format(player_name))

                rows=cursor.fetchall()

                if (len(rows) != 0):
                    query2 = (""" Delete from players
                    where player_Name = %s 
                     """)

                    val = (player_name,)
                    
                    cursor.execute(query2, val)
                    db.commit()
                    print("------------")
                else:
                    print("record does not exists!")
                    print("------------")

            case "3":
                team_name = input("Enter team name: ")
                query3 = ("""select * from teamwise_home_and_away where team = (%s) """)
                val = (team_name,)

                cursor.execute(query3,val)

                myResult = cursor.fetchall()
                team_stats = """The {0} have :
home wins: {1}
away wins: {2}
home matches: {3}
away matches: {4}
home win percentage: {5}
away win percentage: {6}
"""
                print(team_stats.format(myResult[0][0], myResult[0][1], myResult[0][2], myResult[0][3], myResult[0][4], myResult[0][5], myResult[0][6]))

                # for rowNum in range(len(myResult)):
                #     print(myResult[0])
                print("------------")

            case "4":
                team_name = input("Enter team name to insert: ")
                check_records_query4 = (""" SELECT team FROM teams WHERE EXISTS(SELECT * FROM teams WHERE team = "{}") """)
                cursor.execute(check_records_query4.format(team_name))

                rows=cursor.fetchall()

                if (len(rows) == 0):
                    # create values
                    year_created = int(input("Enter year team was created: "))
                    home_wins = Decimal(input("Enter home wins: "))
                    away_wins = Decimal(input("Enter away wins: "))
                    home_matches = Decimal(input("Enter home matches played: "))
                    away_matches = Decimal(input("Enter away matches played: "))
                    home_win_percentage = home_wins / home_matches
                    away_win_percentage =  away_wins / away_matches
                    # Create queries
                    insert_team_query = """Insert into teams (team, year_created)
                    values (%s, %s)
                    """
                    insert_teamwise = ("""Insert into teamwise_home_and_away 
                    (team, home_wins, away_wins, home_matches, away_matches, home_win_percentage, away_win_percentage)
                    values (%s, %s, %s, %s, %s, %s, %s)
                    """)
                    values_team = (team_name, year_created)
                    values_teamwise = (team_name, home_wins, away_wins, home_matches, away_matches, home_win_percentage, away_win_percentage)
                    # Insert into db
                    cursor.execute(insert_team_query, values_team)
                    cursor.execute(insert_teamwise, values_teamwise)

                    db.commit()
                    print("------------")  

                else:
                    print("Records of the team already exists!")

            case "5":
                team_name = input("Enter team name to delete: ")
                # Check if records exist already
                check_records_query5 = (""" SELECT team FROM teams WHERE EXISTS(SELECT * FROM teams WHERE team = "{}") """)
                cursor.execute(check_records_query5.format(team_name))

                rows=cursor.fetchall()

                if (len(rows) != 0):
                    delete_team = (""" Delete from teams
                    where team = %s 
                     """)
                    delete_teamwise = (""" Delete from teamwise_home_and_away
                    where team = %s 
                     """)

                    val_delete = (team_name,)
                    
                    cursor.execute(delete_teamwise, val_delete)
                    cursor.execute(delete_team, val_delete)
                    db.commit()
                    print("------------")
                else:
                    print("record does not exists!")
                    print("------------")

                
            case "6":
                player_name = input("Enter player name: ")
                query6 = ("""select * from players join most_runs_average_strikerate on players.player_Name = batsman where player_Name = (%s) """)
                val = (player_name,)

                cursor.execute(query6,val)

                myResult = cursor.fetchall()

                stats_Info_player = """{0}'s stats:\
Total runs in career: {6}
Dismissaled/Outted : {7}
Number of balls hit: {8}
Average: {9}
Strike rate: {10} 
--Back ground Info--
DOB: {1}
Batting hand: {2}
Bowling skill: {3}
Country: {4}       
                """
                print(stats_Info_player.format(myResult[0][0], myResult[0][1], 
                myResult[0][2], myResult[0][3], myResult[0][4], myResult[0][5], 
                myResult[0][6], myResult[0][7], myResult[0][8], 
                myResult[0][9], myResult[0][10]
                ))
                
                print("------------")

            case "7":
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

                POG_player = 'Matches where "{0}" was player of the match:'

                print(POG_player.format(player_name))
                
                for rowNum in range(len(myResult)):
                    print()
                    print("Match ID: " , myResult[rowNum][0])
                    print("Season: " , myResult[rowNum][1])
                    print("City: " , myResult[rowNum][2])
                    print("Date: " , myResult[rowNum][3])
                    print(myResult[rowNum][4], " VS ", myResult[rowNum][5])
                    print("Winning team: ", myResult[rowNum][10] )
                print("------------")
            case "8":
                print("Exiting program...")
                keepGoing = False

            case _:
                print("That is not an option.")

def main():
    request_info()
    # Close connections
    cursor.close()
    db.close()

main()
