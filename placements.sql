-- https://www.hackerrank.com/challenges/placements
-- Good join practice!
select s1.name
from students s1
join friends f
on s1.id = f.id
join students s2
on f.friend_id = s2.id
join packages sal1
on s1.id = sal1.id
join packages sal2
on f.friend_id = sal2.id
where sal2.salary > sal1.salary
order by sal2.salary asc;
