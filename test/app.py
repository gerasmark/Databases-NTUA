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

    cur2 = db.connection.cursor()
    queryString2 = """
    select distinct duration from project
    order by duration
    """
    cur2.execute(queryString2)
    duration = cur2.fetchall()
    cur2.close()

    cur3 = db.connection.cursor()
    queryString3 = """
    select distinct exec from project
    order by exec
    """
    cur3.execute(queryString3)
    exec = cur3.fetchall()
    cur3.close()

    chosen_start = ''
    chosen_end = ''
    chosen_duration = ''
    chosen_exec = ''
    queryString4 = ''
    projects = ''
    projects2=''
    researchers = []


    if request.method == 'POST':
        chosen_start = request.form['start']
        chosen_end = request.form['end']
        chosen_duration = request.form['duration']
        chosen_exec = request.form['exec']
        if chosen_start == '':
            chosen_start = ''
        if chosen_end == '':
            chosen_end = ''
        if chosen_duration == "Submit":
            chosen_duration = ''
        if chosen_exec == "Submit":
            chosen_exec = ''

        cur4 = db.connection.cursor()
        queryString4 = """
        SELECT p.title as Project_title
        from project p
        where p.start_date < current_date()
        """
        if chosen_start != '':
            queryString4 = queryString4 + " and (p.start_date > " + "'" + chosen_start + "'" + ")"
        if chosen_end != '':
            queryString4 = queryString4 + " and (p.end_date < " + "'" + chosen_end + "'" + ")"
        if chosen_duration != '':
            queryString4 = queryString4 + "  and p.duration = " + chosen_duration
        if chosen_exec != '':
            queryString4 = queryString4 + " and p.exec = " + '"' + chosen_exec + '"'
        queryString4 = queryString4 + ';'
        cur4.execute(queryString4)
        projects = cur4.fetchall()
        cur4.close()
        tempcounter = len(projects)
        projects2= [(item,idx) for item,idx in enumerate(projects)]





        for i in range(tempcounter):
            cur5 = db.connection.cursor()
            queryString5 = """
            select t.Full_name from
            (select p.title , concat(r.last_name," ", r.first_name) as Full_name
            from researcher r
            inner join worksfor w on r.id = w.id
            inner join project p on w.title = p.title
            where p.title =
            """
            queryString6 = """
            order by Full_name) t
            ORDER BY t.Full_name;
            """
            temp=projects[i]
            temp=temp[0]
            queryString7 = queryString5 + '"' + temp + '"' + queryString6
            cur5.execute(queryString7)
            researchers.append(cur5.fetchall())
            cur5.close()

        # skase = projects[0]
        # skase = skase[0]


    return render_template('projects_and_programs.html', programs=programs, chosen_start=chosen_start, chosen_end=chosen_end, chosen_duration=chosen_duration, chosen_exec=chosen_exec, queryString4=queryString4, duration=duration, exec=exec, projects=projects, projects2=projects2, researchers=researchers)

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
    columns = ''

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

        cur3 = db.connection.cursor()
        queryString3 = """
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = '{}'
        ORDER BY ORDINAL_POSITION
        """.format(chosen)
        cur3.execute(queryString3)
        columns = cur3.fetchall()
        cur3.close()

    return render_template('read_entry.html',field=field, chosen=chosen, values=values, columns=columns)

