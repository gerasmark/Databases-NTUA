SELECT f.name, f.title FROM fieldthatdescribes f
INNER JOIN project p ON p.title = f.title
WHERE p.end_date > '2022-06-06';
