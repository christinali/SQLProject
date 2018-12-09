strInput = """
    if 'cz' in needed:
        currClasses = db.session.query(models.Class).filter_by(cz=1).all()
        for currClass in currClasses:
            if currClass not in classes:
                classes[currClass] = list()
            classes[currClass].append('cz')"""

treqs =['cz', 'ss','cci','alp','ns','qs','ei','fl','r','sts','w']

for treq in treqs:
    print(strInput.replace("cz",treq))