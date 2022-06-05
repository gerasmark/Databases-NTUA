from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

database = yaml.safe_load(open('database.yaml'))
app.config["MYSQL_USER"] = database['mysql_user']
app.config["MYSQL_PASSWORD"] = database['mysql_password']
app.config["MYSQL_DB"] = database['mysql_db']
app.config["MYSQL_HOST"] = database['mysql_host']

db = MySQL(app)

#homepage
@app.route("/")
def index():
    return render_template('ui.html')

#3.1
@app.route("/projects_and_programs", methods={'GET', 'POST'})
def projects_and_programs():
    cur1 = db.connection.cursor()
    queryString1 = """
    SELECT name FROM program;
    """
    cur1.execute(queryString1)
    programs = cur1.fetchall()
    cur1.close()

    # if request.method == 'POST':
    #     if request.form['viewvalues'] == "first":
    #         viewvalues = viewvalues1
    #         chosen = "Έργα ανά ερευνητή"
    #     elif request.form['viewvalues'] == "second":
    #         viewvalues = viewvalues2
    #         chosen = "Έργα ανά οργανισμό"
    #     else:
    #         viewvalues = ''
    return render_template('projects_and_programs.html', programs=programs)

#3.2
@app.route("/views", methods={'GET', 'POST'})
def views():
    cur1 = db.connection.cursor()
    queryString1 = """
    SELECT concat(r.last_name," ", r.first_name) as Full_name, p.title as title_of_project
    FROM researcher r
    INNER JOIN worksfor w ON r.id = w.id
    INNER JOIN project p ON w.title = p.title
    ORDER BY Full_name;
    """
    cur1.execute(queryString1)
    viewvalues1 = cur1.fetchall()
    cur1.close()
    cur2 = db.connection.cursor()
    queryString2 = """
    SELECT o.name as organization_name, p.title as title_of_project
    FROM organization o
    INNER JOIN project p on o.name = p.from_org
    ORDER BY organization_name;
    """
    cur2.execute(queryString2)
    viewvalues2 = cur2.fetchall()
    cur2.close()
    viewvalues = ''
    chosen = ''
    if request.method == 'POST':
        if request.form['viewvalues'] == "first":
            viewvalues = viewvalues1
            chosen = "Έργα ανά ερευνητή"
        elif request.form['viewvalues'] == "second":
            viewvalues = viewvalues2
            chosen = "Έργα ανά οργανισμό"
        else:
            viewvalues = ''
    return render_template('views.html', viewvalues=viewvalues, chosen=chosen)


#3.3
@app.route("/most_popular_field", methods={'GET', 'POST'})
def most_popular_field():
    cur1 = db.connection.cursor()
    queryString1 = """
    SELECT * FROM scientific_field;
    """
    cur1.execute(queryString1)
    field = cur1.fetchall()
    cur1.close()
    chosen = ''
    values = ''
    if request.method == 'POST':
        chosen = request.form['field']
        if chosen == "Submit":
            chosen = ''
            return render_template('most_popular_field.html', field=field, chosen=chosen, values=values)
        cur2 = db.connection.cursor()
        queryString2 = """
        SELECT p.title, concat(r.last_name," ", r.first_name) as Full_name  FROM fieldthatdescribes f
        INNER JOIN project p ON f.title = p.title
        INNER JOIN worksfor w ON p.title = w.title
        INNER JOIN researcher r ON w.id = r.id
        WHERE r.works_since <= current_date() AND f.name =
        """
        queryString3= """
        AND p.end_date > current_date() AND p.start_date < current_date()
        union
        SELECT p.title, p.exec as Full_name  FROM fieldthatdescribes f
        INNER JOIN project p ON f.title = p.title
        WHERE f.name =
        """
        queryString4= """
        AND p.end_date > current_date() AND p.start_date < current_date()
        ORDER BY title;
        """
        wholeQuery = queryString2 + '"' + str(chosen) + '"' + queryString3 + '"' + str(chosen) + '"' + queryString4
        cur2.execute(wholeQuery)
        values = cur2.fetchall()
        cur2.close()
    return render_template('most_popular_field.html', field=field, chosen=chosen, values=values)

