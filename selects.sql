--3.3
SELECT f.name, f.title, r.first_name, r.last_name  FROM fieldthatdescribes f
INNER JOIN project p ON p.title = f.title
INNER JOIN researcher r ON p.evaluated_from = r.id
WHERE r.works_since > '2021-06-06'
AND p.end_date > '2022-06-06';

--3.4
