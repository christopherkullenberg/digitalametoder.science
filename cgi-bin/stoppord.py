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

for t in tknzr:
    if t not in stopwords.words('swedish'):
        print(t)









