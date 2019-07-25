#!/usr/bin/python3
import datetime
import mysql.connector

now = datetime.datetime.now()
ctime=now.strftime("%Y-%m-%d %H:%M:%S")
recipient=input("Enter your email : ")
name = recipient.split("@")[0]
print(name)

mydb=mysql.connector.connect(host="localhost", user="root",passwd="root",database="reko")
mycursor=mydb.cursor()
mycursor.execute("create table %s(uname varchar(20),login_time varchar(20),logout_time varchar(20),sentiment varchar(20))"%(name))
mydb.commit()
conn=mysql.connector.connect(host="localhost",user="root",passwd="root",database="reko")
mycursor=conn.cursor()
mycursor.execute("insert into %s(uname,login_time) values('%s','%s')"%(name,name,ctime))
conn.commit()
conn.close()

print("Table successfully created")
mydb.close()
