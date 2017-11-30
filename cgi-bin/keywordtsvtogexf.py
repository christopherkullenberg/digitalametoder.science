#!/usr/bin/python3

import cgi, os
import cgitb; cgitb.enable()
import csv

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']

# Test if the file was uploaded
if fileitem.filename:
   fn = os.path.basename(fileitem.filename)
   open('upload/' + fn, 'wb').write(fileitem.file.read())

   message = '<p>The file "' + fn + '" was uploaded successfully</p>'
   
else:
   message = 'No file was uploaded'
   
print("""\
Content-Type: text/html\n
<html>
  <head>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="http://tools.christopherkullenberg.se/style.css">
    <title>Results</title>
  </head>
<body>
   <p>Processing...</p>
""" + message)



thefile = open("upload/" + fn, 'r', encoding="utf-8")
tsv = csv.reader(thefile, delimiter='\t')
next(tsv) #remove headers

from gexf import Gexf
from itertools import combinations


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
            graph.addNode(keyw.lower(), keyw.lower()) # add nodes to graph


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
gexf_file = open("/home/chrisk/tools.christopherkullenberg.se/public_html/download/"+ fn + ".gexf", "wb")
gexf.write(gexf_file)
print("<p>")

print('<p>Created network file: <a href="http://tools.christopherkullenberg.se/download/' 
+ fn + '.gexf">' + fn + '.gexf</a>')

print('''
</body>
</html>
''')










