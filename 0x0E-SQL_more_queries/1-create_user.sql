-- Script that creates the MySQL server user user_0d_1.
-- Query to create user:
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_1_pwd';
-- Query to grant privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
