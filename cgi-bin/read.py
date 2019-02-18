import sqlite3
print("Content-Type:text/html\r\n\r\n")
conn=sqlite3.connect("cgi-bin/empdetails.db")
cur=conn.cursor()
query="select * from employee"
html='''
<html>
<body>
<table border=2>
'''
print(html)
try:
	rs=cur.execute(query)
except Exception as e:
	print(e)
else:
	for record in cur:
		print("<tr>")
		for column in record:
			print("<td>"+str(column)+"</td>")
		print("</tr>")
	html='''
	</table>
</body>
</html>
	'''
finally:
        cur.close()
        conn.close()
