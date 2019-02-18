import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")

conn=sqlite3.connect("cgi-bin/empdetails.db")
cur=conn.cursor()

form=cgi.FieldStorage()
rno=form.getvalue("rno")
name=form.getvalue("name")
dept=form.getvalue("dept")
print(rno,name,dept)

query="update employee SET dept=?,name=? where rno=?"


try:
    rs=cur.execute(query,(dept,name,rno))
    conn.commit()
except Exception as e:
    print('failure')
    print(e)
else:
    print("updated succesfully")
finally:
    conn.close()
#cur.close()
    
