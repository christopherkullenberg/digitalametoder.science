#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import cgi
import sys
import os
import requests
import pandas as pd
from werkzeug import secure_filename
from printhtml import printluftdata
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)
form = cgi.FieldStorage()

def openfile():
    # Get filename here.
    fileitem = form['filename']
    try:
        if fileitem.filename:
            fn = os.path.basename(fileitem.filename.replace(' ', '-'))
            thefile = open('upload/' + fn, 'wb').write(fileitem.file.read())
            df = pd.read_excel('upload/' + fn, skiprows=0)
            df['Status'] = df['Status'].astype(str)
            printluftdata()
            checksensors(df, fn)
        else:
            printluftdata()
            print("<p>Ingen fil vald.</p>")

    except UnicodeError:
        printluftdata()
        print("<p>Filen har inte korrekt teckenkodning. Testa att spara om med Unicode / UTF-8.</p>")


def checksensors(df, fn):
    online = 0
    offline = 0

    for row in df.iterrows():
        sensor = row[1][0]
        baseurl = "https://www.madavi.de/sensor/graph.php?sensor=esp8266-" + str(sensor) + "-sds011"
        #print(baseurl)
        html = requests.get(baseurl)
        #print(html.text)
        if "Sensor nicht gefunden" in html.text:
            print("<p>Sensor " + str(sensor) + " is offline</p>")
            df.set_value(row[0], 'Status', 'Offline')
            offline += 1
        else:
            print("<p>Sensor " + str(sensor) + " is online</p>")
            df.set_value(row[0], 'Status', 'Online')
            online += 1
        df.to_excel("/home/chrisk/digitalametoder.science/results/" + fn)
    print('''<p><a href="https:///digitalametoder.science/results/'''
                    + fn + '''">Excelfil med sensorstatus.</a></p>''')











try:
    openfile()
except KeyError:
    printluftdata()
    sys.exit()

print("</body></html>")
