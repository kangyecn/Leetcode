# Write your MySQL query statement below
select id,

case when p_id is null then 'Root'
when id in (select t2.p_id from tree t2) then 'Inner'
else 'Leaf'

end as type

from tree t1