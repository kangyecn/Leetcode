# Write your MySQL query statement below

select name from salesperson where name not in
(
select s.name from salesperson as s
left join orders as o 
on s.sales_id = o.sales_id
left join company as c
on o.com_id = c.com_id
where c.name ='Red'
    )