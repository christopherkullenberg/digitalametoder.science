#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import cgi
import cgitb
import sys
import re
import os
import pandas as pd
import networkx as nx
from werkzeug import secure_filename
import time
from printhtml import printrtnetwork
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)
form = cgi.FieldStorage()


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
            printrtnetwork()
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
            print('''Nätverksfilen för RT-network kan laddas ned <a href="http://digitalametoder.science/results/''' +
                  filename + '''.gexf">här</a> (högerklicka och välj "spara som")  och sedan öppnas med Gephi.''')
        elif fileitem2.filename:
            open('upload/' + fn2, 'wb').write(fileitem2.file.read())
            fn2 = os.path.basename(fileitem2.filename.replace(' ', '-'))
            df = pd.read_csv('upload/' + fn2)
            printrtnetwork()
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
            print('''Nätverksfilen för RT-network kan laddas ned <a href="http://digitalametoder.science/results/''' +
                  filename + '''.gexf">här</a> (högerklicka och välj "spara som")  och sedan öppnas med Gephi.''')
        else:
            printrtnetwork()
            print('<p>Ingen fil valdes.</p>')
    except UnicodeError:
        print("<p>Filen har inte korrekt teckenkodning. Testa att spara om med Unicode / UTF-8.</p>")


try:
    openfile()
except KeyError:
    printrtnetwork()
    sys.exit()

print("</body></html>")
