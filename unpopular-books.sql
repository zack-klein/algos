-- https://leetcode.com/problems/unpopular-books/submissions/

with quantities as (
    select book_id, sum(quantity) quantity
    from orders
    where dispatch_date >= '2018-06-23'
    group by book_id
), names_quantities as (
    select books.book_id, books.name, quantities.quantity quantity
    from books
    left join quantities
    on books.book_id = quantities.book_id
    where available_from <= '2019-05-23'
)
select book_id, name
from names_quantities
where quantity < 10 or quantity is null
