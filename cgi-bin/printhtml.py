def printrtnetwork():
    print("content-type:text/html; charset=utf-8\r\n\r\n")
    print()
    print('''
        <!DOCTYPE html>
        <html lang="sv">

          <head>

            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <meta name="description" content="">
            <meta name="author" content="">

            <title>Digitala metoder: Retweetnätverk</title>

                <!-- Bootstrap core CSS -->
                <link href="http://digitalametoder.science/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

                <!-- Custom styles for this template -->
                <link href="http://digitalametoder.science/css/3-col-portfolio.css" rel="stylesheet">

              </head>

              <body>
    <div id="container">
     <main>
        <h1>Skapa RT-nätverk</h1>
        <p>För instruktioner, se <a href="https://youtu.be/Dfz9e0KOzCU">denna video</a></p>
	<p><b>OBS: filnamnen får inte innehålla specialtecken</b>. Godkänt filnamn är ex. <code>fil.csv</code>. Välj gärna ett unikt och specifikt filnamn, ex. <code>christophersdata.csv</code></p>
        <p>Exportera till csv fil i Google Calc/TAGS och ladda upp:</p>
        <form enctype="multipart/form-data"
                         action="rtnetwork.py" method="post">
         <br><input type="file" name="filename" />
         <input type="submit" value="Ladda upp" />

        <br><br>

        <p>Om du har fått en .csv-fil av Christoher, ladda upp här:</p>
        <form enctype="multipart/form-data"
                         action="rtnetwork.py" method="post">
         <br><input type="file" name="filename2" />
         <input type="submit" value="Ladda upp" />

         <br><br>
         <p>Källkoden till detta verktyg finns <a href="https://github.com/christopherkullenberg/digitalametoder.science/blob/master/cgi-bin/rtnetwork.py">här</a>.</p>
        <br>
        </section>
     </main>
   </div>
    ''')

def printmentionsnetwork():
    print("content-type:text/html; charset=utf-8\r\n\r\n")
    print()
    print('''
    <!DOCTYPE html>
    <html lang="sv">

      <head>

        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta name="description" content="">
        <meta name="author" content="">

        <title>Digitala metoder: Mentions network</title>

            <!-- Bootstrap core CSS -->
            <link href="http://digitalametoder.science/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

            <!-- Custom styles for this template -->
            <link href="http://digitalametoder.science/css/3-col-portfolio.css" rel="stylesheet">

          </head>

          <body>

    <div id="container">
     <main>
        <h1>Skapa Mentions-nätverk</h1>
        <p>För instruktioner, se <a href="https://youtu.be/yeBxoT7uTdQ">denna video</a></p>
	<p><b>OBS: filnamnen får inte innehålla specialtecken</b>. Godkänt filnamn är ex. <code>fil.csv</code>. Välj gärna ett unikt och specifikt filnamn, ex. <code>christophersdata.csv</code></p>
        <p>Exportera till csv fil i Google Calc/TAGS och ladda upp:</p>
        <form enctype="multipart/form-data"
                         action="mentionsnetwork.py" method="post">
         <br><input type="file" name="filename" />
         <input type="submit" value="Ladda upp" />

        <br><br>

        <p>Om du har fått en .csv-fil av Christoher, ladda upp här:</p>
        <form enctype="multipart/form-data"
                         action="mentionsnetwork.py" method="post">
         <br><input type="file" name="filename2" />
         <input type="submit" value="Ladda upp" />


         <br><br>
         <p>Källkoden till detta verktyg finns <a href="https://github.com/christopherkullenberg/digitalametoder.science/blob/master/cgi-bin/mentionsnetwork.py">här</a>.</p>

        <br>
        </section>
     </main>
   </div>
    ''')

def printtimemessages():
    print("content-type:text/html; charset=utf-8\r\n\r\n")
    print()
    print('''
        <!DOCTYPE html>
        <html lang="sv">

          <head>

            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <meta name="description" content="">
            <meta name="author" content="">

            <title>Digitala metoder</title>

                <!-- Bootstrap core CSS -->
                <link href="http://digitalametoder.science/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

                <!-- Custom styles for this template -->
                <link href="http://digitalametoder.science/css/3-col-portfolio.css" rel="stylesheet">

              </head>

              <body>
    <div id="container">
     <main>
        <h1>Analysera meddelandens tidsstämplar</h1>
	<p><b>OBS: filnamnen får inte innehålla specialtecken</b>.<br> Godkänt filnamn är ex. <code>fil.csv</code>.
    <br>Välj gärna ett unikt och specifikt filnamn, ex. <code>christophersdata.csv</code></p>
        <h3>A. Twitter/TAGS</h3>
        <p>Exportera till csv-fil i Google Calc/TAGS och ladda upp:</p>
        <form enctype="multipart/form-data"
                         action="timemessages.py" method="post">
         <br><input type="file" name="filename" />
         <input type="submit" value="Ladda upp" />

        <br><br>

        <h3>B. Facebook/Netvizz</h3>
        <p>Om du har en csv-fil som samlats in med Netvizz, ladda upp här:</p>
        <form enctype="multipart/form-data"
                         action="timemessages.py" method="post">
         <br><input type="file" name="filename2" />
         <input type="submit" value="Ladda upp" />

        <br>
        </section>
     </main>
   </div>
    ''')


