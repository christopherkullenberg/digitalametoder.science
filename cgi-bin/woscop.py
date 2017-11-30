#!/usr/bin/python3

import cgi, os
import cgitb; cgitb.enable()
import csv

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']
fileitem2 = form['filename2']

# Test if the file was uploaded
if fileitem.filename:
   fn = os.path.basename(fileitem.filename)
   open('upload/' + fn, 'wb').write(fileitem.file.read())

   message = '<p>The file "' + fn + '" was uploaded successfully</p>'
   
else:
   message = 'No file was uploaded'


if fileitem2.filename:
   fn2 = os.path.basename(fileitem2.filename)
   open('upload/' + fn2, 'wb').write(fileitem2.file.read())

   message2 = '<p>The file "' + fn2 + '" was uploaded successfully</p>'

else:
   message2 = 'No file was uploaded'

   
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
""" + message + message2)






"""
thefile = open("upload/" + fn, 'r', encoding="utf-8")
tsv = csv.reader(thefile, delimiter='\t')
next(tsv) #remove headers

"""


import csv
import re


scopuscsv = open("upload/" + fn,'r', encoding="utf-8") # change file-name here
scopusdata = csv.reader(scopuscsv, delimiter=',', quotechar='"')

wostsv = open("upload/" + fn2, 'r', encoding="utf-8")
wosdata = csv.reader(wostsv, delimiter='\t')

#For debugging only, verify with your original download of records.
scopuscount = 0
woscount = 0

recordlist = [] #Holds the extracted data from the loops
therecords = {} #Takes the duplicate check string as key and the rest of the data as value

#Loops to extract the duplicate check string and the desired fields in the data.
for s in scopusdata:
    scopuscount += 1 #Just to count
    #print(s[0]) #print whatever you want to add. See headers in the csv file
    stitlelowered = s[1].lower() #just making lower cases
    ssplitted = stitlelowered.split() #split up the words in the title
    sfirstsevenwords = ssplitted[0:6] # add only the first seven words to avoid dual language titles
    sjoined = ''.join(sfirstsevenwords) # join back again.
    stitlenonspecialchar = re.sub(r'[^A-Za-z0-9]+',r'',sjoined) # remove everything except words and numbers
    recordlist.append([stitlenonspecialchar, s[0], s[2], s[1], s[2], s[3], s[4]]) # put everything you want in a list

for w in wosdata:
    woscount += 1
    #print(w)
    #print(w[1])
    titlelowered = w[8].lower()
    splitted = titlelowered.split()
    firstsevenwords = splitted[0:6]
    joined = ''.join(firstsevenwords)
    titlenonspecialchar = re.sub(r'[^A-Za-z0-9]+',r'',joined)
    recordlist.append([titlenonspecialchar, w[1], w[44], w[8], w[9], w[45], w[46]])

# Takes the duplicate check string as a key in the dictionary and the rest as value
for r in recordlist:
    therecords.update({r[0]: [r[1], r[2], r[3], r[4], r[5], r[6]]})

# This removes duplicates by adding only if the duplicate checker does NOT exist in the result dict.
result = {}
for key, value in therecords.items():
        if key not in list(result.values()):
            result[key] = value

# Open and write to a new csv.
savedir = '/home/chrisk/tools.christopherkullenberg.se/public_html/download/'
with open(savedir + fn + fn2 + ".csv", 'w', encoding="utf-8") as csvfile:
    fieldnames = ['Author', 'Year', 'Title', 'Journal', 'Volume', 'Issue'] #add here whatever you need
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quotechar='"')
    writer.writeheader()
    for key, value in sorted(result.items()):
        #print(value[0])
        writer.writerow({'Author': value[0], 'Year': value[1], 'Title': value[2], 'Journal': value[3], 'Volume': value[4], 'Issue': value[5]}) # Then add here also

numberofduplicates = ((int(scopuscount) - 1) + (int(woscount) - 1)) - int(len(therecords))

#Print some control information
print("<p>There were originally " + str(scopuscount - 1) + " Scopus records and " + str(woscount - 1) + " WoS records.</p>")
print("<p>" + (str(numberofduplicates)) + " duplicates were excluded, leaving " + str(len(therecords)) + " records.</p>")
print("<p>Writing to file " + str(len(result)) + " records.</p><br><p>CSV file written:</p> ")
print('<p><a href="http://tools.christopherkullenberg.se/download/' + fn + fn2 + '.csv">' + fn + fn2 + ".csv")

print('''
</body>
</html>
''')










