import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")
conn=sqlite3.connect("cgi-bin/empdetails.db")
cur=conn.cursor()
form=cgi.FieldStorage()
rno=form.getvalue("rno")
query="select * from employee where rno=?"
try:
	cur.execute(query,(rno,))
except Exception as e:
	print(e)
else:
        
	for record in cur:
		pass
	html='''<html>
	<body>
	<form action="update.py" method="PUT">
	<input type="text" value="%s" name="rno"><br/>
	<input type="text" value="%s" name="name"><br/>
	<input type="text" value="%s" name="dept"><br/>
	<input type="submit" value="Update" >
	</form>
	</body>
	</html>'''%(str(record[0]),record[1],record[2])
	print(html)
finally:
	conn.close()
	#cur.close()
