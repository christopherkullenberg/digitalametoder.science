#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import cgi, cgitb
import sys
import re
import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from werkzeug import secure_filename
import time
from printhtml import printtimemessages
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)
form = cgi.FieldStorage()

def parsetags(filename):
    df = pd.read_csv(filename, sep=",") # TAGS file
    pd.created_at = pd.to_datetime(df.time, format='%d/%m/%Y %H:%M:%S')
    df.index = pd.created_at
    print("<p>Antal rader i filen: " + str(len(df)))
    return(df)

def parsenetvizz(filename):
    df = pd.read_csv(filename, sep="\t") # Netvizz file
    pd.created_at = pd.to_datetime(df.post_published_sql,
                                   format='%Y-%m-%d %H:%M:%S')
    df.index = pd.created_at
    print("<p>Antal rader i filen: " + str(len(df)))
    return(df)

def messagesperday(dataframe):
    messagesperday = dataframe.resample('D').count()
    fig = plt.figure(figsize=(15,7))
    ax = fig.add_subplot(111)
    plt.title('Meddelanden per dag', size=16)
    try:
        messagesperday['post_id'].plot() #Netvizz data
    except KeyError:
        messagesperday['status_url'].plot() #Tags data
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

def openfile():
    # Get filename here.

    fileitem = form['filename'] # Tags dat
    fn = secure_filename(fileitem.filename)

    fileitem2 = form['filename2'] # Netvizz data
    fn2 = secure_filename(fileitem2.filename)
    # Test if the file was uploaded
    try:
        if fileitem.filename:
            printtimemessages()
            print("<p>TAGS-data</p>")
            print("Filnamn: " + fn)
            open("upload/" + fn, "wb").write(fileitem.file.read())
            fileitem = os.path.basename(fileitem.filename.replace(' ', '-'))
            print('''
                <p>Meddelanden per dag: <a href="http://digitalametoder.science/results/'''
                + messagesperday(parsetags("upload/" + fileitem)) + '''perday.png">
                här</a> (högerklicka och välj "spara som")</p>
                <br>
                <p>Meddelanden per timme: <a href="http://digitalametoder.science/results/'''
                + messagesperhour(parsetags("upload/" + fileitem)) + '''perhour.png">
                här</a> (högerklicka och välj "spara som")</p>
                ''')
        elif fileitem2.filename:
            printtimemessages()
            open("upload/" + fn2, "wb").write(fileitem2.file.read())
            fileitem2 = os.path.basename(fileitem2.filename.replace(' ', '-'))
            print('''
                <p>Meddelanden per dag: <a href="http://digitalametoder.science/results/'''
                + messagesperday(parsenetvizz("upload/" + fileitem2)) + '''perday.png">
                här</a> (högerklicka och välj "spara som")</p>
                <br>
                Meddelanden per timme: <a href="http://digitalametoder.science/results/'''
                + messagesperhour(parsenetvizz("upload/" + str(fileitem2))) + '''perhour.png">
                här</a> (högerklicka och välj "spara som")
                ''')
        else:
            printtimemessages()
            print('<p>Ingen fil valdes.</p>')
    #except KeyError:
    #    print("<p>KEYERROR</p>")
    except UnicodeError:
        print("<p>Filen har inte korrekt teckenkodning. Testa att spara om med Unicode / UTF-8.</p>")


try:
    openfile()
except KeyError:
    printtimemessages()
    sys.exit()

#printtimemessages()
#openfile()

print("</body></html>")
