#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import pandas as pd
from bokeh.plotting import figure, output_file, save
#from bokeh.embed import file_html
from bokeh.resources import CDN
from bokeh.embed import components
import collections
from gexf import Gexf
from itertools import combinations
import numpy as np
#import cgi, os
#import cgitb; cgitb.enable()
import cgi, cgitb
import os
import sys
import csv
import time
# import matplotlib.pyplot as plt # Not used right now
# from wordcloud import WordCloud, STOPWORDS # Not used right now
# import image # Not used right now.
# Get file from form
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

ts = int(time.time())

form = cgi.FieldStorage()
fileitem = form['filename']

# Test if the file was uploaded
if fileitem.filename:
   fn = os.path.basename(fileitem.filename)
   open('upload/' + fn, 'wb').write(fileitem.file.read())

   message = 'The file "' + fn + '" was uploaded successfully'

else:
   message = 'No file was uploaded'

print("content-type:text/html; charset=utf-8\r\n\r\n")
print()

print('''\
Content-Type: text/html\n
<html>
  <head>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="http://digitalametoder.science/stylecitepy.css">
    <title>Results for Cite.py</title>
  </head>
<body>
   <h1>Cite.py</h1>''')
print('<h2>View the <a href="http://digitalametoder.science/results/' + str(ts) + '">results online</a>.</h2>')
print('<h2>Download <a href="http://digitalametoder.science/results/' + str(ts) + '.zip">archive of results</a> for offline browsing.</h2>')
print('<p><b>System log:</b><br>' + message + '</p>')

thefile = open("upload/" + fn, 'r', encoding="utf-8")
WoSdata = csv.reader(thefile, delimiter='\t')
next(WoSdata) #remove headers

#ts = int(time.time())
print("<p>Timestamp: " + str(ts) + " </p>")
if not os.path.exists("/home/chrisk/digitalametoder.science/results/" + str(ts)):
    os.makedirs("/home/chrisk/digitalametoder.science/results/" + str(ts))

plotyears = []
cr = []
authors = []
journals = []
keywords = []
keywordset = []

records = 0
citrefcounter = 0
authorcounter = 0
journalcounter = 0
keywordcounter = 0

#indexbody = [] Use to write everything to index. Memory overload, see below
authorbody = []
journalbody = []
keywordbody = []

wclist = []

indexbodydict= {}
citationnetworkdict = {}

# Open up the Web of Science source data as a tsv file.
#with open(fn,'r') as tsv: # change file-name here
#    next(tsv) #Skips the first line in the file, containing the TSV headers
#    WoSdata = [line.strip().split('\t') for line in tsv] #everything as a list

# This begins the creation of a .gexf graph for keyword co-occurrence analysis.
# It comes already here because nodes are added in the loop below.
gexf = Gexf("Keyword Co-occurrence Network", "File:" + fn + ".")
graph = gexf.addGraph("directed", "static", "Web of Science Keyword network")

