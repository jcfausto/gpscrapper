# -*- coding: utf-8 -*-
"""Google Play Review Scrapper

Usage:
  gpscrap.py --appid=<google-play-application-id> --pagenum=<page_num>

Options:
  --appid=<app_id>	The ID of the app where the reviews will be scrapped.
  --page=<page_num> The review page number.
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
	page_number = arguments["--pagenum"]

	buffer = BytesIO()
	c = pycurl.Curl()

	c.setopt(c.URL, 'https://play.google.com/store/getreviews?authuser=0')
	c.setopt(c.ENCODING, 'gzip,deflate')

	post_data = {'reviewType': '0', 'pageNum': page_number, 'id': application_id, 'reviewSortOrder': '0', 'xhr': '1', 'token': 'FxkOaC8-kGnB-duj_Zcc3H7BRow%3A1448462501595', 'hl': 'pt_BR'} 
	postfields = urlencode(post_data)

	c.setopt(c.POSTFIELDS, postfields)
	c.setopt(c.WRITEDATA, buffer)

	c.perform()
	c.close()

	body = buffer.getvalue()

	#you could try this expression here: http://pythex.org/
	filtered = re.match(r'^\)]}\'\s*\[\["ecr",1,(?P<body>"[^"].*"),[0-9]]\s*]', body).group('body')
	converted = filtered.decode('unicode-escape')

	soup = BeautifulSoup(converted)
	review_bodies = str(soup.findAll("div", {"class": "review-body"}))
		
	json_start = review_bodies.replace("<div class=\"review-body\"> <span class=\"review-title\">", "{\"review\": \"")
	json_end = json_start.replace("<div class=\"review-link\" style=\"display:none\"> <a class=\"id-no-nav play-button tiny\" href=\"#\" target=\"_blank\">Resenha completa</a> </div> </div>", "\"}")
	json_final = json_end.replace("</span>", "")

	print(json_final)