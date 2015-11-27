# -*- coding: utf-8 -*-
import json

class GooglePlayParsedResponseTransformer(object):

    """
    Those are the necessary replacements on a parsed response in order to generate a json formatted output
    """
    __FIRST_TRANSFORMATION_RULE = ["<div class=\"review-body\"> <span class=\"review-title\">", "{\"review\": \""]
    __SECOND_TRANSFORMATION_RULE = ["<div class=\"review-link\" style=\"display:none\"> <a class=\"id-no-nav play-button tiny\" href=\"#\" target=\"_blank\">Resenha completa</a> </div> </div>", "\"}"]
    __THIRD_TRANSFORMATION_RULE = ["</span>", ""]

    #TO-DO: this should be an array or set.
    __CHARACTER_TRANSFORMATION_ONE = ["Ã£", "ã"]
    __CHARACTER_TRANSFORMATION_TWO = ["Ãº", "ú"]
    __CHARACTER_TRANSFORMATION_THREE = ["Ã§", "ç"]
    __CHARACTER_TRANSFORMATION_FOUR = ["Ãµ", "õ"]
    __CHARACTER_TRANSFORMATION_FIVE = ["Ã¡", "á"]
    __CHARACTER_TRANSFORMATION_SIX = ["Ã­", "í"]
    __CHARACTER_TRANSFORMATION_SEVEN = ["Ã³", "ó"]
    __CHARACTER_TRANSFORMATION_EIGHT = ["Ãªs", "ó"]


    """Constructor"""
    def __init__(self, parsed_content_from_google_play_response_parser):
        self.parsed_content = parsed_content_from_google_play_response_parser
        self.transformed_content = ""

    """
    This method do the transformation
    :return:json
    """
    def transform(self):
        self.__apply_transformation(self.parsed_content, self.__FIRST_TRANSFORMATION_RULE)\
            .__apply_transformation(self.transformed_content, self.__SECOND_TRANSFORMATION_RULE)\
            .__apply_transformation(self.transformed_content, self.__THIRD_TRANSFORMATION_RULE)\
            .__apply_transformation(self.transformed_content, self.__CHARACTER_TRANSFORMATION_ONE)\
            .__apply_transformation(self.transformed_content, self.__CHARACTER_TRANSFORMATION_TWO)\
            .__apply_transformation(self.transformed_content, self.__CHARACTER_TRANSFORMATION_THREE)\
            .__apply_transformation(self.transformed_content, self.__CHARACTER_TRANSFORMATION_FOUR)\
            .__apply_transformation(self.transformed_content, self.__CHARACTER_TRANSFORMATION_FIVE)\
            .__apply_transformation(self.transformed_content, self.__CHARACTER_TRANSFORMATION_SIX)\
            .__apply_transformation(self.transformed_content, self.__CHARACTER_TRANSFORMATION_SEVEN)\
            .__apply_transformation(self.transformed_content, self.__CHARACTER_TRANSFORMATION_EIGHT)

        # finishing the json format
        self.transformed_content = "{\"reviews\": "+self.transformed_content+"}"

        the_json = json.loads(self.transformed_content)
        return json.dumps(the_json, indent=4, sort_keys=True).decode('unicode-escape')

    #private methods

    """
    This method applies the replacements necessary to generate a json formatted output and store it at
    transformed_content attribute.
    :return:self
    """
    def __apply_transformation(self, content_to_be_transformed, transformation_rule):
        self.transformed_content = content_to_be_transformed.replace(transformation_rule[0], transformation_rule[1])
        return self
