# Write your MySQL query statement below

        
select 

d.name as 'Department', e1.name as 'Employee', e1.Salary from

Employee e1 join Department d on e1.Departmentid=d.id

where

3 > (select count(distinct e2.salary) from employee e2 where e2.salary>e1.salary 
    and e1.departmentID=e2.departmentID)