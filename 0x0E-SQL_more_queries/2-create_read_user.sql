-- Script that creates the database hbtn_0d_2 and the user user_0d_2.
-- Query to create database:
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Query to create user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Query to grant privileges to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
