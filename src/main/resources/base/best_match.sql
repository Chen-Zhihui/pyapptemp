SELECT 
	M1.target_id as 目标编号, 
	max(M1.score) as 最高分, 
	(
    select MAX(scence_id)
    from pmatch M2
	  where M2.target_id == M1.target_id
		AND M2.score = MAX(M1.score) ) as 最佳影像, 
	count(*) as 备选数据量, 
	pmatch.id as 匹配ID
--FROM ((((pmatch join scence on pmatch.scence_id == scence.id) as M) join target on target.id == M.target_id) as N join targetgroup on targetgroup.country == N.country) as M1 
from (pmatch join scence, target, targetgroup on pmatch.scence_id==scence.id and target.id==pmatch.target_id and targetgroup.country == target.country) as M1
where M1.score > 0 and M1.covered == 0 and M1.used == 0
group by M1.target_id 