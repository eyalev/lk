import json

# from nose.tools import nottest
# import requests

# from share.classes.api_util import APIUtil
# from share.classes.dict_util import DictUtil
# from share.config import config, app_config, handlers


class TestUtil(object):

    def __init__(self, host_url=None):

        self.host_url = host_url
        self.admin_cookie = None

    # def init_history_module_local_storage(self):
    #
    #     response = self.request('{host}/_ah/gcs/breezometer-gce30-datagrid-isr/201506010100/29.json'.format(
    #         host=config.history_test_server_url
    #     ))
    #
    #     if response.status_code != 200:
    #
    #         self.request(APIUtil().local_history_url() + '/local/storage/load_files')
    #         self.request(APIUtil().local_history_url() + '/local/helpers/create_test_key/')

    # def request(self, path, options=None, _host_url=None, method='get'):
    #
    #     if options is None:
    #         options = {}
    #
    #     if path.startswith('http://'):
    #         url = path
    #
    #     else:
    #
    #         if path.startswith('/'):
    #             path = path[1:]
    #
    #         if not _host_url:
    #             _host_url = self.host_url
    #
    #         url = '{host_url}/{path}'.format(
    #             host_url=_host_url,
    #             path=path,
    #         )
    #
    #     if method == 'get':
    #         response = requests.get(url, **options)
    #
    #         if '_ah/login' in response.content:
    #             raise ValueError('Use api_admin_request to log in as admin')
    #
    #         return response
    #
    #     if method == 'post':
    #         return requests.post(url, **options)

    def request_dict(self, path, options=None, _host_url=None, method='get'):

        response = self.request(path, options, _host_url, method)

        return response.json()

    def admin_request(self, path, options=None, host_url=None):
        """
        Example: response = self.admin_request('/manage/meta')

        :returns Response (from requests lib)
        """

        if not self.admin_cookie:
            response = self.request(
                '_ah/login?email=test_admin%40example.com&admin=True&action=Login',
                {'allow_redirects': False}
            )
            self.admin_cookie = response.cookies['dev_appserver_login']

        admin_options = {'cookies': {'dev_appserver_login': self.admin_cookie}}

        if options:
            admin_options.update(options)

        return self.request(path, admin_options, host_url)

    def isr_lat_lon_string(self):

        return '32.833063,34.980683'

    def local_host_url(self):

        return 'http://localhost'

    # @nottest
    # def api_test_server_url(self):
    #
    #     return self.local_host_url() + ':' + config.api_test_server_port
    #
    # @nottest
    # def dashboard_test_server_url(self):
    #
    #     return self.local_host_url() + ':' + config.dashboard_test_server_port
    #
    # @nottest
    # def history_test_server_url(self):
    #
    #     return self.local_host_url() + ':' + config.history_test_server_port

    # @nottest
    # def users_test_server_url(self):
    #
    #     return self.local_host_url() + ':' + config.users_test_server_port

    def assert_true(self, param, message='Parameter is not True.'):

        if param is True:
            return True

        else:
            raise AssertionError(message)

    def expected_keys(self):
        return [
            'data_valid',
            'country_aqi',
            'country_aqi_prefix',
            'breezometer_description',
            'breezometer_aqi',
            'country_description',
            'country_color',
            'country_name',
            'breezometer_color',
            'key_valid',
            'random_recommendations',
            'dominant_pollutant_canonical_name',
            'dominant_pollutant_description',
            'dominant_pollutant_text',
        ]

    def expected_history_keys(self):
        return ['datetime'] + self.expected_keys()

    # @staticmethod
    # def clear_db_and_seed_data():
    #
    #     api_test_util.request(handlers.clear_db_and_seed_data.path)

    def print_start(self):

        print('\n')

    def print_finish(self):

        print('')

    def debug_print(self, text):

        print('\n\n >>>>>>> Print Output Start >>>>>>> \n')
        print(text)
        print('\n >>>>>>> Print Output End >>>>>>> \n')

        # def print_dict(self, _dict):
        #
        #     self.print_start()
        #     print(DictUtil(_dict).to_pretty_json_string())
        #     self.print_finish()
        #
        # def error_json_convert(dict_obj):
        #
        #     try:
        #         json_obj = json.loads(json.dumps(dict_obj))
        #     except TypeError:
        #         try:
        #             json_obj = json.loads(json.dumps(dict_obj.response()))
        #         except TypeError:
        #             json_obj = False
        #     return json_obj

# api_test_util = TestUtil(host_url=app_config.api_test_server_url)
# api_request = api_test_util.request
# api_request_dict = api_test_util.request_dict

# api_admin_request = api_test_util.admin_request

# app_request = TestUtil().request
