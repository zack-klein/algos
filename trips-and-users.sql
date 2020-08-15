-- https://leetcode.com/problems/trips-and-users/submissions/

with unbanned as (
    select t.request_at, count(*) cancellations
    from Trips t
    join Users u1 on t.client_id = u1.users_id
    join Users u2 on t.driver_id = u2.users_id
    where u1.banned = "No"
    and u2.banned = "No"
    and t.status like "cancelled_by%"
    and t.request_at >= "2013-10-01"
    and t.request_at <= "2013-10-03"
    group by t.request_at
    order by t.request_at asc
), total as (
    select t.request_at, count(*) rides
    from Trips t
    join Users u1 on t.client_id = u1.users_id
    join Users u2 on t.driver_id = u2.users_id
    where u1.banned = "No"
    and u2.banned = "No"
    and t.request_at >= "2013-10-01"
    and t.request_at <= "2013-10-03"
    group by t.request_at
    order by t.request_at asc
)
select total.request_at Day
, round((ifnull(unbanned.cancellations, 0)/total.rides), 2) "Cancellation Rate"
from total
left join unbanned on total.request_at = unbanned.request_at
group by Day
