def create_entry():
    queryString = ''
    oqueryString = ''
    rqueryString = ''
    rcqueryString = ''
    uqueryString = ''
    cqueryString = ''
    pqueryString = ''
    squeryString = ''
    queryString = ''
    if request.method == 'POST':
        cur1 = db.connection.cursor()
        pname = str(request.form.get('inputname'))
        paddress = str(request.form.get('inputaddress'))

        oname = str(request.form.get('inputoname'))
        oinitials = str(request.form.get('inputoinitials'))
        opostal_code = str(request.form.get('inputopostal_code'))
        ostreet = str(request.form.get('inputostreet'))
        ocity = str(request.form.get('inputocity'))

        rid = str(request.form.get('rid'))
        rfirst_name = str(request.form.get('rfirst_name'))
        rlast_name = str(request.form.get('rlast_name'))
        rsex = str(request.form.get('rsex'))
        rbirhtdate = str(request.form.get('rbirthdate'))
        rname = str(request.form.get('rname'))
        rworks_since = str(request.form.get('rworks_since'))







        if (pname != 'None' and paddress != 'None'):
             queryString = """
             INSERT INTO program (name,address) VALUES ('{}','{}');
             """.format(pname, paddress)
        cur1.execute(queryString)
        db.connection.commit()
        cur1.close

    
    
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

    return render_template('create_entry.html', queryString=queryString)