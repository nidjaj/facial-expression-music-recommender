#!/usr/bin/python3

import mysql.connector


fp = open("label.txt","r")
label = fp.read()
fp.close()
f = open("/var/www/html/imageid.txt","r")
imageid = f.read()
f.close()
imgpath = "/cgi-bin/snaps/"+imageid
fptr = open("login_time.txt","r")
login_time = fptr.read()
fptr.close()
p = open("uname.txt","r")
name = p.read()
p.close()

newtable = name+label

connect=mysql.connector.connect(host="localhost",user="root",passwd="root",database="reko")
mycur=connect.cursor()
#mycur.execute("insert into %s(imageid,sentiment) values('%s','%s')"%(name,imageid,label))
mycur.execute("update %s set imageid='%s', sentiment='%s' where login_time='%s'"%(name,imageid,label,login_time))
connect.commit()
connect.close()

mydb=mysql.connector.connect(host="localhost", user="root",passwd="root",database="reko")
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS %s(login_time varchar(20),songname varchar(20))"%(newtable))
mydb.commit()
#print("user signup successful. ':)'")
mydb.close()

#print("<meta http-equiv='refresh' content='0;url=https://13.233.28.221/index.php'>")
