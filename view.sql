CREATE VIEW researchers AS
SELECT DISTINCT
r.first_name + ' ' + r.last_name as Full_name,
p.title as Project_title
FROM researcher
INNER JOIN worksfor w AS r.id = w.id
INNER JOIN project p AS w.title = p.title
