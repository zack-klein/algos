-- https://leetcode.com/problems/duplicate-emails/submissions/

select email
from person
group by email
having count(*) > 1
