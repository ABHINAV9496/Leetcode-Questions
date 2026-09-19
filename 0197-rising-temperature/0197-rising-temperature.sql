# Write your MySQL query statement below
select today.id 
from weather as today
left join weather as yesterday
on today.recordDate= yesterday.recordDate + interval 1 day
where today.temperature > yesterday.temperature;