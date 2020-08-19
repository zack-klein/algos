-- https://www.hackerrank.com/challenges/weather-observation-station-5
-- For how easy this should be, I had a weirdly hard time finding a solution.
-- I was able to brute-force it:
with max_city as (
    select city, length(city) city_length
    from station
    where length(city) = (select max(length(city)) from station)
    order by city asc
    limit 1
), min_city as (
    select city, length(city) city_length
    from station
    where length(city) = (select min(length(city)) from station)
    order by city asc
    limit 1
)
select ma.city, ma.city_length
from max_city ma
union all
select mi.city, mi.city_length
from min_city mi;
