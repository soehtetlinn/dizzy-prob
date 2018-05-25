import fdb
con = fdb.connect(host='localhost', database='/var/lib/firebird/2.5/data/first_database.fdb',user='sysdba',password='1996dec17')
cur = con.cursor()
newLanguages = [
    ('Lisp',1958),
    ('Dylan',1995),
    ]
cur.executemany("insert into frompython(name,year_released) values (?,?)", newLanguages)
con.commit()

