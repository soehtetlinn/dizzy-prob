import fdb
import string
import random
import sys
min_char = 8
max_char = 12
i = 101
allchar = string.ascii_letters
allnum = string.digits
con = fdb.connect(host='localhost',database='/var/lib/firebird/2.5/data/employee.fdb', user = 'SYSDBA', password = '1996dec17')
cur = con.cursor()
while i < 100000:
    name = "".join(random.choice(allchar) for x in range(8))
    price = random.randint(100,1100)
    print name
    print price
    cur.execute("INSERT INTO Products(Id, Name, Price) VALUES(?,?,?)",(i,name,price))	
    i = i + 1
    con.commit()
