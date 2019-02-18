import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")

conn=sqlite3.connect("cgi-bin/empdetails.db")
cur=conn.cursor()

form=cgi.FieldStorage()
rno=form.getvalue("rno")
name=form.getvalue("name")
dept=form.getvalue("dept")
print(rno,name,dept)

sql="insert into employee values(?,?,?)"


try:
    rs=cur.execute(sql,(rno,name,dept))
except Exception as e:
    print(e)
else:
    conn.commit()
    print("succesfully inserted")
finally:
    cur.close()
    conn.close()