def printaltmetric():
    print("content-type:text/html; charset=utf-8\r\n\r\n")
    print()
    print('''
        <!DOCTYPE html>
        <html lang="sv">

          <head>

            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <meta name="description" content="">
            <meta name="author" content="">

            <title>Digitala metoder</title>

                <!-- Bootstrap core CSS -->
                <link href="http://digitalametoder.science/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

                <!-- Custom styles for this template -->
                <link href="http://digitalametoder.science/css/3-col-portfolio.css" rel="stylesheet">

              </head>

              <body>
    <div id="container">
     <main>
        <h1>Analyzing altmetric scores </h1>
        <p>This tool uses data from the <a href="https://www.altmetric.com/">Altmetric</a> API.</p>

	    <p>Please use a unique file name without special characters, for example <code>christophersdata.csv</code></p>

        <p>This tool is currently limited to 100 requests to the Altmetric API to
        to prevent overloading it. Longer files will only make requests for the
        100 first records.</p>

        <p>Please be patient, fetching records might take some time.</p>

        <h3>A. Web of Science</h3>
        <p>Export a .tsv file from Web of Science,  "Mac Tab delimited UTF-8" as character encoding.</p>
        <form enctype="multipart/form-data"
                         action="altmetric.py" method="post">
         <br><input type="file" name="filename" />
         <input type="submit" value="Upload Web of Science TSV file" />

        <br><br>

        <h3>B. Scopus</h3>
        <p>Export search results from Scopus as CSV file.</p>
        <form enctype="multipart/form-data"
                         action="altmetric.py" method="post">
         <br><input type="file" name="filename2" />
         <input type="submit" value="Upload Scopus CSV file" />

        <br>

        <h3>C. From list of DOIs</h3>
        <p>Save DOI numbers in a plain text file. Delimit each DOI with a newline (one DOI per line)</p>
        <form enctype="multipart/form-data"
                         action="altmetric.py" method="post">
         <br><input type="file" name="filename3" />
         <input type="submit" value="Upload textfile with DOIs" />

        <br>
        </section>
     </main>
   </div>
    ''')

def printwoscop():
    print("content-type:text/html; charset=utf-8\r\n\r\n")
    print()
    print('''
        <!DOCTYPE html>
        <html lang="sv">

          <head>

            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <meta name="description" content="">
            <meta name="author" content="">

            <title>Digitala metoder: Woscop</title>

                <!-- Bootstrap core CSS -->
                <link href="http://digitalametoder.science/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

                <!-- Custom styles for this template -->
                <link href="http://digitalametoder.science/css/3-col-portfolio.css" rel="stylesheet">

              </head>

              <body>

              <p>This tool takes a Web of Science tsv file (Mac, UTF-8) and
              a Scopus csv file and merges them, removing duplicates.</p>

              <p>The source code for this tool can be found <a href="https://github.com/christopherkullenberg/digitalametoder.science/blob/master/cgi-bin/woscopweb.py">here</a>.</p>

              <div id="container">
              <main>
           <form enctype="multipart/form-data"
                         action="woscopweb.py" method="post">
         <p>Scopus file (<b>csv</b>):<br><input type="file" name="filename" /></p>
         <p>Web of Science file (<b>tsv</b>):<br><input type="file" name="filename2" /></p>
         <p><input type="submit" value="Upload" /></p>
       </form>


     </main>
   </div>
    ''')

def printkeywordstogexf():
        print("content-type:text/html; charset=utf-8\r\n\r\n")
        print()
        print('''
            <!DOCTYPE html>
            <html lang="sv">

              <head>

                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <meta name="description" content="">
                <meta name="author" content="">

                <title>Digitala metoder: Keywords to Gexf</title>


  <h3>File conversion: Keyword co-occurrence network</h3>
     <p>Create a keyword co-occurrence network from Web of Science data.</p>
     <p>Edges are drawn between keywords that co-occur within an article.</p>
     <p>Upload a tab-separated file (tsv) that has been exported from the Web
        of Science and get a gexf network file back. Gexf files can then be
        opened and visualized with <a href="https://gephi.org">Gephi</a>.</p>

        <p>The source code for this application can be found <a href="https://github.com/christopherkullenberg/digitalametoder.science/blob/master/cgi-bin/keywordstogexf.py">here</a></p>


       <form enctype="multipart/form-data"
                         action="keywordstogexf.py" method="post">
       <p><input type="file" name="filename" /><input type="submit" value="Upload" /></p>
       </form>


     </main>
   </div>
    ''')

def printinstagramparser():
        print("content-type:text/html; charset=utf-8\r\n\r\n")
        print()
        print('''
            <!DOCTYPE html>
            <html lang="sv">

              <head>

                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <meta name="description" content="">
                <meta name="author" content="">

                <title>Instagram - Konvertera data</title>



        <p>Källkoden finns här <a href="https://github.com/christopherkullenberg/digitalametoder.science/blob/master/cgi-bin/instagramjsontospreadsheet.py">here</a></p>

        <p> Läser en json-fil från instagram-scraper som innehåller både comments och location-data.
        Returnerar Excel och CSV-filer. Observera att det endast funkar (än så länge) om du har ställt in
        instagram-scraper på att samla både comments och location.</p>

       <form enctype="multipart/form-data"
                         action="instagramjsontospreadsheet.py" method="post">
       <p><input type="file" name="filename" /><input type="submit" value="Ladda upp" /></p>
       </form>


     </main>
   </div>
    ''')
