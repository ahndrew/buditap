#!/bin/bash
# buditap db shell script 

username="buditap"
password="budishake"
db_name="flowmeter_db"
tbl_1="keg_pours"
tbl_2="beers"
tbl_3="proximity_checks"

Q1="CREATE DATABASE IF NOT EXISTS $db_name;"

Q2="CREATE TABLE IF NOT EXISTS $tbl_1 (
  id int(12) NOT NULL auto_increment,
  pour_amount varchar(255) NOT NULL,
  user_id int(12),
  poured_at timestamp,
  PRIMARY KEY  (id)
);"

Q3="CREATE TABLE IF NOT EXISTS $tbl_2 (
  id int(12) NOT NULL auto_increment,
  name varchar(255),
  quantity varchar(255),
  installed_at timestamp,
  removed_at timestamp,
  PRIMARY KEY  (id)
);"

Q4="CREATE TABLE IF NOT EXISTS $tbl_3 (
  id int(12) NOT NULL auto_increment,
  proximity varchar(255),
  user_id int(12),
  timed_at timestamp,
  PRIMARY KEY  (id)
);"

SQL="${Q1}${Q2}${Q3}${Q4}"

mysql -hec2-54-86-171-52.compute-1.amazonaws.com -u $username -p$password -e "$SQL" $db_name
