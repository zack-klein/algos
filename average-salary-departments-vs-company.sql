-- Write your MySQL query statement below
-- https://leetcode.com/problems/average-salary-departments-vs-company/
with by_department as (
    select s.pay_date
    , e.department_id
    , avg(s.amount) average_salary
    from salary s
    join employee e
    on s.employee_id = e.employee_id
    group by
    e.department_id
    , s.pay_date
), company as (
    select pay_date
    , avg(amount) average_salary
    from salary
    group by pay_date
), unique_mapping as(
select
  left(d.pay_date, 7) pay_month
  , d.department_id
  , case
      when d.average_salary > c.average_salary then 'higher'
      when d.average_salary < c.average_salary then 'lower'
      else 'same'
      end as comparison
  from by_department d
  join company c
  on d.pay_date = c.pay_date
  order by d.department_id asc, d.pay_date asc
)
select distinct *
from unique_mapping;
