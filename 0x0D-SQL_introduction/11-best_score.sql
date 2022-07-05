-- Script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
-- Command to list those records of the second table of the databes hbtn_0c_0 (passe by argument) with a score >= 10
SELECT score, name
    FROM second_table
    WHERE score >= 10
    ORDER BY score DESC;
