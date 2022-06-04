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
@app.route("/projects_and_programs")
def projects_and_programs():
    return render_template('projects_and_programs.html')

#3.2
@app.route("/views", methods={'GET', 'POST'})
def views():
    if request.method == 'POST':
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

        if request.form['viewvalues'] == 0:
            return render_template('views.html', viewvalues=viewvalues1)
        elif request.form['viewvalues'] == 1:
            return render_template('views.html', viewvalues=viewvalues2)
        else:
            return render_template('views.html')



#3.3
@app.route("/most_popular_field")
def most_popular_field():
    return render_template('most_popular_field.html')

#3.4
@app.route("/same_number_of_projects")
def same_number_of_projects():
    return render_template('same_number_of_projects.html')

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
    return render_template('top_executives.html')

#3.8
@app.route("/work_in_five_or_more")
def work_in_five_or_more():
    return render_template('work_in_five_or_more.html')


# CRUD

@app.route("/create_entry")
def create_entry():
    return render_template('create_entry.html')

@app.route("/read_entry")
def read_entry():
    return render_template('read_entry.html')

@app.route("/update_entry")
def update_entry():
    return render_template('update_entry.html')

@app.route("/delete_entry")
def delete_entry():
    return render_template('delete_entry.html')

#END OF CRUD

if __name__ == '__main__':
    app.run(debug=True)