"""
This loop parses, redefines and writes the values selecte to 'index.html'
However, it also contains surplus variables for future uses, following the
non-existent documentation of the ISI format. Use however you feel like.
"""
for W in WoSdata:
    PT = W[0] # Publication Type
    AU = W[1] # Authors
    BA = W[2] # ?
    BE = W[3] # Editors of Proceedings
    GP = W[4] # ?
    AF = W[5] # Authors Full
    BF = W[6] # ?
    CA = W[7] # Group Authors
    TI = W[8] # Title
    SO = W[9] # Source (Journal title, full)
    SE = W[10] # Book Series title
    BS = W[11] # ?
    LA = W[12] # Language
    DT = W[13] # Document Type
    CT = W[14] # Conference Title
    CY = W[15] # Conference Date
    CL = W[16] # Conference Location
    SP = W[17] # Conference Sponsors
    HO = W[18] # Conference Host
    DE = W[19] # Original Keywords
    ID = W[20] # New Keywords by ISI (keywords plus)
    AB = W[21] # Abstract
    C1 = W[22] # Research Addresses: Note [] in fields.
    RP = W[23] # Reprint Address
    EM = W[24] # E-mail (Semi-colon separated)
    RI = W[25] # Researcher ID
    OI = W[26] # ?
    FU = W[27] # Funding agency and grant number
    FX = W[28] # Funding text
    CR = W[29] # Cited references (Semi-colon separated)
    NR = int(W[30]) # Cited reference count (Numerical value)
    TC = int(W[31]) # Times cited (Numerical value)
    Z9 = int(W[32]) # Total times Cited
    U1 = int(W[33]) # ?
    U2 = int(W[34]) # ?
    PU = W[35] # Publisher
    PI = W[36] # Publisher city
    PA = W[37] # Publisher Address
    SN = W[38] # ISSN (String value)
    EI = W[39] # ?
    BN = W[40] # ISBN
    J9 = W[41] # 29 Character Journal Abbreviation
    JI = W[42] # ISO Journal Title Abbreviation
    PD = W[43] # Publication date (mixed string and possible integer value)
    PY = int(W[44]) # Publication Year (Could also be parsed with date module)
    VL = W[45] # Volume (could also be parsed as integer, but not really useful)
    IS = W[46] # Issue (contains both numerical values and hyphenations)
    PN = W[47] # Part Number
    SU = W[48] # Supplement (number)
    SI = W[49] # Special Issue
    MA = W[50] # ?
    BP = W[51] # Beginning page
    EP = W[52] # End page
    AR = W[53] # Article number of APS journals
    DI = W[54] # DOI Number
    D2 = W[55] # ?
    PG = int(W[56]) # Number of Pages
    WC = W[57] # Research Field
    SC = W[58] # Science Categories?
    GA = W[59] # IDS number, ISI original
    UT = W[60] # WOS ISI unique artile identifier

    # Count records, good for verification of your original data.
    if PT:
        records += 1
    else:
        continue

    # This appends out the Web of Science categories to list.
    for category in WC.split('; '):
        wclist.append(category)

    """
    Now, this adds the content of the index.html by creating a dictionary
    with the Author, Title, Journal and Year as keys and the Times Cited
    as values. In a later stage, this dictionary will be limited to 500
    records sorted by Times Cited to prevent creating browser hangups.
    """
    indexbodydict.update({'<tr>\n<td>' + AU + '<br><a href="http://dx.doi.org/'
    + DI + '" target="_blank"><div title="' + AB + '">' + TI +
    '</div>\n</a></td>' + '\n<td>' + SO + '</td>\n <td>' + str(PY) + '</td><td>'
    + str(TC) + '</td>\n</tr>\n': TC})

    # Create list of years
    plotyears.append(PY)

    # and a list of journals
    journals.append(SO)

    # and a list of keywords (splitted with semicolons)
    keywordset.append(DE.split('; '))

    # This dictionary is later used to create a citation network file.
    citationnetworkdict.update({AU: CR.split('; ')})

    # This loop splits and adds cited refereces to create cr.html page
    for citref in CR.split('; '):
        cr.append(citref)
        citrefcounter += 1

    # This loop splits and adds authors for the authors.html page
    for au in AU.split('; '):
        authors.append(au)

    # This loop splits and adds keywords to the keywords.html page
    for keyw in DE.split('; '):
        if len(keyw) < 1:  # removes empty keywords
            continue
        else:
            keywords.append(keyw.lower()) # make everything lower case
            graph.addNode(keyw.lower(), keyw.lower()) # add nodes to graph


"""
Below the body data of the static pages are created. Increase the values
after 'most_common' to include more data. But keep in mind that this will
slow down the browser.
"""
# Create author list
authorcount = collections.Counter(authors)
for a in authorcount: # count unique authors, not duplicates
    authorcounter += 1
for author, count in authorcount.most_common(500):
    authorbody.append("<tr>\n<td>" + author + "</td>\n<td>"
                      + str(count) + "</td>\n</tr>\n")

# Create journal list
journalcount = collections.Counter(journals)
for j in journalcount:
    journalcounter +=1
for journal, count in journalcount.most_common(500):
    journalbody.append("<tr>\n<td>" + journal + "</td>\n<td>"
                       + str(count) + "</td>\n</tr>\n")

# Create keyword list
keywordcount = collections.Counter(keywords)
for k in keywordcount:
    keywordcounter +=1
for keyword, count in keywordcount.most_common(1000):
    keywordbody.append("<tr>\n<td>" + keyword + "</td>\n<td>"
                       + str(count) + "</td>\n</tr>\n")

# This is just for printing the top 20 wc categories to the terminal.
# !!! Make a proper page out of this in future version
wclistcount = collections.Counter(wclist)
for wc, count in wclistcount.most_common(20):
    print("<p>" + wc + "\t" + str(count) + "</p>")

# Create edges for a keyword cooccurrence network as defined alredy on line 60.
edgelist = []
for k in keywordset:
    cooccurrence = list(combinations(k, 2))
    for c in cooccurrence:
        edgelist.append(c)

