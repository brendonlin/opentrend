CREATE TABLE  lake.opentrend as
select name,
	REPLACE(REGEXP_SUBSTR(name,"^\/(.+?)\/",1),"/","") as username, 
	REPLACE(REGEXP_SUBSTR(name,"\/[^\/]+$",1),"/","") as reponame,
	language,
	total_star_count, fork_count, member_count, period_stars_count, period,
	created_dt,
	DATE_FORMAT(created_dt,"%Y-%m-%d") as created_day,
	Hour(created_dt) as hour
from sea.opentrend

CREATE INDEX idx on lake.opentrend(created_day);