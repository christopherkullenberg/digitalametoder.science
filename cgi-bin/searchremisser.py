#!/usr/bin/python3

# -*- coding: UTF-8 -*-

# Import modules for CGI handling and UTF-8 handling of input/output
import cgi
import cgitb
import sys
import re
import os
import sqlite3
import numpy as np
import collections
import pandas as pd
from bokeh.plotting import figure, output_file, save
from bokeh.embed import file_html
from bokeh.resources import CDN

# Fix IO and utf8
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

''' For regexp search to work you need to install 'apt-get install sqlite3-pcre'
and put '.load /usr/lib/sqlite3/pcre.so' into the file '~/.sqliterc'''
conn = sqlite3.connect('remisserlycka.sqlite3')
# Enable regexp in sqlite3


def regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None


conn.create_function("REGEXP", 2, regexp)

# Get data from fields
form = cgi.FieldStorage()
if form.getvalue('like_search_word'):
    form_string = form.getvalue('like_search_word')
    search_string = form_string
else:
    search_string = "Not entered"

if form.getvalue('result_limit'):
    result_limit = form.getvalue('result_limit')
else:
    result_limit = 1000

if form.getvalue('order'):
    theorder = form.getvalue('order')
    if theorder == "Stigande":
        order = "ASC"
    elif theorder == "Fallande":
        order = "DESC"
    else:
        order = "ASC"

if form.getvalue('mode'):
    themode = form.getvalue('mode')
    if themode == "like":
        mode = "like"
    elif themode == "regexp":
        mode = "regexp"
    elif themode == "match":
        mode = "match"
    else:
        mode = "like"
else:
    mode = "undefined"


# Queries to the database with a LIKE seach
# sqlite> CREATE TABLE main (id INT PRIMARY KEY, dom TEXT, pdflink TEXT, content TEXT, UNIQUE(dom));


def matchsearches():
    if order == "ASC":
        search = conn.execute("SELECT title, pdflink, text FROM remisserfts WHERE \
                          text MATCH (?) ORDER BY title ASC LIMIT (?)",
                              (search_string, result_limit, ))
    elif order == "DESC":
        search = conn.execute("SELECT title, pdflink, text FROM remisserfts WHERE \
                          text MATCH (?) ORDER BY title DESC LIMIT (?)",
                              (search_string, result_limit, ))
    else:
        print("Something went wrong")
    return(search)


def likesearches():
    percentsearchstring = "%" + search_string + "%"
    if order == "ASC":
        search = conn.execute("SELECT title, pdflink, text FROM remisser WHERE \
                          text LIKE (?) ORDER BY title ASC LIMIT (?)",
                              (percentsearchstring, result_limit, ))
    elif order == "DESC":
        search = conn.execute("SELECT title, pdflink, text FROM remisser WHERE \
                          text LIKE (?) ORDER BY title DESC LIMIT (?)",
                              (percentsearchstring, result_limit, ))
    else:
        print("Something went wrong")
    return(search)

# Queries to the database with a REGEXP seach


def regexpsearches():
    if order == "ASC":
        search = conn.execute("SELECT title, pdflink, text FROM remisser WHERE \
                          text REGEXP (?) ORDER BY title ASC LIMIT (?)",
                              (search_string, result_limit, ))
    elif order == "DESC":
        search = conn.execute("SELECT title, pdflink, text FROM remisser WHERE \
                          text REGEXP (?) ORDER BY title DESC LIMIT (?)",
                              (search_string, result_limit, ))
    else:
        print("Something went wrong")
    return(search)


# Select which search method
if mode == 'like':
    searchmode = likesearches()
elif mode == 'regexp':
    searchmode = regexpsearches()
elif mode == 'match':
    searchmode = matchsearches()
else:
    print("Error")

results = []
for s in searchmode:
    results.append(s)


def totalsize():
    totaldbsize = conn.execute("SELECT count(*) FROM remisser")
    for t in totaldbsize:
        total = t
    return(total[0])


###
print("Content-type:text/html; charset=utf-8\r\n\r\n")
print()


print('''<style>
    table#t01 tr:nth-child(even) {
    background-color: #eee;
    }
    table#t01 tr:nth-child(odd) {
    background-color: #fff;
    }
    table#t01 th {
    color: white;
    background-color: black;
    }
    td#d01 {
    padding: 15px;
    }
    span.highlight {
    background-color: yellow;
    }
    </style>
    ''')


print('<p>Du sökte på ordet <b>' + search_string + '</b> i ' + mode
      + '-läge. Databasen har sammanlagt <b>' + str(totalsize())
      + ' </b> sparade kommentarer. Gör \
       en <a href="http://digitalametoder.science/remisser.html">ny sökning</a>.</p>')
print("<br>")

# https://www.google.se/?q=M+10072-12+site:%2F%2Fwww.markochmiljooverdomstolen.se%2F

header = '<table id="t01"><b><tr><td><b>Remiss</b></td><td><b>PDF</b></td>\
          <td><b>Resultat</b></td></tr></b>'
print(header)


def printresults():
    resultcounter = 0
    for s in results:
        print("<tr>")
        print('<td id=#d01><b>' + s[0] + '</td>')
        print('<td id=#d01><a href="https://scientometrics.flov.gu.se/happiness/map/' + s[1][0:2] + ".pdf"
              + '">PDF</a></td>')
        print("<td>")

        contextstring = "(.*)(" + form_string + ")(.*\n.*)"
        printbold = re.findall(contextstring, s[2], re.IGNORECASE)
        if printbold:
            hitperdocumentcounter = 1
            for p in printbold:
                print(str(hitperdocumentcounter) + ". " + p[0]
                      + '<span class="highlight">' + p[1] + "</span>" + p[2])
                hitperdocumentcounter += 1
                print("<br>")
        else:
            continue
        print("</td>")

        print("</tr>")
        resultcounter += 1
    print("</table>")
    return(resultcounter)


print("<i>Sökningen gav " + str(printresults()) + " träffar.</i>")
print('<br>Gör en <a href="http://digitalametoder.science/remisser.html">ny sökning</a>.')

print('''
    <br>
    </body>
    </html>
    ''')
