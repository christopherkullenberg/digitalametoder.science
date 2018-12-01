Title: Norrköping Workshop
Date: 2017-11-10
Category: Workshop
Tags: bibliometri, Gephi
Authors: Christopher Kullenberg
Slug: nkpg
Summary: 

## Useful links and external resources.

- <a href="http://www.roundabout.se/scientometrics/nkpg/">Gustaf's page</a> (additional data)
- <a href="http://webofknowledge.com">Web of Science scientometric database</a>
- <a href="http://scopus.com">Scopus</a> scientometric database
- Altmetric <a href="https://www.altmetric.com/blog/scoreanddonut/">documentation</a> on score calculation

## Valuation practice 1: Citations vs. Altmetrics

There are many value meters in the assesment of scientific publications. The most common two are citations and altmetrics. Here are instructions for how to calculate and visualise both value meters.

[Launch tool](/cgi-bin/altmetric.py)

## QualCite practice: "Measuring welfare" dataset.

This is the methological source material and digital method
toolbox used for the article <a href="http://valuationstudies.liu.se/Issues/articles/default.asp?DOI=10.3384/VS.2001-5992.17517">Measuring Welfare Beyond GDP</a> by Kullenberg and Nelhans.

1. A visual and hyperlinked **overview** of the dataset can be found
<a href="https://scientometrics.flov.gu.se/happiness/map/index.html" target="_blank">here</a>. 	
	- Graphviz source code can be found <a href="https://scientometrics.flov.gu.se/happiness/map/lycka.dot">here</a> (which also can be opened in Gephi).
	- A Gephi file can be found <a href="http://digitalametoder.science/data/lycka.gephi">here</a>
	- and a <code>.gexf</code> file <a href="http://digitalametoder.science/data/lycka.gexf">here</a>.</p>
2. The **source** documents (zip, 147Mb) can be found <a href="https://scientometrics.flov.gu.se/happiness/measuringwelfare.zip" target="_blank">here</a>
3. *'Search** Remisser (<a href="https://github.com/christopherkullenberg/digitalametoder.science/blob/master/cgi-bin/searchremisser.py">source code for search engine</a>)

	<form action="cgi-bin/searchremisser.py" method="post">
	Fulltext search: <input type="text" name="like_search_word"> <input type="submit" value="Sök" />

	Method:
	<input type="radio" name="mode" value="like" checked /> Like (recommended)
	<input type="radio" name="mode" value="match" /> Match
	<input type="radio" name="mode" value="regexp" /> Regexp
	
	Order:
	<input type="radio" name="order" value="Stigande" checked /> Ascending
	<input type="radio" name="order" value="Fallande" /> Descending</p>
	</form>


## Valuation practice 2: "Valuation of Valuation Studies Journal"

Under construction.

This excercise extracts all the articles and their cited articles
from the Journal of Valuation Studies (source code for the scraper
can be found <a href="https://github.com/christopherkullenberg/ValuationStudiesScraper">here</a>)
. Then we run these through scholarly citation databases as well as Altmetrics

**Data**

The datafiles below can be run through the <a href="http://digitalametoder.science/cgi-bin/altmetric.py">Altmetric</a> tool.

- <a href="/data/VSdoi.txt">Valuation Studies, all DOIs, plain text file</a>
- <a href="/data/VSreferencesDOIS.txt">Valuation Studies, all reference list DOIs (cited references) except self references to journal, plain text file</a>
- <a href="/data/VSselfreferencesDOIs.txt">Valuation Studies, all references to own journal, DOIs, plain text file</a>