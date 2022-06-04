--read
select * from '{}'

--create
INSERT INTO program (name,address) VALUES ('{}','{}')

INSERT INTO organization (name,initials,postal_code,street,city) VALUES ('{}','{}','{}','{}')

INSERT INTO researcher (id,first_name,last_name,sex,birthdate,name,works_since) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')

INSERT INTO phone (name,phone) VALUES ('{}','{}')

INSERT INTO research_center (name,budget_from_edu,budget_from_priv) VALUES ('{}','{}','{}')

INSERT INTO university (name,budget_from_edu) VALUES ('{}','{}')

INSERT INTO company (name,equity) VALUES ('{}','{}')

INSERT INTO project (title,amount,summary,start_date,end_date,name,evaluated_from,from_org,grade,date_of_eval,exec) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')

INSERT INTO scientific_field (name) VALUES ('{}')

INSERT INTO deliverable (title,summary,title_project,due_date) VALUES ('{}','{}','{}','{}')

INSERT INTO fieldthatdescribes (name,title) VALUES ('{}','{}')

INSERT INTO worksfor (title,id) VALUES ('{}','{}')


--update



--delete