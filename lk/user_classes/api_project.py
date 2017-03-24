import requests

from lk.classes.request import Request
from lk.classes.response import Response


class APIProject(object):

    def __init__(self):

        self._host = 'http://localhost:8080'

        self._admin_cookie = None

    @property
    def host(self):

        return self._host

    def get_users_json_string(self):

        url = '{host}/team/api_users'.format(host=self.host)

        response_raw = self.admin_request(url)

        response = Response(response_raw)

        # import ipdb; ipdb.set_trace()
        return response.pretty_json_string

    def reset_db_data(self):

        url = '{host}/local/seed_data?clear_db=true'.format(host=self.host)

        response = Request().get(url)

        return response.pretty_json_string

    def admin_request(self, path, options=None):
        """
        Example: response = self.admin_request('/manage/meta')

        :returns Response (from requests lib)
        """

        # http://localhost:2080/_ah/login?email=test_admin%40example.com&admin=True&action=Login
        # http://localhost:8080/_ah/login?email=test_admin%40example.com&admin=True&action=Login
        # http://localhost:8080/_ah/login?email=test_admin%40example.com&admin=True&action=Login&continue=
        # url = '{host}/_ah/login?email=test_admin%40example.com&admin=True&action=Login'.format(host=self.host)
        url = 'http://localhost:8080/_ah/login?email=test_admin%40example.com&admin=True&action=Login'

        if not self._admin_cookie:
            response = requests.get(
                url,
                allow_redirects=False
            )
            self._admin_cookie = response.cookies['dev_appserver_login']

        admin_options = {'cookies': {'dev_appserver_login': self._admin_cookie}}

        if options:
            admin_options.update(options)

        # return requests.get(path, admin_options)
        return requests.get(path, cookies=admin_options['cookies'])

