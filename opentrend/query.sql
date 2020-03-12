with cte1 as(
SELECT `language` as lan,created_day,period,sum(period_stars_count) as cnt
FROM lake.opentrend
where `hour`= 18
and created_day >= "2020-01-02"
group by 1,2,3),
daily as(
SELECT lan,created_day,cnt
from cte1
where period = "daily"),
weekly as(
SELECT lan,created_day,cnt
from cte1
where period = "weekly"
),
monthly as(
SELECT lan,created_day,cnt
from cte1
where period = "monthly"
)
select daily.created_day,daily.lan,daily.cnt as daily_cnt,weekly.cnt as weekly_cnt,monthly.cnt as monthly_cnt
from daily
left OUTER join weekly
on daily.lan = weekly.lan and weekly.created_day BETWEEN DATE_SUB(daily.created_day,INTERVAL 6 DAY) and daily.created_day
left OUTER join monthly
on daily.lan = monthly.lan and monthly.created_day BETWEEN DATE_SUB(daily.created_day,INTERVAL 6 DAY) and daily.created_day
