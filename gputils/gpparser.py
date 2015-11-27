# -*- coding: utf-8 -*-
import re
from BeautifulSoup import BeautifulSoup

class GooglePlayResponseParser(object):

    def __init__(self, response):
        self.response = response

    def parseResponse(self):
        """
        You could try this expression here: http://pythex.org/.
        This regular expression grabs only the relevant content containing the reviews.
        The content is decoded from unicode to utf-8
        :return:string
        """
        response_filtered = re.match(r'^\)]}\'\s*\[\["ecr",1,(?P<content>"[^"].*"),[0-9]]\s*]', self.response).group('content')

        response_converted = response_filtered.decode('unicode-escape').encode('UTF-8', errors='ignore')

        soup = BeautifulSoup(response_converted)
        return str(soup.findAll("div", {"class": "review-body"}))