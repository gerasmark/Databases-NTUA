--read
show tables
SHOW COLUMNS FROM program
select * from program

--create
INSERT INTO program (name,address) VALUES ('{}','{}')

INSERT INTO organization (name,initials,postal_code,street,city) VALUES ('{}','{}','{}','{}')

select name from organization
INSERT INTO researcher (id,first_name,last_name,sex,birthdate,name,works_since) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')

select name from organization
INSERT INTO phone (name,phone) VALUES ('{}','{}')

select name from organization
INSERT INTO research_center (name,budget_from_edu,budget_from_priv) VALUES ('{}','{}','{}')

select name from organization
INSERT INTO university (name,budget_from_edu) VALUES ('{}','{}')

select name from organization
INSERT INTO company (name,equity) VALUES ('{}','{}')

select name from program
select name from organization
select id from researcher
INSERT INTO project (title,amount,summary,start_date,end_date,name,evaluated_from,from_org,grade,date_of_eval,exec) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')

INSERT INTO scientific_field (name) VALUES ('{}')

select title_of_project from deliverable
INSERT INTO deliverable (title,summary,title_project,due_date) VALUES ('{}','{}','{}','{}')

select name from scientific_field
select title from project
INSERT INTO fieldthatdescribes (name,title) VALUES ('{}','{}')

select title from project
select id from researcher
INSERT INTO worksfor (title,id) VALUES ('{}','{}')


--update
UPDATE program SET address = '{}' WHERE name = '{}'

UPDATE organization SET initials = '{}', postal_code = '{}', street = '{}', city = '{}' WHERE name = '{}'

UPDATE researcher SET first_name = '{}', last_name = '{}', sex = '{}', birthdate = '{}' , works_since = '{}' WHERE id = '{}'

UPDATE phone SET phone = '{}' WHERE name = '{}'

UPDATE research_center SET budget_from_edu = '{}', budget_from_priv = '{}' WHERE name = '{}'

UPDATE university SET budget_from_edu = '{}' where name = '{}'

update company set equity = '{}' where name = '{}'

update project set amount = '{}', summary = '{}', start_date = '{}', end_date = '{}', grade = '{}', date_of_eval = '{}', exec = '{}' where title = '{}'

update scientific_field set name = '{}'

update deliverable set summary = '{}', due_date = '{}', title = '{}' where title_project = '{}'

update deliverable set summary = '{}', due_date = '{}' where title = '{}'


--delete

delete from program WHERE name = '{}'


delete from organization WHERE name = '{}'


delete from researcher WHERE id = '{}'


delete from project WHERE title = '{}'





delete from deliverable WHERE title = '{}'




delete from research_center WHERE name = '{}'


delete from university WHERE name = '{}'


delete from company WHERE name = '{}'



delete from phone WHERE phome = '{}'
