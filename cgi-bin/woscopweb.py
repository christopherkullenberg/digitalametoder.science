#!/usr/bin/python3
import sys
import cgi
import os
# import cgitb
import csv
from printhtml import printwoscop
from werkzeug import secure_filename
import re
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

form = cgi.FieldStorage()
# Get filename here.
try:
    fileitem = form['filename']
    fileitem2 = form['filename2']
except KeyError:  # if no file, just print first page.
    printwoscop()
    print("<p>No files loaded...</p>")
    sys.exit()

# Test if the file was uploaded
if fileitem.filename:
    securefn = secure_filename(fileitem.filename)
    fn = os.path.basename(securefn)
    open('upload/' + fn, 'wb').write(fileitem.file.read())
    message = '<p>The file "' + fn + '" was uploaded successfully</p>'
    # print(fn)

else:
    message = 'No file was uploaded'
    print("content-type:text/html; charset=utf-8\r\n\r\n")
    print()
    print('Please load files...')


if fileitem2.filename:
    securefn2 = secure_filename(fileitem2.filename)
    fn2 = os.path.basename(securefn2)
    open('upload/' + fn2, 'wb').write(fileitem2.file.read())

    message2 = '<p>The file "' + fn2 + '" was uploaded successfully</p>'
    # print(fn2)

else:
    message2 = 'No file was uploaded'
    print("content-type:text/html; charset=utf-8\r\n\r\n")
    print()
    print('No file was uploaded')


scopuscsv = open("upload/" + fn, 'r', encoding="utf-8")  # change file-name here
scopusdata = csv.reader(scopuscsv)

wostsv = open("upload/" + fn2, 'r', encoding="utf-8")
wosdata = csv.reader(wostsv, delimiter='\t')

# For debugging only, verify with your original download of records.
scopuscount = 0
woscount = 0

recordlist = [] # Holds the extracted data from the loops
therecords = {} # Takes the duplicate check string as key and the rest of the data as value

# Loops to extract the duplicate check string and the desired fields in the data.
for s in scopusdata:
    scopuscount += 1 # Just to count
    # print(s[0]) #print whatever you want to add. See headers in the csv file
    stitlelowered = s[1].lower() # just making lower cases
    ssplitted = stitlelowered.split() # split up the words in the title
    sfirstsevenwords = ssplitted[0:6] # add only the first seven words to avoid dual language titles
    sjoined = ''.join(sfirstsevenwords) # join back again.
    stitlenonspecialchar = re.sub(r'[^A-Za-z0-9]+',r'',sjoined) # remove everything except words and numbers
    recordlist.append([stitlenonspecialchar, s[0], s[2], s[1], s[2], s[3], s[4]]) # put everything you want in a list

for w in wosdata:
    woscount += 1
    # print(w)
    # print(w[1])
    titlelowered = w[8].lower()
    splitted = titlelowered.split()
    firstsevenwords = splitted[0:6]
    joined = ''.join(firstsevenwords)
    titlenonspecialchar = re.sub(r'[^A-Za-z0-9]+', r'', joined)
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
savedir = '/home/chrisk/digitalametoder.science/results/'
with open(savedir + fn + fn2 + ".csv", 'w', encoding="utf-8") as csvfile:
    fieldnames = ['Author', 'Year', 'Title', 'Journal', 'Volume', 'Issue'] # add here whatever you need
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quotechar='"')
    writer.writeheader()
    for key, value in sorted(result.items()):
        #print(value[0])
        writer.writerow({'Author': value[0], 'Year': value[1], 'Title': value[2],
        'Journal': value[3], 'Volume': value[4], 'Issue': value[5]}) # Then add here also
numberofduplicates = ((int(scopuscount) - 1) + (int(woscount) - 1)) - int(len(therecords))
# Print some control information

printwoscop()
print("<p>There were originally " + str(scopuscount - 1) + " Scopus records and " + str(woscount - 1) + " WoS records.</p>")
print("<p>" + (str(numberofduplicates)) + " duplicates were excluded, leaving " + str(len(therecords)) + " records.</p>")
print("<p>Writing to file " + str(len(result)) + " records.</p><br><p>CSV file written:</p> ")
print('<p><a href="http://digitalametoder.science/results/' + fn + fn2 + '.csv">' + fn + fn2 + ".csv")

print('''
</body>
</html>
''')
