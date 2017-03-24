from lk.utils.string_util import String


class Response(object):

    def __init__(self, response):
        self._response = response

    @property
    def requests_response(self):
        """
        :rtype: requests.models.Response
        """

        return self._response

    @property
    def content(self):
        return self.requests_response.text

    @property
    def text(self):
        return self.requests_response.text

    @property
    def odict(self):

        text = self.requests_response.text

        odict = String(text).to_odict()

        return odict

    @property
    def pretty_json_string(self):

        content = self.requests_response.content

        result = String(content).to_pretty_json_string()

        return result
