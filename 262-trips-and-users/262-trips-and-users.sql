# Write your MySQL query statement below

select request_at as Day, round(sum(if(status!='completed', 1, 0))/count(status), 2) as 'Cancellation Rate' from
Trips where Request_at >='2013-10-01' and Request_at <= '2013-10-03'
and client_id in (select users_id from Users where banned != 'Yes')
and driver_id in (select users_id from Users where banned != 'Yes')
group by request_at
order by request_at