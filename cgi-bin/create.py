import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")

conn=sqlite3.connect("empdetails.db")
cur=conn.cursor()
query="create table employee(rno text,name text,dept text)"
try:
    cur.execute(query)
except Exception as e:
    print(e)
else:
    conn.commit()
    print("created employee table successfully")
finally:
    conn.close()
    
