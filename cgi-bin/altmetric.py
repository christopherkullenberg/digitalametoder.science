#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''Documentation for the Altmetric api: https://api.altmetric.com/'''

import cgi
import cgitb
import sys
import re
import os
import pandas as pd
#import networkx as nx
from werkzeug import secure_filename
import time
from printhtml import printaltmetric
import math
import requests
import json
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)
form = cgi.FieldStorage()



'''
def callaltmetric(listofdois):
    # Initialize a pandas dataframe with the correct columns
    df = pd.DataFrame(columns=["Title", "DOI", "URL", "AltmetricURL", "Score"])
    for DOI in listofdois[0:9]:
        webcontent = requests.get('https://api.altmetric.com/v1/doi/' + DOI)
        try:
            jsonobject = webcontent.json()
            try:
                df = df.append({
                 "Title": jsonobject['title'],
                 "DOI":  jsonobject['doi'],
                 "URL": "https://dx.doi.org/" + jsonobject['doi'],
                 "Score": jsonobject['score'],
                "AltmetricURL": jsonobject['details_url']
                  }, ignore_index=True)
             except KeyError:
                 print("<p>KeyError, Skipping this piece</p>")
                 continue
         except json.JSONDecodeError:
            print("The article " + DOI + " was not in Altmetrics database")
            continue
'''




def openfile():
    # Get filename here.
    fileitem = form['filename']
    fileitem2 = form['filename2']
    fn = secure_filename(fileitem.filename)
    fn2 = secure_filename(fileitem2.filename)
    # Test if the file was uploaded
    try:
        if fileitem.filename:
            wosdois = []
            open('upload/' + fn, 'wb').write(fileitem.file.read())
            fn = os.path.basename(fileitem.filename.replace(' ', '-'))
            #fn = secure_filename(fn)
            dfwos = pd.read_csv('upload/' + fn, sep="\t")
            printaltmetric()
            for d in dfwos.iterrows():
                if type(d[1][53]) == float:
                    continue
                else:
                    wosdois.append(d[1][53])
            print("<p>The original file length: " + str(len(dfwos)) + "</p>")
            print("<p>Extracted DOIs: " + str(len(wosdois)) + "</p>")
            print("<p>Now attempting to contact the Altmetric API... please be patient.</p>")
            return(wosdois)

        elif fileitem2.filename:
            scopusdois = []
            open('upload/' + fn2, 'wb').write(fileitem2.file.read())
            fn2 = os.path.basename(fileitem2.filename.replace(' ', '-'))
            dfscopus = pd.read_csv('upload/' + fn2)
            printaltmetric()
            for d in dfscopus.iterrows():
                if type(d[1][11]) == float:
                    continue
                else:
                    scopusdois.append(d[1][11])

            print("<p>The original file length: " + str(len(dfscopus)) + "</p>")
            print("<p>Extracted DOIs: " + str(len(scopusdois)) + "</p>")
            print("<p>Now attempting to contact the Altmetric API... please be patient.</p>")
            return(scopusdois)
        else:
            printaltmetric()
            print('<p>Ingen fil valdes.</p>')
    except UnicodeError:
        print("<p>Filen har inte korrekt teckenkodning. Testa att spara om med Unicode / UTF-8.</p>")

'''
try:
    callaltmetric(openfile())
except KeyError:
    printaltmetric()
    sys.exit()
'''

df = pd.DataFrame(columns=["Title", "DOI", "URL", "AltmetricURL", "Score"])

for DOI in openfile()[0:100]:

    webcontent = requests.get('https://api.altmetric.com/v1/doi/' + DOI)
    try:
        jsonobject = webcontent.json()
    except json.JSONDecodeError:
        print("Not in Altmetrics database")
        continue
    print(jsonobject)
    try:
        #print(jsonobject['title'])
        #print(jsonobject['doi'])
        #print(jsonobject['cited_by_posts_count'])
        #print(jsonobject['cited_by_msm_count'])
        #print(jsonobject['cited_by_feeds_count'])
        #print(jsonobject['cited_by_tweeters_count'])
        #print(jsonobject['cited_by_fbwalls_count'])
        #print(jsonobject['cited_by_wikipedia_count'])
        #print(jsonobject['cited_by_gplus_count'])
        #print(jsonobject['cited_by_rdts_count'])
        #print(jsonobject['cited_by_videos_count'])
        #print(jsonobject['cited_by_accounts_count'])
        #print(jsonobject['score'])
        df = df.append({
         "Title": jsonobject['title'],
         "DOI":  jsonobject['doi'],
         #"Tweets": jsonobject['cited_by_tweeters_count'],
         "URL": "https://dx.doi.org/" + jsonobject['doi'],
         "Score": jsonobject['score'],
        "AltmetricURL": jsonobject['details_url']
          }, ignore_index=True)
    except KeyError:
        print("No data, Skipping this piece")
        continue

df.to_excel("/home/chrisk/digitalametoder.science/results/test2.xlsx")
print('''Nätverksfilen för RT-network kan laddas ned <a href="http://digitalametoder.science/results/test2.xlsx">här</a> (högerklicka och välj "spara som")  och sedan öppnas med Excel.''')






print("</body></html>")
