# -*- coding: utf-8 -*-
"""Google Play Review Scrapper

Usage:
  gpscrap.py --appid=<google-play-application-id>

Options:
  --appid=<app_id>	The ID of the app where the reviews will be scrapped.
"""
from docopt import docopt
import pycurl
from io import BytesIO
from urllib import urlencode
import re
from BeautifulSoup import BeautifulSoup

if __name__ == '__main__':
	arguments = docopt(__doc__, version='Google Play Review Scrapper V1.0')
	
	application_id = arguments["--appid"]

	buffer = BytesIO()
	c = pycurl.Curl()

	c.setopt(c.URL, 'https://play.google.com/store/getreviews?authuser=0')
	c.setopt(c.ENCODING, 'gzip,deflate')

	post_data = {'reviewType': '0', 'pageNum': '2', 'id': application_id, 'reviewSortOrder': '0', 'xhr': '1', 'token': 'FxkOaC8-kGnB-duj_Zcc3H7BRow%3A1448462501595', 'hl': 'pt_BR'} 
	postfields = urlencode(post_data)

	c.setopt(c.POSTFIELDS, postfields)
	c.setopt(c.WRITEDATA, buffer)

	c.perform()
	c.close()

	body = buffer.getvalue()

	#you could try this expression here: http://pythex.org/
	filtered = re.match(r'^\)]}\'\s*\[\["ecr",1,(?P<body>"[^"].*"),[0-9]]\s*]', body).group('body')
	
	soup = BeautifulSoup(filtered.decode('unicode-escape'))
	filtered2 = ""
	filtered2 = str(soup.findAll("div",id="review-body"))
	filtered3 = filtered2.replace("<div id=\"review-body\"><spanclass>", "{\"review\": \"")
	filtered4 = filtered3.replace("<div id=\"review-link\" style=\"display:none\"><aclass>Resenhacompleta</aclass></div></spanclass></div>", "\"}")

	print(filtered4)