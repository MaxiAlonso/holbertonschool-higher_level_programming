-- Script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
-- Query to create the database:
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Query to create the table:
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
    name VARCHAR(256) NOT NULL
    );