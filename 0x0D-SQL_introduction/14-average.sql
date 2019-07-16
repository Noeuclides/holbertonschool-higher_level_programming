--  computes the score average of all records in the table.  
SELECT SUM(score) / COUNT(name) AS average
FROM second_table;

