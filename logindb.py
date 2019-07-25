#!/usr/bin/python3

import cgi	#for connecting webpage
import cgitb	#for gathering any error info
import mysql.connector	#mysql connection
import datetime
current_value="uname"
cgitb.enable() 		#gathering error info

def update_value(uname):
	global current_value
	current_value = uname

print("Content-type:text/html")	#information about the type of content it will read
print("")

webdata=cgi.FieldStorage()

eid=webdata.getvalue("email")	#fetching email from input variable
paswd=webdata.getvalue("pwd")	#fetching password from input variable

now = datetime.datetime.now()
ctime=now.strftime("%Y-%m-%d %H:%M:%S")
cng=str(eid)
name = cng.split("@")[0]

update_value(name)
f = open("login_time.txt","w")
f.write(ctime)
f.close()
fp = open("uname.txt","w")
fp.write(name)
f.close()

conn = mysql.connector.connect(host='localhost',user='root',passwd='root',database='reko')	
#establishing connection with server
mycursor=conn.cursor()
mycursor.execute("select email from user where email='%s'"%(eid))
usercheck=mycursor.fetchone()
mycursor2=conn.cursor()
mycursor2.execute("select pass from user where pass='%s'"%(paswd))
passcheck=mycursor2.fetchone()
try:
	if eid == usercheck[0] and paswd == passcheck[0]:
		print("<meta http-equiv='refresh' content='0;url=https://13.233.28.221/index.php'>")
		connect=mysql.connector.connect(host="localhost",user="root",passwd="root",database="reko")
		mycur=connect.cursor()
		mycur.execute("insert into %s(uname,login_time) values('%s','%s')"%(name,name,ctime))
		connect.commit()
		conn.close()

except:
	print("Account Doesn't exist!")
	print("<meta http-equiv='refresh' content='3;url=https://13.233.28.221/new_account.html'>")
conn.close()
