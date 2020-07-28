-- https://leetcode.com/problems/rising-temperature/

-- Original answer:
select weather_today.id
from weather weather_today
join weather weather_yesterday
on weather_today.recordDate - 1 = weather_yesterday.recordDate
where weather_today.temperature > weather_yesterday.temperature

-- Looked at the solution for this, but it was the same concept!
select weather_today.id
from weather weather_today
join weather weather_yesterday
on datediff(weather_today.recordDate) = 1
and weather_today.temperature > weather_yesterday.temperature
