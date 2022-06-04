--3.1 trexoun kai ta tria to trito den bgazei tpt omos
SELECT name FROM program;

SELECT p.title as Project_title
from project p
where p.exec like '%' and p.duration > 0 and ((p.start_date < current_date())  and (p.end_date > current_date()));

select Full_name from 
(select  p.title , concat(r.last_name," ", r.first_name) as Full_name
from researcher r 
inner join worksfor w on r.id = w.id
inner join project p on w.title = p.title
order by Full_name) A
where A.title = '%';

--3.2 check 

create view projects_per_researcher as
(select concat(r.last_name," ", r.first_name) as Full_name, p.title as title_of_project 
from researcher r 
inner join worksfor w on r.id = w.id 
inner join project p on w.title = p.title)
order by Full_name ;

select * from projects_per_researcher;

create view projects_per_organization as 
select o.name as organization_name, p.title as title_of_project
from organization o 
inner join project p on o.name = p.from_org
order by organization_name ;

select * from projects_per_organization;

drop view projects_per_researcher;
drop view projects_per_organization;

--3.3 check 
select * from scientific_field;

SELECT p.title, concat(r.last_name," ", r.first_name) as Full_name  FROM fieldthatdescribes f
INNER JOIN project p ON f.title = p.title
INNER JOIN worksfor w ON p.title = w.title
INNER JOIN researcher r ON w.id = r.id
WHERE r.works_since <= current_date() AND f.name = "Mathematics"
AND p.end_date > current_date() AND p.start_date < current_date()
union
SELECT p.title, p.exec as Full_name  FROM fieldthatdescribes f
INNER JOIN project p ON f.title = p.title
WHERE f.name = "Mathematics"
AND p.end_date > current_date() AND p.start_date < current_date() 
ORDER BY Full_name;

--3.4 
create view organizations as
select o.name, extract( year from p.start_date) as year, count(*) as projects 
from organization o 
inner join project p on o.name = p.from_org
group by year, name;
select * from organizations;

select o1.name, o1.year, o2.year,o1.projects
from organizations o1
inner join organizations o2 on o1.name = o2.name
where ( o1.year <> o2.year and o1.year < o2.year)
and o2.year - o1.year = 1 and o1.projects = o2.projects and o1.projects >= 10;

--3.5 check
CREATE VIEW organizations_with_same_project_numbers as
SELECT s1.name as project_1, s2.name as project_2
FROM scientific_field s1 
INNER JOIN fieldthatdescribes f1 ON s1.name = f1.name
INNER JOIN fieldthatdescribes f2 ON f1.title = f2.title
INNER JOIN scientific_field s2 ON f2.name = s2.name
WHERE s1.name <> s2.name
GROUP BY s1.name, s2.name
LIMIT 3;

DROP VIEW organizations_with_same_project_numbers;

--3.6 check
SELECT concat(r.first_name," ", r.last_name) as Full_name, COUNT(*) as number_of_projects
FROM researcher r
INNER JOIN worksfor w ON r.id = w.id
INNER JOIN project p ON w.title = p.title
WHERE r.age < 40
AND p.end_date > curdate() AND p.start_date < curdate()
GROUP BY Full_name
ORDER BY number_of_projects DESC

--3.7 check
SELECT p.exec as project_executive, c.name as company_name, SUM(p.amount) as total_amount
FROM project p 
INNER JOIN organization o ON p.from_org = o.name
INNER JOIN company c ON o.name = c.name
GROUP BY p.exec, o.name
ORDER BY SUM(p.amount) DESC
LIMIT 5;

--3.8 check 
select * from (
select concat(last_name, " ", first_name) as Full_name, count(*) as projects  from (
(select r.last_name, r.first_name
from researcher r 
inner join worksfor w on r.id = w.id
inner join project p on w.title = p.title
left join deliverable d on p.title = d.title_project
where d.title_project is null )) A
group by A.last_name, A.first_name ) B
where projects >= 5
order by projects desc;
