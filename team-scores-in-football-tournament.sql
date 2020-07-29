-- My monstrosity:
with wins_losses as (
    select
        case
            when host_goals > guest_goals
            then host_team
            when host_goals < guest_goals
            then guest_team
        end as winner_id,
        count(*) * 3 as points
    from matches
    where host_goals != guest_goals
    group by winner_id
)
, ties as (
    select host_team team, count(*) points
        from matches
        where host_goals = guest_goals
    union all
    select guest_team team, count(*) points
        from matches
        where host_goals = guest_goals
    group by team
)
, results as (
    select teams.team_id
    , teams.team_name
    , case
        when ties.points is null then wins_losses.points
        when wins_losses.points is null then ties.points
        when wins_losses.points > 0 and ties.points > 0 then wins_losses.points + ties.points
        else 0
      end as num_points
    from teams
    left join wins_losses
        on teams.team_id = wins_losses.winner_id
    left join ties
        on teams.team_id = ties.team
    order by num_points desc, team_name asc
)
select team_id
, team_name
, case when num_points is null then 0 else num_points end as num_points from results
order by num_points desc, team_name asc


-- A much cleaner solution:
SELECT team_id,team_name,
SUM(CASE WHEN team_id=host_team AND host_goals>guest_goals THEN 3 ELSE 0 END)+
SUM(CASE WHEN team_id=guest_team AND guest_goals>host_goals THEN 3 ELSE 0 END)+
SUM(CASE WHEN team_id=host_team AND host_goals=guest_goals THEN 1 ELSE 0 END)+
SUM(CASE WHEN team_id=guest_team AND guest_goals=host_goals THEN 1 ELSE 0 END)
as num_points
FROM Teams
LEFT JOIN Matches
ON team_id=host_team OR team_id=guest_team
GROUP BY team_id
ORDER BY num_points DESC, team_id ASC;
