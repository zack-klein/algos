-- https://www.hackerrank.com/challenges/weather-observation-station-8/
-- Some fun slicing gymnastics!


select distinct city
from station
where lower(substr(city, 1, 1)) in ('a', 'e', 'i', 'o', 'u')
and lower(substr(city, length(city), length(city))) in ('a', 'e', 'i', 'o', 'u');
