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


gexf = Gexf("Citation Network", "File:" + fn + ".")
graph = gexf.addGraph("directed", "static", "Web of Science Citation network")

citationnetworkdict = {}

for t in tsv:
    AU = t[1]
    CR = t[29]
    citationnetworkdict.update({AU: CR.split('; ')})


numberofedges = 0
for key, value in citationnetworkdict.items():
    graph.addNode(key, key)

    for v in value:
        graph.addNode(v,v)
        #print(str(numberofedges) + "***" + key + "***" + v)
        graph.addEdge(str(numberofedges), key, v)
        numberofedges += 1

# Write file, wrap in <p> for pretty printing
print("<p>")
gexf_file = open("/home/chrisk/tools.christopherkullenberg.se/public_html/download/citation"+ fn + ".gexf", "wb")
gexf.write(gexf_file)
print("</p>")

print('<p>Created network file: <a href="http://tools.christopherkullenberg.se/download/citation' 
+ fn + '.gexf">citation' + fn + '.gexf</a>')

print('''
</body>
</html>
''')







