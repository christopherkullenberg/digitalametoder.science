Title: Instagram
Date: 2018-02-27
Category: Sociala medier
Tags: Instagram
Authors: Christopher Kullenberg
Slug: Instagram
Summary: Instruktioner och verktyg för att hämta, processa och visualisera data från Instagram.



## Hämta data med Instagram-scraper
Instagram gillar inte att man hämtar och använder data från deras tjänster. Till
skillnad från Twitter har de väldigt begränsad åtkomst via sitt
[applikationsprogrammeringsgränssnitt](https://sv.wikipedia.org/wiki/Application_Programming_Interface)
så man måste gå en omväg för att hämta data.

När man jobbar med Instagram är det särskilt viktigt att tänka på forskningsetik.
Många konton kan innehålla känslig personlig information och vara självutlämnande
både i bild och skrift. Tänk på anonymisering och tänk på att du i många fall
måste ha samtycke av kontoägaren för att kunna forska.

För att kringgå Instagrams begränsningar kan man använda programmet
[Instagram-scraper](https://github.com/rarcega/instagram-scraper). Det är ett
program som kräver att man har programmeringsspråket Python installerat på
sin dator. Om man har Linux eller Mac så finns detta språk redan installerat,
men om man har Windows så måste man [ladda ned](https://www.python.org/) och installera.

Har man sedan Mac måste man även [installera pip](https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x)
 vilket man enkelt gör med kommandot `sudo easy_install pip` i programmet Terminal.
 I Linux gör man
 på lite olika sätt beroende på distribution, men det kan säkert Linuxanvändare
 klura ut. Instruktioner för Windows kan man [hitta här](https://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows).

 När man har installerat pip skriver man bara `pip install instagram-scraper` i
 Terminal (på vissa system måste man lägga till `sudo` först).

När man har installerat instagram-scraper så kan man använda datorns Terminal
(Mac / Linux) eller Kommandotolk (Windows) för att anropa instagram-scraper.

För att hämta så mycket data som möjligt skriver man:

`instagram-scraper skatteverket --media-metadata --include-location --comments`

I exemplet hämtar jag data från kontot `@skatteverket`. Men det funkar på samma
sätt för alla öppna konton.

Det tar ganska lång tid att hämta många instagram-poster. Ibland får man även ett
litet felmeddelande som frågar:

`(A)bort, (I)gnore, (R)etry or retry (F)orever?`

Då trycker man bara `F` och `enter`.

När hämtningen är klar har man en drös med bildfiler och en fil som heter (i det här
  fallet) `skatteverket.json`. Det är denna fil som innehåller all intressant metadata.


## Omvandla data

### Kalkylark
Ett preliminärt verktyg för att konvertera .json-filen (i exemplet ovan
  `skatteverket.json`) från instagram-scraper
till Excel och CSV finns [här](https://digitalametoder.science/cgi-bin/instagramjsontospreadsheet.py).
Rapportera gärna buggar till christopher punkt kullenberg snabela gu punkt se.
**Observera** att det endast funkar (än så länge) om du har ställt in
instagram-scraper på att samla både comments och location, som i exemplet ovan.

### Nätverk

* För att skapa ett riktat nätverk (directed network) utifrån varje enskild
postning, använd [detta verktyg](https://digitalametoder.science/cgi-bin/instagrampostnetwork.py).



## Analysera data


## Visualisera nätverk med Gephi
