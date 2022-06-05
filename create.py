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








    return render_template('create_entry.html', queryString=queryString)