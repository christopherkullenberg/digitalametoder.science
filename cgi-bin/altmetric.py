#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
Documentation for the Altmetric api: https://api.altmetric.com/
Example json: https://api.altmetric.com/v1/doi/10.1371/journal.pone.0147152
'''

import cgi
import sys
import os
import pandas as pd
from werkzeug import secure_filename
import time
import datetime
from printhtml import printaltmetric
import requests
import json
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)
form = cgi.FieldStorage()
filename = str(time.time())
with open("/home/chrisk/apikey.txt") as apifile:
    apikey = apifile.read()


def openfile():
    # Get filename here.
    fileitem = form['filename']
    fileitem2 = form['filename2']
    fileitem3 = form['filename3']
    fn = secure_filename(fileitem.filename)
    fn2 = secure_filename(fileitem2.filename)
    fn3 = secure_filename(fileitem3.filename)
    # Test if the file was uploaded
    try:
        if fileitem.filename:
            wosdois = []
            open('upload/' + fn, 'wb').write(fileitem.file.read())
            fn = os.path.basename(fileitem.filename.replace(' ', '-'))
            # fn = secure_filename(fn)
            dfwos = pd.read_csv('upload/' + fn, sep="\t")
            printaltmetric()
            for d in dfwos.iterrows():
                if type(d[1][53]) == float:
                    continue
                else:
                    wosdois.append(d[1][53])
            print("<p>The original file length: " + str(len(dfwos)) + "</p>")
            print("<p>Extracted DOIs: " + str(len(wosdois)) + "</p>")
            print('''<p>Now attempting to contact the Altmetric API...
                  please be patient.</p>''')
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

            print("<p>The original file length: " + str(len(dfscopus))
                  + "</p>")
            print("<p>Extracted DOIs: " + str(len(scopusdois)) + "</p>")
            print('''<p>Now attempting to contact the Altmetric API...
                  please be patient.</p>''')
            return(scopusdois)

        elif fileitem3.filename:
            plaintextdois = []
            open('upload/' + fn3, 'wb').write(fileitem3.file.read())
            fn3 = os.path.basename(fileitem3.filename.replace(' ', '-'))
            dois = open('upload/' + fn3, "r")
            listofdois = dois.readlines()
            printaltmetric()
            for line in listofdois:
                plaintextdois.append(line[:-1])  # -2 removes \n
                # print(line)
            print("<p>Number of DOIs in file: " + str(len(plaintextdois))
                  + "</p>")
            print('''<p>Now attempting to contact the Altmetric API...
                  please be patient.</p>''')
            # print(plaintextdois[0:10])
            return(plaintextdois)

        else:
            printaltmetric()
            print('<p>Ingen fil valdes.</p>')
    except UnicodeError:
        print('''<p>Filen har inte korrekt teckenkodning.
              Testa att spara om med Unicode / UTF-8.</p>''')


def builddf(filename):
    df = pd.DataFrame(columns=["Title", "Date", "DOI", "URL", "AltmetricURL",
                      "Tweets", "Wikipedia", "MSM", "Score"])
    skipped = 0
    try:
        for DOI in openfile()[0:150]:
            datadict = {}
            webcontent = requests.get('https://api.altmetric.com/v1/doi/' +
                                      DOI + "?key=" + apikey)
            #  print(webcontent)
            try:
                jsonobject = webcontent.json()
            except json.JSONDecodeError:
                skipped += 1
                continue
            #  print(jsonobject)
            try:
                datadict['Title'] = jsonobject['title']
                try:
                    datadict['Date'] = datetime.datetime.fromtimestamp(jsonobject['published_on'])
                except KeyError:
                    datadict['Date'] = 0
                datadict['DOI'] = jsonobject['doi']
                datadict['Score'] = jsonobject['score']
                datadict['URL'] = "https://dx.doi.org/" + jsonobject['doi']
                datadict['AltmetricURL'] = jsonobject['details_url']
                try:
                    datadict['Wikipedia'] = jsonobject['cited_by_wikipedia_count']
                except KeyError:
                    datadict['Wikipedia'] = 0
                try:
                    datadict['Tweets'] = jsonobject['cited_by_tweeters_count']
                except KeyError:
                    datadict['Tweets'] = 0
                try:
                    datadict['MSM'] = jsonobject['cited_by_msm_count']
                except KeyError:
                    datadict['MSM'] = 0
                try:
                    datadict['Videos'] = jsonobject['cited_by_videos_count']
                except KeyError:
                    datadict['Videos'] = 0


                df = df.append(datadict, ignore_index=True)

            except KeyError:
                skipped += 1
                continue
    except KeyError:
        printaltmetric()
        sys.exit()
    df.to_excel("/home/chrisk/digitalametoder.science/results/" +
                filename + ".xlsx")
    print("<p>" + str(skipped) +
          " DOIs had no matches in the Altmetric database</p>")
    print("<p>" + str(len(df)) +
          " Altmetric scores were written to file.</p>")
    print('''<p>The file can be downloaded
          <a href="http://digitalametoder.science/results/''' + filename +
          '''.xlsx">here</a> and be opened with a spreadsheet
          application.</p>''')
#  get timestamped filename


builddf(filename)

print("</body></html>")
