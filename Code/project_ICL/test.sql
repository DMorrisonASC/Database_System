# set global foreign_key_checks=1;
select * from players join most_runs_average_strikerate on players.player_Name = batsman where player_Name = "A Hales";
select * from players join most_runs_average_strikerate on players.player_Name = batsman;
#
with player_stats_info(Player_Name, DOB, Batting_Hand, Bowling_Skill, Country, batsman, total_runs_ever, `out`, numberofballs, average, strikerate) as (select * from players join most_runs_average_strikerate on players.player_Name = batsman)
select * from matches join 
player_stats_info
on matches.player_of_match = player_stats_info.player_Name;
# For project 2
with player_stats_info(Player_Name, DOB, Batting_Hand, Bowling_Skill, Country, batsman, total_runs_ever, `out`, numberofballs, average, strikerate) as (select * from players join most_runs_average_strikerate on players.player_Name = batsman)
select * from matches join 
player_stats_info
on matches.player_of_match = player_stats_info.player_Name 
where player_of_match = "A Kumble";


