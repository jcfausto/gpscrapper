import pycurl
from io import BytesIO
from urllib import urlencode

class ScrapEngine(object):

    def __init__(self, application_id, page_number_to_scrap):
        self.application_id = application_id
        self.page_number_to_scrap = page_number_to_scrap
        self.buffer = BytesIO()
        self.c = pycurl.Curl()

    def setup(self):
        self.c.setopt(self.c.URL, 'https://play.google.com/store/getreviews?authuser=0')
        self.c.setopt(self.c.ENCODING, 'gzip,deflate')

        post_data = {'reviewType': '0', 'pageNum': self.page_number_to_scrap, 'id': self.application_id, 'reviewSortOrder': '0', 'xhr': '1', 'token': 'FxkOaC8-kGnB-duj_Zcc3H7BRow%3A1448462501595', 'hl': 'pt_BR'}
        postfields = urlencode(post_data)

        self.c.setopt(self.c.POSTFIELDS, postfields)
        self.c.setopt(self.c.WRITEDATA, self.buffer)

    def go(self):
        self.setup()
        self.c.perform()
        self.c.close()

        return self.buffer.getvalue()