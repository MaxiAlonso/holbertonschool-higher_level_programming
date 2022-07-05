-- Script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
-- Command to create the second_table of database hbtn_0c_0(passed by argument)
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
    );
-- Command add elements to the table
INSERT INTO second_table (id, name, score)
VALUES (1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8);
