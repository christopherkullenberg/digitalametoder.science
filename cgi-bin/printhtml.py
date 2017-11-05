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
