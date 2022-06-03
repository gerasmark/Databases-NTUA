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

--3.3 check alla den bgazei tpt isos na allaksoyme ta dummy data
SELECT p.title, r.first_name, r.last_name  FROM fieldthatdescribes f
INNER JOIN project p ON f.title = p.title
INNER JOIN researcher r ON p.evaluated_from = r.id
WHERE r.works_since >= current_date() AND f.name = "Mathematics"
AND p.end_date > current_date() AND p.start_date < current_date()
ORDER BY f.name;

--3.4
SELECT o1.name as organization_1,
       o2.name as organization_2
FROM organization o1
INNER JOIN project p1 ON o1.from_org = p1.name 
INNER JOIN project p2 ON COUNT(p1.from_org) = COUNT(p2.from_org)
INNER JOIN organization o2 ON p2.from_org = o2.name 
WHERE p1.start_date < (p2.start_date + '2-01-01')
AND p1.start_date > (p2.start_date - '2-01-01')
AND COUNT(p1.from_org) >= 20
AND COUNT(p2.from_org) >= 20;

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
SELECT r.first_name, r.last_name, COUNT(*) as number_of_projects
FROM researcher r
INNER JOIN worksfor w ON r.id = w.id
INNER JOIN project p ON w.title = p.title
WHERE r.age < 40 
AND p.end_date > curdate() AND p.start_date < curdate()
GROUP BY r.last_name, r.first_name
ORDER BY number_of_projects DESC

--3.7 check
SELECT p.exec as project_executive, c.name as company_name, SUM(p.amount) as total_amount
FROM project p 
INNER JOIN organization o ON p.from_org = o.name
INNER JOIN company c ON o.name = c.name
GROUP BY p.exec, o.name
ORDER BY SUM(p.amount) DESC
LIMIT 5;

--3.8 check den bgazei kati
select * from (
select concat(last_name, " ", first_name) as name_of_researcher, count(*) as projects_working_on  from (
(select r.last_name, r.first_name
from researcher r 
inner join worksfor w on r.id = w.id
inner join project p on w.title = p.title
inner join deliverable d on p.title = d.title_project
where d.title_project is null )) A
group by A.last_name, A.first_name ) B
where projects_working_on >= 5
order by projects_working_on desc;