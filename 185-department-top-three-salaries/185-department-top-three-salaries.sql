# Write your MySQL query statement below
select
    d.name as department,
    e1.name as employee,
    e1.salary
from employee e1 
left join department d 
on e1.departmentid = d.id
where
    (select count(distinct (e2.salary)) 
    from employee e2 
    where 
        e2.salary >= e1.salary
        and e2.departmentid = e1.departmentid) <=3