for enumer, edge in enumerate(edgelist):
    # print(enumer, edge[0].lower(), edge[1].lower())
    graph.addEdge(enumer, edge[0].lower(), edge[1].lower())

# Write file
print("<p>")
gexf_file = open("/home/chrisk/digitalametoder.science/results/" + str(ts) + "/" + fn + "Keywords.gexf", "wb")
gexf.write(gexf_file)
print("</p>")

"""
# Create graphviz visualization (experimental) Not used right now
from graphviz import Digraph

u = Digraph('unix', fn='testargraphviz.gv')
u.body.append('size="6,6"')
u.node_attr.update(color='lightblue2', style='filled')

testlist = [('katt', 'fax'), ('kille', 'tjej')]

edgetoplist = collections.Counter(edgelist)
#print(edgetoplist)
for n in edgetoplist.most_common(100):
    print(n)

for edge, value in edgetoplist.most_common(100):
    edge1 = edge[0].lower()
    edge2 = edge[1].lower()
    u.edge(edge1, edge2)

u.view()
"""

# Create nodes and edges for Citation network.
gexf = Gexf("Citation Network", "File:" + fn + ".")
graph = gexf.addGraph("directed", "static", "Web of Science Citation network")

numberofedges = 0
for key, value in citationnetworkdict.items():
    graph.addNode(key, key)

    for v in value:
        graph.addNode(v,v)
        #print(str(numberofedges) + "***" + key + "***" + v)
        graph.addEdge(str(numberofedges), key, v)
        numberofedges += 1

# Write file
print("<p>")
gexf_file = open("/home/chrisk/digitalametoder.science/results/" + str(ts) + "/" + fn + "Citations.gexf", "wb")
gexf.write(gexf_file)
print("</p>")

# Create the header graph with Bokeh
counter = collections.Counter(plotyears) #count them
output_file("/home/chrisk/digitalametoder.science/results/"  + str(ts) + "/years.html", title="Citepy - Yearly distribution of records")

years = []
val   = []
yearvaldict = {}

for number in sorted(counter): #This puts years and values
    years.append(number)
    value = counter[number]
    val.append(value)
    yearvaldict[number] = [value]

print("<p>")
for key, value in yearvaldict.items():
    print(key, value)
print("</p>")

# Convert data into a panda DataFrame format
data=pd.DataFrame({'year':years, 'value':val})

# Create new column (yearDate) equal to the year Column but with datetime format
data['yearDate']=pd.to_datetime(data['year'],format='%Y')

# Create a line graph with datetime x axis and use datetime column(yearDate)
# for this axis
p = figure(width=600, height=150, x_axis_type="datetime")
p.toolbar.logo = None
p.toolbar_location = None #"right"
p.line(x=data['yearDate'],y=data['value'], color="#B7ADCF", line_width=2)
#show(p) # for debugging
bokehhtml = components(p)
save(p)


"""
#Create wordcloud of keywords. Not used in the current version. Just a suggest.
# Stopwords, just add more if needed.
stopwords = STOPWORDS
stopwords.add("et")
stopwords.add("will")
stopwords.add("al")
stopwords.add("also")

# Generating wordcloud (change size)
wordcloud = WordCloud(
        background_color="white",
        max_words=500,
        stopwords=STOPWORDS,
        width=3000,
        height=1500
        )
wordcloud.generate(str(keywords))

# Generating the image and showing it.
plt.imshow(wordcloud)
plt.axis("off")
print('Saving Wordcloud as: ' + fn + '.png')
plt.savefig(fn + '.png') # change to .svg, .pdf etc. for other outputs.
##plt.show()
"""


"""
Below begins the html rendering to files.
"""
# Read css and tsorter javascript
thecssfile = open('stylecitepy.css', 'r', encoding="utf-8")
csscontent = thecssfile.read()
thetsorterfile = open('tsorter.min.js', 'r', encoding="utf-8")
tsortercontent = thetsorterfile.read()

# Open the files for writing)
htmlfile = open('/home/chrisk/digitalametoder.science/results/'  + str(ts) + '/index.html','w')
crfile = open('/home/chrisk/digitalametoder.science/results/'  + str(ts) + '/cr.html','w')
authorfile = open('/home/chrisk/digitalametoder.science/results/'  + str(ts) + '/authors.html','w')
journalfile = open('/home/chrisk/digitalametoder.science/results/'  + str(ts) + '/journals.html', 'w')
keywordfile = open('/home/chrisk/digitalametoder.science/results/'  + str(ts) + '/keywords.html', 'w')
cssfile = open('/home/chrisk/digitalametoder.science/results/'  + str(ts) + '/stylecitepy.css', 'w')
tsorterfile = open('/home/chrisk/digitalametoder.science/results/'  + str(ts) + '/tsorter.min.js', 'w')

