#!/usr/bin/python3
import webbrowser
import sentimentAnalysing as senti
import pandas as pd


value = senti.current_ytvalue

#song=""
#curr_song = pd.core.series.Series(song)
#valuesong=pd.DataFrame(value)
#valuesong.to_csv("newww.csv")
#def update_song(val):
#        global curr_song
#        curr_song = val

f = open("songlist.txt", "w")
for i in range(len(value)):
	name = str(value[i])
	#update_song(value)
	f.write(name+"\n")

	
