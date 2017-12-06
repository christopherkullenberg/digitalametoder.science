# Source code: digitalametoder.science

This is a repository of all the code used to build
[digtalametoder.science](http://digitalametoder.science).

## Installation

To run site on a web server, please configure Apache to run Python cgi scripts in the `cgi-bin` directory. Also, make sure you have all Python dependencies installed (I will make a list soon).

This frontend is based on the [3 Col Portfolio Bootstrap template](https://github.com/BlackrockDigital/startbootstrap-3-col-portfolio) by Startbootstrap, Blackrock Digital LLC, created by David Miller.

The backend is based on [Pelican](http://getpelican.com/) static web site generator. 

## Install Pelican

1. Install [pelican](http://docs.getpelican.com/en/stable/quickstart.html): `pip install pelican markdown`
2. Create directory for web site:
	```r
	mkdir digitalametoder.science
	cd digitalametoder.science
	```
3. Create project: `pelican-quickstart`

## Create content

Create a new [Markdown](https://en.wikipedia.org/wiki/Markdown) file and place it in the `/content` directory.

Put the metadata in the file header, and the content after.

Note that the `slug` is used both as the file name (e.g., `twitter.html`) and image name. In this case, `Slug: twitter` will automatically look for the image `twitter.png` in the `/images` directory.

```md
Title: Twitterdata
Date: 2017-12-05
Category: Internet
Tags: sociala medier
Authors: Christopher Kullenberg
Slug: twitter
Summary: Instruktioner och verktyg för att hämta, processa och visualisera data från Twitter.

Det finns många sätt att hämta och analysera data från Twitter. På denna sida finns instruktioner för verktygen TAGS, för att hämta data, och sedan Gephi, som används för att visualisera datan. Fler metoder för både insamling och analys kommer inom kort.

## Hämta Twitterdata med TAGS

TAGS är ett tillägg till Google [...]
```

## Generate web site

To generate HTML web pages, type `pelican content`.

The content is stored in the the `/output` directory.