# Wite css and tsorter javascript
for linecss in csscontent:
    cssfile.write(linecss)
cssfile.close()
for tsort in tsortercontent:
    tsorterfile.write(tsort)
tsorterfile.close()

# This header is shared for all pages.
header = '''
<!DOCTYPE html>
<html>
<head>
<link href="stylecitepy.css" rel="stylesheet">
<script src="tsorter.min.js" type="text/javascript"></script>
<script>
function init() {
    var sorter = tsorter.create('result_table');
}

window.onload = init;
</script>
</head>
<body>
<h1>Results for <em>''' + fn + ''' </em></h1>
''' + bokehhtml[0] + bokehhtml[1] + '''
<a href="index.html">Records</a>: ''' + str(records) + '''
<a href="authors.html">Authors</a>: ''' + str(authorcounter) + '''
<a href="journals.html">Journals</a>: ''' + str(journalcounter) + '''
<a href="cr.html">Cited References</a>: ''' + str(citrefcounter) + '''
<a href="keywords.html">Original Keywords</a>: ''' + str(keywordcounter) + '''
<br><a href="years.html">Yearly output (graph)</a> |
<a href="''' + fn + '''
Keywords.gexf">Keyword Co-occurrence Network (.gexf)</a> |
<a href="''' + fn + '''
Citations.gexf">Citation Network (Authors, Cited references) (.gexf)</a> |
'''

# This top is specific to index.html
indexbodytop = """
<table id="result_table" class="sortable">
    <thead>
        <tr>
            <th>Author / Title</th>
            <th>Journal</th>
            <th data-tsorter="numeric">Year</th>
            <th data-tsorter="numeric">Citations</th>
        </tr>
    </thead>
    <tbody>
"""

# This top is specific to cr.html
crbodytop = """
<table id="result_table" class="sortable">
    <thead>
        <tr>
            <th>Author</th>
            <th data-tsorter="numeric">Year</th>
            <th>Journal</th>
            <th>Volume</th>
            <th>Start page</th>
            <th>DOI</th>
            <th data-tsorter="numeric">Cited in dataset</th>
        </tr>
    </thead>
    <tbody>
"""

# This top is specific to authors.html
authorbodytop = """
<table id="result_table" class="sortable">
    <thead>
        <tr>
            <th>Author</th>
            <th data-tsorter="numeric">Authorship in dataset</th>
        </tr>
    </thead>
    <tbody>
"""

# This top is specific to journals.html
journalbodytop = """
<table id="result_table" class="sortable">
    <thead>
        <tr>
            <th>Journals</th>
            <th data-tsorter="numeric">Records in dataset</th>
        </tr>
    </thead>
    <tbody>
"""

# This top is specific to keywords.html
keywordbodytop = """
<table id="result_table" class="sortable">
    <thead>
        <tr>
            <th>Keyword</th>
            <th data-tsorter="numeric">Occurrences in dataset</th>
        </tr>
    </thead>
    <tbody>
"""

# Write to files but keep them open.
htmlfile.write(header + indexbodytop)
crfile.write(header + crbodytop)
authorfile.write(header + authorbodytop)
journalfile.write(header + journalbodytop)
keywordfile.write(header + keywordbodytop)


"""
Write the content of the main table
Note, arranged by most cited with the 'most_common' variable
Change to increase/decrease the value.
This should be rewritten in a future version.
"""
for record in dict(collections.Counter(indexbodydict).most_common(500)):
    htmlfile.write(record)

"""
This one could be used to write everything as index (without the
limitation above). Makes computer run out of memory when using large data sets.

for i in indexbody:
    htmlfile.write(i)
"""

#Write html code to file
for a in authorbody:
    authorfile.write(a)

for j in journalbody:
    journalfile.write(j)

for k in keywordbody:
    keywordfile.write(k)


