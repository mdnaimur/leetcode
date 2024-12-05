

-- solution one
select machine_id,round(sum(extract(epoch from end) - extract(epoch from start)) / count(process_id),3)

from    Activity
GROUP BY 
    machine_id;



select a1.machine_id,round(avg(a2.timestamp - a1.timestamp),3) as processing_time 
from Activity a1
join Activity a2 
on
 a1.machine_id = a2.machine_id
  and a1.process_id=a2.process_id 
  and a1.activity_type = 'start' 
  and a2.activity_type = 'end'
GROUP BY a1.machine_id;


-- for postgreeSQL

SELECT 
    a1.machine_id,
    ROUND(AVG(EXTRACT(EPOCH FROM a2.timestamp) - EXTRACT(EPOCH FROM a1.timestamp)), 3) AS processing_time
FROM 
    Activity a1
JOIN 
    Activity a2 
ON 
    a1.machine_id = a2.machine_id
    AND a1.process_id = a2.process_id
    AND a1.activity_type = 'start' 
    AND a2.activity_type = 'end'
GROUP BY 
    a1.machine_id;
;


select a1.machine_id
, ROUND(AVG(a2.timestamp - a1.timestamp),3) as processing_time
from
   Activity a1
join 
  Activity a2
on a1.process_id=a2.process_id
and a1.machine_id=a2.machine_id
and a1.timestamp<a2.timestamp
group by a1.machine_id;

| machine_id | processing_time |
| ---------- | --------------- |
| 0          | 0.894           |
| 1          | 0.995           |
| 2          | 1.456           |