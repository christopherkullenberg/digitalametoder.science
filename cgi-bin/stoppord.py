#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Import modules for CGI handling and UTF-8 handling of input/output 
import cgi, cgitb
import sys
import re
import os
import time
from nltk.corpus import stopwords
from nltk import word_tokenize
import random


# Fix input and output from apache
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

## GET TEXT FROM FORM
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
if form.getvalue('textcontent'):
    text_content = form.getvalue('textcontent')
else:
    text_content = "Not entered"


tknzr = word_tokenize(text_content)
#tokenized = tnkzr(text_content)



print("Content-type:text/html; charset=utf-8\r\n\r\n")
print()

randomfilename = str(random.getrandbits(32))

with open("/home/chrisk/digitalametoder.science/results/" + randomfilename + ".txt", 'w', encoding="utf8") as outfile:
    for t in tknzr:
        if t not in stopwords.words('swedish'):
            t8 = t.encode('utf-8')
            # print(t)
            outfile.write(t)

print('''Filen kan laddas ned <a href="http://digitalametoder.science/results/''' + randomfilename + '''.txt">här</a> (högerklicka och välj "spara som")  och sedan öppnas med spara som .txt.''')









