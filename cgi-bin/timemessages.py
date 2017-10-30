#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Import modules for CGI handling and UTF-8 handling of input/output
import cgi, cgitb
import sys
import re
import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from werkzeug import secure_filename
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)
form = cgi.FieldStorage()
import time

def parsetags(filename):
    df = pd.read_csv(filename) # TAGS file
    pd.created_at = pd.to_datetime(df.post_published_sql,
                                   format='%Y-%m-%d %H:%M:%S')
    df.index = pd.created_at
    #df.head()
    return(df)

def parsenetvizz(filename):
    df = pd.read_csv(filename, sep=";") # Netvizz file
    pd.created_at = pd.to_datetime(df.post_published_sql,
                                   format='%Y-%m-%d %H:%M:%S')
    df.index = pd.created_at
    #df.head()
    return(df)

def messagesperday(dataframe):
    messagesperday = dataframe.resample('D').count()

    fig = plt.figure(figsize=(15,7))
    ax = fig.add_subplot(111)

    plt.title('Meddelanden per dag', size=16)

    messagesperday['post_id'].plot() #Plot each individual message per day

    plt.xlabel('Datum')
    plt.ylabel('Meddelanden')
    novelfilename = str(time.time())
    plt.savefig("../results/" + str(novelfilename) + "perday.png")
    return(str(novelfilename))
    #plt.show()

def messagesperhour(dataframe):
    hours = dataframe.index.hour
    hours.mean()
    fig = plt.figure(figsize=(15,7))
    ax = fig.add_subplot(111)

    plt.title('Meddelanden per timme', size=16)

    plt.plot(hours, 'ro') #Plot each individual message per day

    plt.xlabel('Meddelande')
    plt.ylabel('Klockslag')
    novelfilename = str(time.time())
    plt.savefig("../results/" + str(novelfilename) + "perhour.png")
    return(str(novelfilename))
    #plt.show()

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
        <h1>Analysera meddelandens tidsstämplar</h1>
        <!-- <p>För instruktioner, se <a href="https://youtu.be/Dfz9e0KOzCU">denna video</a></p> -->
	<p><b>OBS: filnamnen får inte innehålla specialtecken</b>.<br> Godkänt filnamn är ex. <code>fil.csv</code>.
    <br>Välj gärna ett unikt och specifikt filnamn, ex. <code>christophersdata.csv</code></p>
        <h3>A. Twitter/TAGS</h3>
        <p>Exportera till csv-fil i Google Calc/TAGS och ladda upp:</p>
        <form enctype="multipart/form-data"
                         action="timemessages.py" method="post">
         <br><input type="file" name="filename" />
         <input type="submit" value="Ladda upp" />

        <br><br>

        <h3>B. Facebook/Netvizz</h3>
        <p>Om du har en csv-fil som samlats in med Netvizz, ladda upp här:</p>
        <form enctype="multipart/form-data"
                         action="timemessages.py" method="post">
         <br><input type="file" name="filename2" />
         <input type="submit" value="Ladda upp" />



        <br>
        </section>
     </main>
   </div>

    ''')

def openfile():
    # Get filename here.

    fileitem = form['filename'] # Tags data
    fileitem2 = form['filename2'] # Netvizz data

    fn = secure_filename(fileitem.filename)
    fn2 = secure_filename(fileitem2.filename)

    # Test if the file was uploaded
    try:
        if fileitem.filename:
            printpage()
            open("upload/" + fn, "wb").write(fileitem.file.read())
            fileitem = os.path.basename(fileitem.filename.replace(' ', '-'))
            print('''
                Meddelanden per dag: <a href="http://digitalametoder.science/results/'''
                + messagesperday(parsetags("upload/" + fileitem)) + '''perday.png">
                här</a> (högerklicka och välj "spara som")
                <br>
                Meddelanden per timme: <a href="http://digitalametoder.science/results/'''
                + messagesperhour(parsetags("upload/" + fileitem)) + '''perhour.png">
                här</a> (högerklicka och välj "spara som")
                ''')

        elif fileitem2.filename:
            printpage()
            open("upload/" + fn2, "wb").write(fileitem2.file.read())
            fileitem2 = os.path.basename(fileitem2.filename.replace(' ', '-'))
            print('''
                Meddelanden per dag: <a href="http://digitalametoder.science/results/'''
                + messagesperday(parsenetvizz("upload/" + fileitem2)) + '''perday.png">
                här</a> (högerklicka och välj "spara som")
                <br>
                Meddelanden per timme: <a href="http://digitalametoder.science/results/'''
                + messagesperhour(parsenetvizz("upload/" + str(fileitem2))) + '''perhour.png">
                här</a> (högerklicka och välj "spara som")
                ''')


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
