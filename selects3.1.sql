SELECT name FROM program;

SELECT p.title as Project_title
from project p
where p.exec like ''{}'%' and p.duration = '{}' and p.start_date > '{}'  and p.end_date < '{}';

select Full_name from 
(select  p.title , concat(r.last_name," ", r.first_name) as Full_name
from researcher r 
inner join worksfor w on r.id = w.id
inner join project p on w.title = p.title
where p.title = '{}'
order by Full_name) 


