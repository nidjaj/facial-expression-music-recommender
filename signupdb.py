#!/usr/bin/python3

import cgi
import cgitb
import mysql.connector

cgitb.enable()

print("Content-type:text/html")
print("")

webdata=cgi.FieldStorage()

eid=webdata.getvalue("email")
paswd=webdata.getvalue("pwd")
paswd1=webdata.getvalue("pwd-repeat")

name = eid.split("@")[0]

if paswd == paswd1 :
	conn=mysql.connector.connect(host="localhost",user="root",passwd="root",database="reko")
	mycursor=conn.cursor()
	mycursor.execute("insert into user values('%s','%s')"%(eid,paswd))
	conn.commit()

	mydb=mysql.connector.connect(host="localhost", user="root",passwd="root",database="reko")
	mycursor=mydb.cursor()
	mycursor.execute("create table %s(login_time varchar(20),logout_time varchar(20),imageid varchar(20),sentiment varchar(20))"%(name))
	mydb.commit()
	print("user signup successful. ':)'")
	conn.close()
	mydb.close()
	print("<meta http-equiv='refresh' content='2;url=https://13.233.28.221/mylogin.html'>")
else :
	print("password not matched")
	print("<meta http-equiv='refresh' content='2;url=https://13.233.28.221/new_account.html'>")
