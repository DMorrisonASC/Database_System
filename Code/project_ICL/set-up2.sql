create table game (
	game_id varchar(100),
    season int,
    type varchar(10),
    date_time_GMT varchar(25),
    away_team_id smallint,
    home_team_id smallint,
    away_goals smallint,
    home_goals smallint,
    outcome varchar(25),
    home_rink_side_start varchar(10),
    venue varchar(100),
    venue_link varchar(250),
    venue_time_zone_id varchar(50),
    venue_time_zone_offset smallint,
    venue_time_zone_tz varchar(5),
    primary key (game_id)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/game.csv' 
INTO TABLE game 
FIELDS TERMINATED BY '' 
ENCLOSED BY ''
LINES TERMINATED BY ''
IGNORE 1 ROWS;

create table player_info (
	player_id int,
    firstName varchar(50),
    lastName varchar(50),
    nationality varchar(50),
    birthCity varchar(50),
    primaryPosition varchar(55),
    primary key (player_id)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/player_info.csv' 
INTO TABLE player_info 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

create table team_info (
	team_id int,
    franchiseId varchar(10),
    shortName varchar(50),
    teamName varchar(50),
    abbreviation varchar(4),
    link varchar(100),
    primary key (team_id)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/team_info.csv' 
INTO TABLE team_info 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

create table game_plays (
	play_id	varchar(50),
    game_id	varchar(100),
    team_id_for	varchar(100),
    team_id_against	varchar(100),
    event varchar(100),
    secondaryType varchar(100),	
    x varchar(100),
    y varchar(100),	
    period varchar(100),
    periodType varchar(100),	
    periodTime varchar(100),
    periodTimeRemaining varchar(100),	
    dateTime varchar(100),	
    goals_away varchar(100),	
    goals_home varchar(100),	
    description	varchar(100),
    st_x varchar(100),
    st_y varchar(100),
    primary key (play_id),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/game_plays.csv' 
INTO TABLE game_plays 
FIELDS TERMINATED BY ',' 
ENCLOSED BY ''
LINES TERMINATED BY ''
IGNORE 1 ROWS;

create table game_teams_stats (
	game_id varchar(100),
    team_id	varchar(20),
    HoA	varchar(4),
    won	varchar(6),
    settled_in varchar(6),
    head_coach varchar(50),
    goals int,
    shots int,	
    hits int,
    pim	int,
    powerPlayOpportunities int,
    powerPlayGoals int,	
    faceOffWinPercentage	int,
    giveaways int,
    takeaways	int,
	FOREIGN KEY (game_id) REFERENCES game(game_id),
    FOREIGN KEY (team_id) REFERENCES team(team_id)
);

create table game_plays_players (
	play_id varchar(50),
    game_id varchar(50),
    player_id varchar(50),
    player_type int,
	FOREIGN KEY (play_id) REFERENCES game_plays(play_id),
    FOREIGN KEY (player_id) REFERENCES player(player_info)
);

create table game_shifts (
    game_id varchar(50),
    player_id varchar(50),
    period int,
    shift_start int,
    shift_end int,
	FOREIGN KEY (play_id) REFERENCES game_plays(play_id),
    FOREIGN KEY (player_id) REFERENCES player(player_info)
);
