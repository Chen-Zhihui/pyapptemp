create view  as match_count
select targetID, count(pmatch.com) as c
from target left outer join pmatch on pmatch.target_id == target.id
GROUP BY targetID
order by c

create view as match_count_history
select c, count(c) 
from match_count
GROUP BY c;