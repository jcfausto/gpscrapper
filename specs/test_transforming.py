# coding=utf-8
from unittest import TestCase
from gputils.gptransformer import GooglePlayParsedResponseTransformer
from json2html import *

class TestTransforming(TestCase):
    __PARSED_RESPONSE = '[<div class=\"review-body\"> <span class=\"review-title\">Galaxy S5</span> Paro de funcionar novamente no Estado do Parana <div class=\"review-link\" style=\"display:none\"> <a class=\"id-no-nav play-button tiny\" href=\"#\" target=\"_blank\">Resenha completa</a> </div> </div>]'
    __EXPECTED_JSON = u'{\n    "reviews": [\n        {\n            "review": "Galaxy S5 Paro de funcionar novamente no Estado do Parana "\n        }\n    ]\n}'
    __EXPECTED_HTML = u'<table border="1"><tr><th>reviews</th><td><ul><li><table border="1"><tr><th>review</th><td>Galaxy S5 Paro de funcionar novamente no Estado do Parana </td></tr></table></li></ul></td></tr></table>'

    def test_can_transform_parsed_content_into_json_formatted_output(self):
        """
        Should be able to transform parsed content to a json formatted string
            Hint: If this fails there are chances that google changed the html response structure.
        """
        transformer = GooglePlayParsedResponseTransformer(self.__PARSED_RESPONSE)
        json = transformer.transform()
        self.assertEqual(json, self.__EXPECTED_JSON)

    def test_can_output_content_as_html(self):
        """
        Should be able to transform a json transformed content into html content
        """
        transformer = GooglePlayParsedResponseTransformer(self.__PARSED_RESPONSE)
        json = transformer.transform()
        json = json2html.convert(json = json)
        self.assertEqual(json, self.__EXPECTED_HTML)