"""
Create Cited Refere (CR) (cr.html) table content. This a bit complicated because
the CR format is not very consistent, and DOI numbers are not very standardized.
The loop reads from the 'cr' list, which is filled with cited references. It
counts them and creates the list from 500 most frequent occurrences. To parse
the CRs, they are split up and accessed as lists (within the list) and then
tried (try:) for content. If data is lacking, it writes "N/A".
"""
crcount = collections.Counter(cr) #Count them
for citedreference, count in crcount.most_common(500):
    crfile.write("<tr>\n")
    crsplit = (citedreference.split(', '))
    try:
        if len(crsplit[0]) > 1:
            crfile.write("<td>" + crsplit[0] + "</td>")
        else:
            crfile.write("<td>Unknown</td>")
    except IndexError:
        crfile.write("<td>" + "N/A" + "</td>")
    try:
        crfile.write("<td>" + crsplit[1] + "</td>")
    except IndexError:
        crfile.write("<td>" + "N/A" + "</td>")
    try:
        crfile.write("<td>" + crsplit[2] + "</td>")
    except IndexError:
        crfile.write("<td>" + "N/A" + "</td>")
    try:
        """Very rarely the data starts with "DOI DOI".
        Another elif-statement may prevent this."""
        if crsplit[3].startswith("DOI"):
            crfile.write('<td>N/A</td><td>N/A</td><td>'
            + '<a href="http://dx.doi.org/'
            + crsplit[3][4:] + '">' + crsplit[3][4:] + '</td>\n<td>'
            + str(count) + '</td></tr>\n')
            continue
        else:
            crfile.write("<td>" + crsplit[3] + "</td>")
    except IndexError:
        crfile.write("<td>" + "N/A" + "</td>")
    try:
        if crsplit[4].startswith("DOI"):
            crfile.write('<td>N/A</td><td><a href="http://dx.doi.org/'
            + crsplit[4][4:] + '">' + crsplit[4][4:] + '</td>\n<td>'
            + str(count) + '</td></tr>\n')
            continue
        else:
            crfile.write("<td>" + crsplit[4] + "</td>")
    except IndexError:
       crfile.write("<td>" + "N/A" + "</td>")
    try:
       crfile.write('<td><a href="http://dx.doi.org/'
       + crsplit[5][4:] + '">' + crsplit[5][4:] + '</td>')
    except IndexError:
       crfile.write("<td>" + "N/A" + "</td>")
    crfile.write("<td>" + str(count) + "</td>")
    crfile.write("</tr>\n")

#Define a footer
footer = """
    </tbody>
</table>

<script src="tsorter.min.js" type="text/javascript"></script>

</body>
</html>
"""



#Write footer and save files
htmlfile.write(footer)
htmlfile.close()
crfile.write(footer)
crfile.close()
authorfile.write(footer)
authorfile.close()
journalfile.write(footer)
journalfile.close()
keywordfile.write(footer)
keywordfile.close()

import zipfile


print('<p>Creating zip-archive for download...</p>')
zf = zipfile.ZipFile('/home/chrisk/digitalametoder.science/results/' + str(ts) + '.zip', mode='w')
try:
    print('<p>Adding files...</p>')
    zf.write('/home/chrisk/digitalametoder.science/results/' + str(ts) + '/authors.html', os.path.basename('authors.html'))
    zf.write('/home/chrisk/digitalametoder.science/results/' + str(ts) + '/index.html', os.path.basename('index.html'))
    zf.write('/home/chrisk/digitalametoder.science/results/' + str(ts) + '/tsorter.min.js', os.path.basename('tsorter.min.js'))
    zf.write('/home/chrisk/digitalametoder.science/results/' + str(ts) + '/cr.html', os.path.basename('cr.html'))
    zf.write('/home/chrisk/digitalametoder.science/results/' + str(ts) + '/journals.html', os.path.basename('journals.html'))
    zf.write('/home/chrisk/digitalametoder.science/results/' + str(ts) + '/years.html', os.path.basename('years.html'))
    zf.write('/home/chrisk/digitalametoder.science/results/' + str(ts) + '/keywords.html', os.path.basename('keywords.html'))
    zf.write('/home/chrisk/digitalametoder.science/results/' + str(ts) + '/stylecitepy.css', os.path.basename('stylecitepy.css'))
    zf.write('/home/chrisk/digitalametoder.science/results/' + str(ts) + "/" + fn + 'Citations.gexf', os.path.basename(fn + 'Citations.gexf'))
    zf.write('/home/chrisk/digitalametoder.science/results/' + str(ts) + "/" + fn + 'Keywords.gexf', os.path.basename(fn + 'Keywords.gexf'))
finally:
    print('<p>Closing file...</p>')
    zf.close()

print("<p>")
#print(ZipFile.infolist('/home/chrisk/digitalametoder.science/results/' + str(ts) + '.zip'))
print("</p>")


print("<p>Timestamp: " + str(ts) + " </p>")

print('''
</body>
</html>
''')
