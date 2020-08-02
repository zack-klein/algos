-- https://leetcode.com/problems/consecutive-numbers/

-- Original answer
select distinct l1.num consecutivenums
from logs l1
inner join logs l2
on l1.id = l2.id - 1
inner join logs l3
on l1.id = l3.id - 2
where l1.num = l2.num and l2.num = l3.num;

-- Can also be done without Joins
select distinct l1.num consecutivenums
from logs l1, logs l2, logs l3
where l1.id = l2.id - 1
and l1.id = l3.id - 2
and l1.num = l2.num
and l2.num = l3.num;
