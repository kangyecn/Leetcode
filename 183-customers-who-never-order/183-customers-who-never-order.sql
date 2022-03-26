# Write your MySQL query statement below

select c.name as 'Customers' from customers as c 
where c.id not in (select customerid from orders)

#select c.name as 'Customers'
#from customers as c
#where c.id not in
#(
#    select customerid from orders
#);