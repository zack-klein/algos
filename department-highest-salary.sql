-- https://leetcode.com/problems/department-highest-salary

-- Original answer
with max_dept_salaries as (
    select d.name department, e.departmentid, max(e.salary) salary
    from employee e
    inner join department d
    on e.departmentid = d.id
    group by e.departmentid
)
select d.department Department
, e.name Employee
, d.salary Salary
from max_dept_salaries d
inner join employee e
on d.departmentid = e.departmentid
and d.salary = e.salary;
