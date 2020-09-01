-- https://www.hackerrank.com/challenges/the-pads/problem

with names as (
    select
        concat(name, '(', left(occupation, 1), ')') name_c
    from occupations
    order by name_c asc
)
, occupations as (
    select concat('There are a total of ', count(occupation), ' ', lower(occupation), 's.') occ_c
    from occupations
    group by occupation
    order by count(occupation) asc, occupation asc
)
select name_c from names
union all
select occ_c from occupations
order by 1;
