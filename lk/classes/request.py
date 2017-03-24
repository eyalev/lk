import requests

from lk.classes.response import Response


class Request(object):

    def __init__(self):
        pass

    def get(self, url):

        requests_response = requests.get(url)

        response = Response(requests_response)

        return response
