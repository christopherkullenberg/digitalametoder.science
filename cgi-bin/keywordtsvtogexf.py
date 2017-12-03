#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import cgi
import os
import csv
from gexf import Gexf
from itertools import combinations
from printhtml import printkeywordstogexf

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']

# Test if the file was uploaded

try:
    if fileitem.filename:
        fn = os.path.basename(fileitem.filename)
        open('upload/' + fn, 'wb').write(fileitem.file.read())

except KeyError:
    printkeywordstogexf()
    print('<p>No file was uploaded</p>')

printkeywordstogexf()
print('<p>The file "' + fn + '" was uploaded successfully</p>')

thefile = open("upload/" + fn, 'r', encoding="utf-8")
tsv = csv.reader(thefile, delimiter='\t')
next(tsv)  # remove headers
gexf = Gexf("Keyword Co-occurrence Network", "File:" + fn + ".")
graph = gexf.addGraph("undirected", "static", "Web of Science Keyword network")
keywords = []
keywordset = []
for t in tsv:
    DE = t[19]
    keywordset.append(DE.split('; '))
    for keyw in DE.split('; '):
        if len(keyw) < 1:  # removes empty keywords
            continue
        else:
            graph.addNode(keyw.lower(), keyw.lower())  # add nodes to graph


edgelist = []

for k in keywordset:
    cooccurrence = list(combinations(k, 2))
    for c in cooccurrence:
        edgelist.append(c)

for enumer, edge in enumerate(edgelist):
    # print(enumer, edge[0].lower(), edge[1].lower())
    graph.addEdge(enumer, edge[0].lower(), edge[1].lower())

# Write file wrapped in <p> for pretty printing
print("<p>")
directory = "/home/chrisk/tools.christopherkullenberg.se/public_html/download/"
gexf_file = open(directory + fn + ".gexf", "wb")
gexf.write(gexf_file)
dldir = "http://digitalametoder.science/results/"
print("<p>")
print('<p>Created network file: <a href="' + dldir + fn + '.gexf">' + fn
      + '.gexf</a>')

print('''
</body>
</html>
''')
