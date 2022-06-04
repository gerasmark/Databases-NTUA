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

select title from project
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
delete from program WHERE address = '{}'  
delete from program WHERE name = '{}'

delete from organization WHERE initials = '{}' ,   
delete from organization WHERE postal_code = '{}'
delete from organization WHERE street = '{}'
delete from organization WHERE name = '{}'
delete from organization WHERE city = '{}'





delete from researcher  first_name = '{}', last_name = '{}', sex = '{}', birthdate = '{}' , works_since = '{}' WHERE id = '{}'

delete from phone  phone = '{}' WHERE name = '{}'

delete from research_center  budget_from_edu = '{}', budget_from_priv = '{}' WHERE name = '{}'

delete from university  budget_from_edu = '{}' where name = '{}'

delete from company  equity = '{}' where name = '{}' 

delete from project  amount = '{}', summary = '{}', start_date = '{}', end_date = '{}', grade = '{}', date_of_eval = '{}', exec = '{}' where title = '{}'

delete from scientific_field  name = '{}'

delete from deliverable  summary = '{}', due_date = '{}', title = '{}' where title_project = '{}'

delete from deliverable  summary = '{}', due_date = '{}' where title = '{}'