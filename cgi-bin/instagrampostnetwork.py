#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import cgi
import sys
import os
import json
import pandas as pd
# from werkzeug import secure_filename
from printhtml import printinstagrampost
import networkx as nx
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)
form = cgi.FieldStorage()


def commentstodataframe(jsonobject):
    '''This function makes a dataframe of selected content
    in the json data structure.'''
    commentcounter = 0
    thedata = []
    for j in jsonobject:
        commentdata = {}
        postid = j['shortcode']
        posturl = 'https://www.instagram.com/p/' + postid
        commentdata["id"] = postid
        commentdata["url"] = posturl
        commentlist = []
        if len(j['comments']['data']) > 0:
            commentcounter += 1
            for k in j['comments']['data']:
                commentlist.append((k['owner']['username'], k['text']))

            commentdata["comments"] = commentlist
            thedata.append(commentdata)
    # print("Number of comments added to dataframe: " + str(commentcounter))
    df = pd.DataFrame(thedata, columns=['id', 'url', 'comments'])
    return(df)


def makepostdirectednetwork(commentsdataframe, fn):
    '''Makes a directed network from a user to a
    post. Can be visualised as an in- or outdegree
    network depending on your question.'''
    G = nx.DiGraph()
    postcounter = 0
    interactionscounter = 0
    userlist = []
    for row in commentsdataframe.iterrows():
        postid = row[1][0]
        postcounter += 1
        for c in row[1][2]:
            user = c[0]
            interactionscounter += 1
            userlist.append(user)
            G.add_edge(user, postid)  # direction of graph, from user to post
    nx.write_gexf(G, "/home/chrisk/digitalametoder.science/results/" +
                  fn + "_directedpostnetwork.gexf")
    printinstagrampost()
    print("<p>Poster: " + str(postcounter) + "</p>")
    print("<p>Interaktioner (inkl. multipla interaktioner med samma post: "
          + str(interactionscounter) + "</p>")
    print("<p>Unika användare: " + str(len(set(userlist))) + "</p>")
    print('''<p>Fil att ladda ned: <a href="https://digitalametoder.science/results/'''
          + fn + '''_directedpostnetwork.gexf">.gexf</a></p> (högerklicka och välj "spara som".)''')


def openfile():
    # Get filename here.
    fileitem = form['filename']
    try:
        if fileitem.filename:
            fn = os.path.basename(fileitem.filename.replace(' ', '-'))
            #  thefile = open('upload/' + fn, 'wb').write(fileitem.file.read())
            jsonfile = open('upload/' + fn, encoding="utf-8")
            jsonobject = json.load(jsonfile)
            makepostdirectednetwork(commentstodataframe(jsonobject), fn)
        else:
            printinstagrampost()
            print("<p>Ingen fil vald.</p>")

    except UnicodeError:
        printinstagrampost()
        print("<p>Filen har inte korrekt teckenkodning. Testa att spara om med Unicode / UTF-8.</p>")


try:
    openfile()
except KeyError:
    printinstagrampost()
    sys.exit()

print("</body></html>")
