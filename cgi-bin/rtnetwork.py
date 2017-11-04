#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Import modules for CGI handling and UTF-8 handling of input/output
import cgi, cgitb
import sys
import re
import os
import pandas as pd
import networkx as nx
from werkzeug import secure_filename
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)
form = cgi.FieldStorage()
import time

def printpage():
    print("content-type:text/html; charset=utf-8\r\n\r\n")
    print()
    print('''
        <!DOCTYPE html>
        <html lang="sv">

          <head>

            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <meta name="description" content="">
            <meta name="author" content="">

            <title>Digitala metoder</title>

                <!-- Bootstrap core CSS -->
                <link href="http://digitalametoder.science/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

                <!-- Custom styles for this template -->
                <link href="http://digitalametoder.science/css/3-col-portfolio.css" rel="stylesheet">

              </head>

              <body>
    <div id="container">
     <main>
        <h1>Skapa RT-nätverk</h1>
        <p>För instruktioner, se <a href="https://youtu.be/Dfz9e0KOzCU">denna video</a></p>
	<p><b>OBS: filnamnen får inte innehålla specialtecken</b>. Godkänt filnamn är ex. <code>fil.csv</code>. Välj gärna ett unikt och specifikt filnamn, ex. <code>christophersdata.csv</code></p>
        <p>Exportera till csv fil i Google Calc/TAGS och ladda upp:</p>
        <form enctype="multipart/form-data"
                         action="rtnetwork.py" method="post">
         <br><input type="file" name="filename" />
         <input type="submit" value="Ladda upp" />

        <br><br>

        <p>Om du har fått en .csv-fil av Christoher, ladda upp här:</p>
        <form enctype="multipart/form-data"
                         action="rtnetwork.py" method="post">
         <br><input type="file" name="filename2" />
         <input type="submit" value="Ladda upp" />

         <br><br>
         <p>Källkoden till detta verktyg finns <a href="https://github.com/christopherkullenberg/digitalametoder.science/blob/master/cgi-bin/rtnetwork.py">här</a>.</p>
        <br>
        </section>
     </main>
   </div>

    ''')

def openfile():
    # Get filename here.
    fileitem = form['filename']
    fileitem2 = form['filename2']

    fn = secure_filename(fileitem.filename)
    fn2 = secure_filename(fileitem2.filename)

    # Test if the file was uploaded
    try:
        if fileitem.filename:
            open('upload/' + fn, 'wb').write(fileitem.file.read())
            fn = os.path.basename(fileitem.filename.replace(' ', '-'))
            #fn = secure_filename(fn)
            df = pd.read_csv('upload/' + fn)
            printpage()
            #print("Antal rader i filen: " + str(len(df)))
            G = nx.DiGraph()
            for tweet in df.iterrows():
                if tweet[1][2].startswith("RT"):
                    #print("source: " + tweet[1][1] + "<br>")

                    match = re.findall("(?<=RT\s\@).*?(?=\:)", tweet[1][2], re.IGNORECASE)
                    if match:
                        #print(match[0] + "<br>---<br>")
                        G.add_edge(tweet[1][1], match[0])
            filename = str(time.time())
            nx.write_gexf(G, "/home/chrisk/digitalametoder.science/results/" + filename + ".gexf")
            print('''Nätverksfilen för RT-network kan laddas ned <a href="http://digitalametoder.science/results/''' + filename + '''.gexf">här</a> (högerklicka och välj "spara som")  och sedan öppnas med Gephi.''')

        elif fileitem2.filename:
            open('upload/' + fn2, 'wb').write(fileitem2.file.read())
            fn2 = os.path.basename(fileitem2.filename.replace(' ', '-'))
            df = pd.read_csv('upload/' + fn2)
            printpage()
            G = nx.DiGraph()
            for tweet in df.iterrows():
                #print("source: " + str(tweet[1][3]))
                if tweet[1][6].startswith("RT"):
                    #print("target: " + tweet[1][6] + "<br>")

                    match = re.findall("(?<=RT\s\@).*?(?=\:)", tweet[1][6], re.IGNORECASE)
                    if match:
                        #print(match[0] + "<br>---<br>")
                        G.add_edge(tweet[1][3], match[0])
            filename = str(time.time())
            nx.write_gexf(G, "/home/chrisk/digitalametoder.science/results/" + filename + ".gexf")
            print('''Nätverksfilen för RT-network kan laddas ned <a href="http://digitalametoder.science/results/''' + filename + '''.gexf">här</a> (högerklicka och välj "spara som")  och sedan öppnas med Gephi.''')

        else:
            printpage()
            print('<p>Ingen fil valdes.</p>')

    except UnicodeError:
        print("<p>Filen har inte korrekt teckenkodning. Testa att spara om med Unicode / UTF-8.</p>")

## GET TEXT FROM FORM
# Create instance of FieldStorage
try:
    #form = cgi.FieldStorage()
    openfile()
except KeyError:
    printpage()
    sys.exit()

print("</body></html>")
