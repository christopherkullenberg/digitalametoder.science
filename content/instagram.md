Title: Instagram
Date: 2018-02-27
Category: Internet
Tags: sociala medier
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

Har man sedan Mac måste man [installera pip](https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x)
 vilket man enkelt gör med kommandot `sudo easy_install pip`. I Linux gör man
 på lite olika sätt beroende på distribution, men kan säkert Linuxanvändare
 klura ut. Instruktioner för Windows kan man [hitta här](https://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows).

 När man har installerat pip skriver man bara `pip install instagram-scraper` (på vissa
   system måste man lägga till `sudo` först).




## Omvandla data

Ett preliminärt verktyg för att konvertera .json-filen från instagram-scraper
till Excel och CSV finns [här](https://digitalametoder.science/cgi-bin/instagramjsontospreadsheet.py).
Rapportera gärna buggar till christopher punkt kullenberg snabela gu punkt se.
**Observera** att det endast funkar (än så länge) om du har ställt in
instagram-scraper på att samla både comments och location.


## Analysera data


## Visualisera nätverk med Gephi
