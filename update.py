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
             UPDATE program SET address = '{}' WHERE name = '{}';
             """.format(praddress,prname)
             cur1.execute(queryString)
             db.connection.commit()
        else:
            errorprogram="Field is required"

        if (oname != '' and oinitials  != '' and opostal_code != '' and ostreet != '' and  ocity != ''):
             oqueryString = """
             UPDATE organization SET initials = '{}', postal_code = '{}', street = '{}', city = '{}' WHERE name = '{}';
             """.format(oinitials, opostal_code, ostreet, ocity,oname)
             cur1.execute(oqueryString)
             db.connection.commit()
        else:
            errorprogram="Field is required"

        if (rid != '' and rfirst_name != '' and rlast_name != '' and rsex != '' and rbirthdate != '' and rname != '' and rworks_since):
             rqueryString = """
             UPDATE researcher SET first_name = '{}', last_name = '{}', sex = '{}', birthdate = '{}' , works_since = '{}' WHERE id = '{}';
             """.format(rfirst_name, rlast_name, rsex, rbirthdate, rname, rworks_since,rid)
             cur1.execute(rqueryString)
             db.connection.commit()
        else:
            errorprogram="Field is required"

        if (ptitle != '' and pamount != '' and psummary != '' and pstart_date != '' and pend_date != '' and pname != '' and pfrom_org != '' and pevaluated_from != '' and pexec != '' and pgrade != '' and pdate_of_eval != ''):
            pqueryString = """
           update project set amount = '{}', summary = '{}', start_date = '{}', end_date = '{}', grade = '{}', date_of_eval = '{}', exec = '{}' where title = '{}';
            """.format(pamount, psummary, pstart_date, pend_date, pname, pevaluated_from, pfrom_org, pgrade, pdate_of_eval, pexec,ptitle)
            cur1.execute(pqueryString)
            db.connection.commit()
        else:
            errorprogram="Field is required"

        if (phname != '' and phphone != '' ):
             phqueryString = """
             UPDATE phone SET phone = '{}' WHERE name = '{}';
             """.format(phphone,phname)
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