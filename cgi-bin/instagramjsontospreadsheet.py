#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import cgi
import sys
import os
import json
import pandas as pd
from werkzeug import secure_filename
from printhtml import printinstagramparser
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)
form = cgi.FieldStorage()


def jsontospreadsheet(jsonobject, fn):
    '''This function takes the json object and
    writes .xlsx and .csv files.'''
    counter = 0
    totaldata = []
    for j in jsonobject:
        datarow = {}
        datarow["id"] = j['shortcode']
        try:
            datarow["content"] = j['edge_media_to_caption']['edges'][0]['node']['text']
        except IndexError:
            datarow["content"] = None
        try:
            datarow["tags"] = j['tags']
        except KeyError:
            datarow["tags"] = None
        datarow["likes"] = j["edge_media_preview_like"]['count']
        datarow["url"] = 'https://www.instagram.com/p/' + j['shortcode']
        datarow["commentnumber"] = j['edge_media_to_comment']['count']
        try:
            datarow["location"] = j['location']['slug']
            datarow["locationname"] = j['location']['name']
            datarow["locationid"] = j['location']['id']
            datarow["locationurl"] = "https://www.instagram.com/explore/locations/" + str(j['location']['id'])
        except TypeError:
            datarow["location"] = None
            datarow["locationname"] = None
            datarow["locationid"] = None
            datarow["locationurl"] = None
        datarow["time"] = j['taken_at_timestamp']
        datarow["unixtime"] = j['taken_at_timestamp']
        # Iterate the comments, if any.
        commentlist = []
        if len(j['comments']['data']) > 0:
            for k in j['comments']['data']:
                commentlist.append((k['owner']['username'], k['text']))
            datarow["comments"] = commentlist
        else:
            datarow["comments"] = None
        # Append it all
        totaldata.append(datarow)
        counter += 1

    df = pd.DataFrame(totaldata, columns=['id','content', 'tags', 'likes',
                                          'url', 'commentnumber',
                                          'location', 'locationname',
                                         'locationid', 'locationurl', 'time',
                                         'unixtime', 'comments'])
    df.time = pd.to_datetime(df.time,unit='s')
    df.to_excel("/home/chrisk/digitalametoder.science/results/" + fn + ".xlsx")
    df.to_csv("/home/chrisk/digitalametoder.science/results/" + fn + ".csv")
    printinstagramparser()
    print("<p>Number of rows added to dataframe: " + str(counter) + "</p>")
    print('''
            <p><a href="https:///digitalametoder.science/results/'''
            + fn + '''.xlsx">Excelfil</a></p>
            <p><a href="https:///digitalametoder.science/results/'''
            + fn + '''.csv">CSV-fil</a></p>
          ''')



def openfile():
    # Get filename here.
    fileitem = form['filename']
    try:
        if fileitem.filename:
            fn = os.path.basename(fileitem.filename.replace(' ', '-'))
            thefile = open('upload/' + fn, 'wb').write(fileitem.file.read())
            jsonfile = open('upload/' + fn, encoding="utf-8")
            jsonobject = json.load(jsonfile)
            jsontospreadsheet(jsonobject, fn)
        else:
            printinstagramparser()
            print("<p>Ingen fil vald.</p>")

    except UnicodeError:
        printinstagramparser()
        print("<p>Filen har inte korrekt teckenkodning. Testa att spara om med Unicode / UTF-8.</p>")



try:
    openfile()
except KeyError:
    printinstagramparser()
    sys.exit()

print("</body></html>")
