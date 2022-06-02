--3.3
SELECT f.name, f.title, r.first_name, r.last_name  FROM fieldthatdescribes f
INNER JOIN project p ON p.title = f.title
INNER JOIN researcher r ON p.evaluated_from = r.id
WHERE r.works_since >= '2021-06-06'
AND p.end_date > '2022-06-06'
GROUP BY f.name;

--3.4
SELECT o1.name as organization_1,
       o2.name as organization_2
 FROM organization o1
INNER JOIN project p1 ON p1.from_org = o1.name 
INNER JOIN project p2 ON COUNT(p1.from_org) = COUNT(p2.from_org)
INNER JOIN organization o2 ON p2.from_org = o2.name 
WHERE p1.start_date < (p2.start_date + '2-01-01')
AND p1.start_date > (p2.start_date - '2-01-01')
AND COUNT(p1.from_org) >= 20
AND COUNT(p2.from_org) >= 20

--3.5

--3.8
SELECT r.first_name, r.last_name, COUNT() FROM researcher r
INNER JOIN worksfor w ON r.id = w.id
INNER JOIN project p ON w.title = p.title
WHERE COUNT(w.id) >= 5
AND p.title <> (SELECT d.title FROM deliverable d)