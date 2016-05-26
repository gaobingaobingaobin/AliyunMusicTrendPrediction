CREATE DATABASE AliyunMusic CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';
USE AliyunMusic;
CREATE TABLE mars_tianchi_user_actions(
   id INT NOT NULL AUTO_INCREMENT,
   user_id VARCHAR(50) NOT NULL,
   song_id VARCHAR(50) NOT NULL,
   gmt_create VARCHAR(20) NOT NULL,
   action_type VARCHAR(5) NOT NULL,
   ds VARCHAR(10) NOT NULL,
   PRIMARY KEY (id)
);
CREATE TABLE mars_tianchi_songs(
   id INT NOT NULL AUTO_INCREMENT,
   song_id VARCHAR(50) NOT NULL,
   artist_id VARCHAR(50) NOT NULL,
   publish_time VARCHAR(10) NOT NULL,
   song_init_plays VARCHAR(5) NOT NULL,
   language_type VARCHAR(10) NOT NULL,
   gender VARCHAR(5) NOT NULL,
   PRIMARY KEY (id)
);
