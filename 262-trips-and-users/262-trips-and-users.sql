select 
    request_at as day,
    round(
        sum(
            if(
                status='completed',0,1
            )
        )/count('status'),2
    ) as 'Cancellation Rate'
from trips
where
    request_at >= '2013-10-01'
    and request_at <= '2013-10-03'
    and client_id in 
        (select users_id from users 
         where 
            banned = 'No'
            and role = 'client')
    and driver_id in
        (select users_id from users
        where 
            banned = 'No'
            and role = 'driver')
group by request_at
order by request_at