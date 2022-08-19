select 
	satellite_name as "卫星", 
	com as "服务商",  
	scene_count as "总景数",
	max_cloud as "云量最大值", 
	min_cloud as "云量最小值", 
	max_width as "宽度最大值", 
	min_width as "宽度最小值", 
	max_height as "高度最大值",
	min_height as "高度最小值",
	match_count as "位置匹配总数",
	matched_target_count as "目标匹配总数", 
	matched_scene_count as "影像匹配总数"
from (
select 
	satellite_name, 
	com, 
	count(id) as scene_count, 
	max(scence.width) as max_width, 
	min(width) as min_width, 
	max(scence.height) as max_height, 
	min(height) as min_height,
	max(cloud_pre) as max_cloud,
	min(cloud_pre) as min_cloud
from scence
group by satellite_name, com) as t1 join 
(
select 
	satellite_name as sname, 
	com as scom, 
	count(id) as match_count, 
	count(distinct pmatch.target_id) as matched_target_count, 
	count(distinct pmatch.scence_id) as matched_scene_count
from pmatch
group by satellite_name, com
) as t2 on t1.satellite_name==t2.sname and t1.com == t2.scom