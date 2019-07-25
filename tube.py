#!/usr/bin/python3

import cgi
import cgitb   
#cgitb --> cgi traceback to see error in the browser instead of going to os for troubleshoot
import subprocess
#import youtube
import pandas as pd
import re
from itertools import islice
#to show common error in webbrowser
cgitb.enable()

print("Content-type:text/html")
print("")

import webbrowser,time

print("<html>")
print(" <head> <title>Search Results</title></head>")
print("<body style='background: rgba(233, 237, 123, 0.87); font-size: 18px;'>")
print("<h2>Your Top Songs</h2>")

filename = "songlist.txt"
number_of_lines = 5
# open the file for reading
#filehandle = open(filename, 'r')  
#while True:  
	# read a single line
#	line = filehandle.readline()
#	if not line:
#		break
with open(filename, 'r') as input_file: 
	input_file.seek(0)  
	lines_cache = islice(input_file, number_of_lines)
	for line in lines_cache:
		print(line)
		print("<pre>")
		print("<a href= https://www.youtube.com/results?search_query="+line+">")
		print(line)
		print("</a>")
		print("</pre>")
print("</body></html>")

print("<meta http-equiv='refresh' content='30;url=https://13.233.28.221/index.html'>") 	