@app.route("/create_entry",methods={'GET', 'POST'})
def create_entry():
    errorprogram = ''
    queryString = ''
    oqueryString = ''
    phqueryString = ''
    rqueryString = ''
    rcqueryString = ''
    uqueryString = ''
    cqueryString = ''
    pqueryString = ''
    squeryString = ''
    dqueryString = ''
    fqueryString = ''
    wqueryString = ''

    cnames = ''
    dtitle_projects = ''
    fnames = ''
    ftitles = ''
    pfrom_orgs = ''
    pevaluated_froms = ''
    pnames = ''
    rnames = ''
    wids = ''
    wtitles = ''
    unames = ''
    rcnames = ''
    phnames = ''

    cur = db.connection.cursor()
    queryStringInitial = """
    select name from organization
    """
    cur.execute(queryStringInitial)
    cnames = cur.fetchall()
    cur.close()

    cur = db.connection.cursor()
    queryStringInitial = """
    select title from project
    """
    cur.execute(queryStringInitial)
    dtitle_projects = cur.fetchall()
    cur.close()

    cur = db.connection.cursor()
    queryStringInitial = """
    select name from scientific_field
    """
    cur.execute(queryStringInitial)
    fnames = cur.fetchall()
    cur.close()

    cur = db.connection.cursor()
    queryStringInitial = """
    select title from project
    """
    cur.execute(queryStringInitial)
    ftitles = cur.fetchall()
    cur.close()

    cur = db.connection.cursor()
    queryStringInitial = """
    select name from organization
    """
    cur.execute(queryStringInitial)
    phnames = cur.fetchall()
    cur.close()

    cur = db.connection.cursor()
    queryStringInitial = """
    select name from organization
    """
    cur.execute(queryStringInitial)
    rcnames = cur.fetchall()
    cur.close()

    cur = db.connection.cursor()
    queryStringInitial = """
    select name from organization
    """
    cur.execute(queryStringInitial)
    unames = cur.fetchall()
    cur.close()

    cur = db.connection.cursor()
    queryStringInitial = """
    select title from project
    """
    cur.execute(queryStringInitial)
    wtitles = cur.fetchall()
    cur.close()

    cur = db.connection.cursor()
    queryStringInitial = """
    select id from researcher
    """
    cur.execute(queryStringInitial)
    wids = cur.fetchall()
    cur.close()

    cur = db.connection.cursor()
    queryStringInitial = """
    select name from organization
    """
    cur.execute(queryStringInitial)
    rnames = cur.fetchall()
    cur.close()

    cur = db.connection.cursor()
    queryStringInitial = """
    select name from program
    """
    cur.execute(queryStringInitial)
    pnames = cur.fetchall()
    cur.close()

    cur = db.connection.cursor()
    queryStringInitial = """
    select id from researcher
    """
    cur.execute(queryStringInitial)
    pevaluated_froms = cur.fetchall()
    cur.close()

    cur = db.connection.cursor()
    queryStringInitial = """
    select name from organization
    """
    cur.execute(queryStringInitial)
    pfrom_orgs = cur.fetchall()
    cur.close()


    if request.method == 'POST':
        cur1 = db.connection.cursor()
        prname = str(request.form.get('prname'))
        praddress = str(request.form.get('praddress'))

        oname = str(request.form.get('oname'))
        oinitials = str(request.form.get('oinitials'))
        opostal_code = str(request.form.get('opostal_code'))
        ostreet = str(request.form.get('ostreet'))
        ocity = str(request.form.get('ocity'))

        rid = str(request.form.get('rid'))
        rfirst_name = str(request.form.get('rfirst_name'))
        rlast_name = str(request.form.get('rlast_name'))
        rsex = str(request.form.get('rsex'))
        rbirthdate = str(request.form.get('rbirthdate'))
        rname = str(request.form.get('rname'))
        rworks_since = str(request.form.get('rworks_since'))

        phphone = str(request.form.get('phphone'))
        phname = str(request.form.get('phname'))

        rcname = str(request.form.get('rcname'))
        rcbudget_from_edu = str(request.form.get('rcbudget_from_edu'))
        rcbudget_from_priv = str(request.form.get('rcbudget_from_priv'))

        uname = str(request.form.get('uname'))
        ubudget_from_edu = str(request.form.get('ubudget_from_edu'))

        cname = str(request.form.get('cname'))
        cequity = str(request.form.get('cequity'))

        sname = str(request.form.get('sname'))

        dtitle = str(request.form.get('dtitle'))
        dsummary = str(request.form.get('dsummary'))
        dtitle_project = str(request.form.get('dtitle_project'))
        ddue_date = str(request.form.get('ddue_date'))

        fname = str(request.form.get('fname'))
        ftitle = str(request.form.get('ftitle'))

        wtitle = str(request.form.get('wtitle'))
        wid = str(request.form.get('wid'))

        ptitle = str(request.form.get('ptitle'))
        pamount = str(request.form.get('pamount'))
        psummary = str(request.form.get('psummary'))
        pstart_date = str(request.form.get('pstart_date'))
        pend_date = str(request.form.get('pend_date'))
        pname = str(request.form.get('pname'))
        pevaluated_from = str(request.form.get('pevaluated_from'))
        pfrom_org = str(request.form.get('pfrom_org'))
        pgrade = str(request.form.get('pgrade'))
        pdate_of_eval = str(request.form.get('pdate_of_eval'))
        pexec = str(request.form.get('pexec'))

        if (prname != ''and praddress != ''):
             queryString = """
             INSERT INTO program (name,address) VALUES ('{}','{}');
             """.format(prname, praddress)
             cur1.execute(queryString)
             db.connection.commit()
        else:
            errorprogram="Field is required"

        if (oname != '' and oinitials  != '' and opostal_code != '' and ostreet != '' and  ocity != ''):
             oqueryString = """
             INSERT INTO organization (name,initials,postal_code,street,city) VALUES ('{}','{}','{}','{}');
             """.format(oname, oinitials, opostal_code, ostreet, ocity)
             cur1.execute(oqueryString)
             db.connection.commit()
        else:
            errorprogram="Field is required"

        if (rid != '' and rfirst_name != '' and rlast_name != '' and rsex != '' and rbirthdate != '' and rname != '' and rworks_since):
             rqueryString = """
             INSERT INTO researcher (id,first_name,last_name,sex,birthdate,name,works_since) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}');
             """.format(rid, rfirst_name, rlast_name, rsex, rbirthdate, rname, rworks_since)
             cur1.execute(rqueryString)
             db.connection.commit()
        else:
            errorprogram="Field is required"

        if (ptitle != '' and pamount != '' and psummary != '' and pstart_date != '' and pend_date != '' and pname != '' and pfrom_org != '' and pevaluated_from != '' and pexec != '' and pgrade != '' and pdate_of_eval != ''):
            pqueryString = """
            INSERT INTO project (title,amount,summary,start_date,end_date,name,evaluated_from,from_org,grade,date_of_eval,exec) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');
            """.format(ptitle, pamount, psummary, pstart_date, pend_date, pname, pevaluated_from, pfrom_org, pgrade, pdate_of_eval, pexec)
            cur1.execute(pqueryString)
            db.connection.commit()
        else:
            errorprogram="Field is required"

        if (phname != '' and phphone != '' ):
             phqueryString = """
             INSERT INTO phone (name,phone) VALUES ('{}','{}');
             """.format(phname,phphone)
             cur1.execute(phqueryString)
             db.connection.commit()
        else:
            errorprogram="Field is required"

        if (rcname != '' and rcbudget_from_edu  != '' and rcbudget_from_priv != ''):
             rcqueryString = """
             INSERT INTO research_center (name,budget_from_edu,budget_from_priv) VALUES ('{}','{}','{}');
             """.format(rcname, rcbudget_from_edu, rcbudget_from_priv)
             cur1.execute(rcqueryString)
             db.connection.commit()
        else:
            errorprogram="Field is required"

        if (cname != '' and cequity != ''):
            cqueryString = """
            INSERT INTO company (name,equity) VALUES ('{}','{}');
            """.format(cname, cequity)
            cur1.execute(cqueryString)
            db.connection.commit()

        if (uname != '' and ubudget_from_edu != ''):
            uqueryString = """
            INSERT INTO university (name,budget_from_edu) VALUES ('{}','{}');
            """.format(uname, ubudget_from_edu)
            cur1.execute(uqueryString)
            db.connection.commit()

        if (rcname != '' and rcbudget_from_edu != '' and rcbudget_from_priv != ''):
            rcqueryString = """
            INSERT INTO research_center (name,budget_from_edu,budget_from_priv) VALUES ('{}','{}','{}');
            """.format(rcname, rcbudget_from_edu, rcbudget_from_priv)
            cur1.execute(rcqueryString)
            db.connection.commit()
            cur1.close

        if (dtitle != '' and dsummary != '' and dtitle_project != '' and ddue_date != ''):
            dqueryString = """
            INSERT INTO deliverable (title,summary,title_project,due_date) VALUES ('{}','{}','{}','{}');
            """.format(dtitle, dsummary, dtitle_project, ddue_date)
            cur1.execute(dqueryString)
            db.connection.commit()

        if (sname != '' ):
            squeryString = """
            INSERT INTO scientific_field (name) VALUES ('{}');
            """.format(sname)
            cur1.execute(squeryString)
            db.connection.commit()

        if (fname != '' and ftitle != '' ):
            fqueryString = """
            INSERT INTO fieldthatdescribes (name,title) VALUES ('{}','{}');
            """.format(fname, ftitle)
            cur1.execute(fqueryString)
            db.connection.commit()

        if (wtitle != '' and wid != '' ):
            wqueryString = """
            worksfor (title,id) VALUES ('{}','{}');
            """.format(fname, ftitle)
            cur1.execute(wqueryString)
            db.connection.commit()
    return render_template('create_entry.html', queryString=queryString, errorprogram=errorprogram, cnames=cnames, dtitle_projects=dtitle_projects, fnames=fnames, ftitles=ftitles, pfrom_orgs=pfrom_orgs, pevaluated_froms=pevaluated_froms, pnames=pnames, rnames=rnames, wids=wids, wtitles=wtitles, unames=unames, rcnames=rcnames, phnames=phnames)

@app.route("/update_entry")
def update_entry():
    return render_template('update_entry.html')

@app.route("/delete_entry")
def delete_entry():
    return render_template('delete_entry.html')

#END OF CRUD

if __name__ == '__main__':
    app.run(debug=True)
