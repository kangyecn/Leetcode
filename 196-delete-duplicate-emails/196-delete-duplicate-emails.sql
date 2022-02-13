# Write your MySQL query statement below
DELETE FROM Person WHERE id NOT IN 
(SELECT minimum_ids FROM 
    (SELECT MIN(id) as minimum_ids FROM Person GROUP BY email) 
as min_id)