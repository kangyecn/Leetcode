# Write your MySQL query statement below

#select c.name as 'customer' from customers as c 
#where c.id not in (select customerid from orders)

select customers.name as 'Customers'
from customers
where customers.id not in
(
    select customerid from orders
);