#3.4
@app.route("/same_number_of_projects")
def same_number_of_projects():
    cur = db.connection.cursor()
    queryString = """
    select o1.name, o1.year, o2.year,o1.projects
    from (select o.name, extract( year from p.start_date) as year, count(*) as projects
    from organization o
    inner join project p on o.name = p.from_org
    group by year, name) o1
    inner join (select o.name, extract( year from p.start_date) as year, count(*) as projects
    from organization o
    inner join project p on o.name = p.from_org
    group by year, name) o2 on o1.name = o2.name
    where ( o1.year <> o2.year and o1.year < o2.year)
    and o2.year - o1.year = 1 and o1.projects = o2.projects and o1.projects >= 10;
    """
    cur.execute(queryString)
    values = cur.fetchall()
    cur.close()
    return render_template('same_number_of_projects.html', values=values)

#3.5
@app.route("/top_pairs")
def top_pairs():
    cur = db.connection.cursor()
    queryString = """
    SELECT s1.name as project_1, s2.name as project_2
    FROM scientific_field s1
    INNER JOIN fieldthatdescribes f1 ON s1.name = f1.name
    INNER JOIN fieldthatdescribes f2 ON f1.title = f2.title
    INNER JOIN scientific_field s2 ON f2.name = s2.name
    WHERE s1.name <> s2.name
    GROUP BY s1.name, s2.name
    LIMIT 3;
    """
    cur.execute(queryString)
    pairnames = cur.fetchall()
    cur.close()
    return render_template('top_pairs.html', pairnames=pairnames)

#3.6
@app.route("/youngest_active_researchers")
def youngest_active_researchers():
    cur = db.connection.cursor()
    queryString = """
    SELECT concat(r.first_name," ", r.last_name) as Full_name, COUNT(*) as number_of_projects
    FROM researcher r
    INNER JOIN worksfor w ON r.id = w.id
    INNER JOIN project p ON w.title = p.title
    WHERE r.age < 40
    AND p.end_date > curdate() AND p.start_date < curdate()
    GROUP BY Full_name
    ORDER BY number_of_projects DESC
    """
    cur.execute(queryString)
    youngest = cur.fetchall()
    cur.close()
    return render_template('youngest_active_researchers.html', youngest=youngest)

#3.7
@app.route("/top_executives")
def top_executives():
    cur = db.connection.cursor()
    queryString = """
    SELECT p.exec as project_executive, c.name as company_name, SUM(p.amount) as total_amount
    FROM project p
    INNER JOIN organization o ON p.from_org = o.name
    INNER JOIN company c ON o.name = c.name
    GROUP BY p.exec, o.name
    ORDER BY SUM(p.amount) DESC
    LIMIT 5;
    """
    cur.execute(queryString)
    executives = cur.fetchall()
    cur.close()
    return render_template('top_executives.html', executives=executives)

#3.8
@app.route("/work_in_five_or_more")
def work_in_five_or_more():
    cur = db.connection.cursor()
    queryString = """
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
    """
    cur.execute(queryString)
    projects = cur.fetchall()
    cur.close()
    return render_template('work_in_five_or_more.html', projects=projects)


# CRUD

@app.route("/read_entry", methods={'GET', 'POST'})
def read_entry():
    cur1 = db.connection.cursor()
    queryString1 = """
    show tables;
    """
    cur1.execute(queryString1)
    field = cur1.fetchall()
    cur1.close()
    chosen = ''
    values = ''
    if request.method == 'POST':
        chosen = request.form['field']
        if chosen == "Submit":
            chosen = ''
            return render_template('read_entry.html',field=field, chosen=chosen, values=values)
        cur2 = db.connection.cursor()
        queryString2 = """
        select * from
        """
        wholeQuery = queryString2 + str(chosen)
        cur2.execute(wholeQuery)
        values = cur2.fetchall()
        cur2.close()
    return render_template('read_entry.html',field=field, chosen=chosen, values=values)

@app.route("/create_entry",methods={'GET', 'POST'})
def create_entry():
    cur1 = db.connection.cursor()
    pname = str(request.form.get('inputname'))
    paddress = str(request.form.get('inputaddress'))
    if (pname != 'None' and paddress != 'None'):
         queryString = """
         INSERT INTO program (name,address) VALUES ('{}','{}');
         """.format(pname, paddress)
    cur1.execute(queryString)
    cur1.close
    return render_template('create_entry.html')

@app.route("/update_entry")
def update_entry():
    return render_template('update_entry.html')

@app.route("/delete_entry")
def delete_entry():
    return render_template('delete_entry.html')

#END OF CRUD

if __name__ == '__main__':
    app.run(debug=True)
