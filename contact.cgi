#!/usr/bin/python3

import cgi
import cgitb
import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
from email.mime.base import MIMEBase 
from email import encoders 

#to show common error in browser
cgitb.enable()
print("Content-type:text/html")
print("")

webdata=cgi.FieldStorage() #this is collect all teh html codes with data
#now extracting the values from webpage
nAme=webdata.getvalue("name")
emid=webdata.getvalue("eid")
num=webdata.getvalue("pno")
messag=webdata.getvalue("msg")


#user info sender to receiver
email_user = 'cachecoders@gmail.com' 
email_password = 'Pass-1234' 
email_send = 'hsinha177@gmail.com' 
subject = 'Message from cache coders' 

#message format
msg = MIMEMultipart() 
msg['From'] = email_user 
msg['To'] = email_send 
msg['Subject'] = subject 
body = (nAme+emid+messag)

msg.attach(MIMEText(body,'plain')) 
#attachment of file
f=open("dock.txt","w+")
f.write("You have received a contact request from : "+nAme)
f.write("\nEmail is : "+emid)
f.write("\nMessage : "+messag)
f.write("\nPhone no. : ")
f.write(num)
f.close()

filename='dock.txt'

attachment =open(filename,'rb') 
part = MIMEBase('application','octet-stream') 
part.set_payload((attachment).read()) 
encoders.encode_base64(part) 
part.add_header('Content-Disposition',"attachment; filename= "+filename) 
msg.attach(part)

#converting msg as string type
text=msg.as_string()

#protocols to send over smtp 
server = smtplib.SMTP('smtp.gmail.com',587) 
server.starttls() 
server.login(email_user,email_password) 
server.sendmail(email_user,email_send,text) 
server.quit() 
