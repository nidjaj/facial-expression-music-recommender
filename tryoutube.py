#!/usr/bin/python3

import cgi
import cgitb   #cgitb --> cgi traceback to see error in the browser instead of going to os for troubleshoot
import subprocess
import time
#to show common error in webbrowser
cgitb.enable()

print("Content-type:text/html")
print("")

webdata=cgi.FieldStorage() #this is collect all the html code with data
#now extracting value of x
data = webdata.getvalue('search')
#sending output of client via web server
#op=subprocess.getoutput(data)
#print("<pre>")
#print(op)
#print("</pre>")

#pgm to search a key entered by user
#by keyboard input

import webbrowser,time
from googlesearch import search


links=[]
for i in search(data,stop=10):
        links.append(i)

f=open("search_results_url.txt","w+")
f.write(data+"\n\n")
for i in links :
        f.write(i+"\n")
f.close()

print("<html> <head> <title>Search Results</title></head>")
print("<body style='background: rgba(233, 237, 123, 0.87); font-size: 18px;'>")
print("<h2>Top 10 links for : "+data+"</h2>")
print("<br>")
for i in links :
	print("<pre>")
	print(i)
	print("<a href= "+i+" target='_blank'>")
	print("Click to go")
	print("</a>")
	print("</pre>")
print("</body></html>")

print("<meta http-equiv='refresh' content='15;url=https://13.233.28.221/index.html'>") 	
