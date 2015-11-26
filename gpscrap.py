# -*- coding: utf-8 -*-
"""Google Play Review Scrapper

Usage:
  gpscrap.py --appid=<google-play-application-id> --pagenum=<page_num>

Options:
  --appid=<app_id>	The ID of the app where the reviews will be scrapped.
  --page=<page_num> The review page number.
"""
from docopt import docopt
from scrapengine import ScrapEngine
import re
from BeautifulSoup import BeautifulSoup

if __name__ == '__main__':
	arguments = docopt(__doc__, version='Google Play Review Scrapper V1.0')
	application_id = arguments["--appid"]
	page_number = arguments["--pagenum"]

	scrapper = ScrapEngine(application_id, page_number)

	body = scrapper.go()

	#you could try this expression here: http://pythex.org/
	filtered = re.match(r'^\)]}\'\s*\[\["ecr",1,(?P<body>"[^"].*"),[0-9]]\s*]', body).group('body')
	converted = filtered.decode('unicode-escape')

	soup = BeautifulSoup(converted)
	review_bodies = str(soup.findAll("div", {"class": "review-body"}))
		
	json_start = review_bodies.replace("<div class=\"review-body\"> <span class=\"review-title\">", "{\"review\": \"")
	json_end = json_start.replace("<div class=\"review-link\" style=\"display:none\"> <a class=\"id-no-nav play-button tiny\" href=\"#\" target=\"_blank\">Resenha completa</a> </div> </div>", "\"}")
	json_final = json_end.replace("</span>", "")

	print(json_final)