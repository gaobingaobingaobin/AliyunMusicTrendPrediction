USE AliyunMusic;
LOAD DATA INFILE '/home/mars_tianchi_songs.csv' INTO TABLE mars_tianchi_songs
FIELDS TERMINATED BY ','
ENCLOSED BY '"';
LOAD DATA INFILE '/home/mars_tianchi_user_actions.csv' INTO TABLE mars_tianchi_user_actions
FIELDS TERMINATED BY ','
ENCLOSED BY '"';
