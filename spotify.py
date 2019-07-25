#!/usr/bin/python3

import cgi
import cgitb   
#cgitb --> cgi traceback to see error in the browser instead of going to os for troubleshoot
import time
import webbrowser
#to show common error in webbrowser
#cgitb.enable()

print("Content-type:text/html")
print("")

import urllib3
f = open("url.txt",'r') 
f.seek(0)
url=f.read()

#http = urllib3.PoolManager()
#r = http.request('GET', myurl)

print("<html> <head> <title>Search Results</title></head>")
print("<body style='background: rgba(233, 237, 123, 0.87); font-size: 18px;'>")
print("<h2>Play your song with spotify </h2>")
print("<br>")
print("<pre>")
print("<a href= "+url+" target='_blank'>")
print("Click to go")
print("</a>")
print("</pre>")
print("</body></html>")

print("<meta http-equiv='refresh' content='15;url=https://13.233.28.221/index.html'>")
