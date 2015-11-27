# -*- coding: utf-8 -*-
"""
Google Play Review Scrapper

Usage:
  gpscrap.py --appid=<google-play-application-id> --pagenum=<page_num> [--format=<json_or_html>]

Options:
  --appid=<app_id>	        The ID of the app where the reviews will be scrapped.
  --page=<page_num>         The review page number.
  --format=<json_or_html>   Optional parameter. Specifies the output format that could be json html. Outputs json by default.
"""
from docopt import docopt

from gpengine.scrapengine import ScrapEngine
from gputils.gpparser import GooglePlayResponseParser
from gputils.gptransformer import GooglePlayParsedResponseTransformer

#to generate the html output
from json2html import *

if __name__ == '__main__':
	arguments = docopt(__doc__, version='Google Play Review Scrapper V1.0')
	application_id = arguments["--appid"]
	page_number = arguments["--pagenum"]
	output_format = arguments["--format"]

	scrapper = ScrapEngine(application_id, page_number)

	response = scrapper.go()

	gpfilter = GooglePlayResponseParser(response)
	parsed_response = gpfilter.parseResponse()

	gpjsongen = GooglePlayParsedResponseTransformer(parsed_response)

	json = gpjsongen.transform()

	if output_format == "html":
		json = json2html.convert(json = json)

	print(json)