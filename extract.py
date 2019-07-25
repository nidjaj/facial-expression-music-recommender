#!/usr/bin/python3

import cgi
import cgitb

cgitb.enable()

print("Context-type:text/html")
print("")

webdata=cgi.FieldStorage()

img=webdata.getvalue("href")

print(img)
