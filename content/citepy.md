Title: Citepy
Date: 2017-11-11
Category: Vetenskap
Tags: bibliometri, Python
Authors: Christopher Kullenberg
Slug: citepy
Summary: Web of Science.

## Web of Science

Export a .tsv file from Web of Science as "Mac Tab delimited UTF-8" as character encoding, then upload.

The source code for cite.py can be found at <https://github.com/christopherkullenberg/digitalametoder.science/blob/master/cgi-bin/cite.py>.

<form enctype="multipart/form-data" action="cgi-bin/cite.py" method="post">
	<input type="file" name="filename" />
	<input type="submit" value="Upload Web of Science TSV file" />
</form>