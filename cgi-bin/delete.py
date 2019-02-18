import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")

conn=sqlite3.connect("cgi-bin/data.db")
cur=conn.cursor()

form=cgi.FieldStorage()
rno=form.getvalue("rno")
query="delete from emp where rno="+rno

try:
    cur.execute(query)
except Exception as e:
    print(e)
else:
    conn.commit()
    print("deleted successfully")
finally:
    cur.close()
    conn.close()
