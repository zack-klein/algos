"""
https://leetcode.com/problems/department-top-three-salaries/
"""

with ranked_salaries as (
    select
    departmentId,
    salary,
    rank() over (
        partition by departmentId
        order by salary desc
    ) salary_rank
    from employee
    group by departmentId, salary
)
select
    department.name Department,
    e.name Employee,
    ranked.salary Salary
from employee e
join ranked_salaries ranked
  on ranked.departmentId = e.departmentId
  and ranked.salary = e.salary
join department
  on ranked.departmentId = department.id
where ranked.salary_rank <= 3
