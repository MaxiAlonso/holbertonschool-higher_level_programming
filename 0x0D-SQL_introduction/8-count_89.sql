-- Script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
-- Command to retrieve the number of records with id 89 in first_table of the database hbtn_0c_0 (passed by argument)
SELECT COUNT(id)
  FROM first_table
  WHERE id = 89;
