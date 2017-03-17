from lk.classes.local_env import LocalEnv


class URLs(object):

    def __init__(self):
        pass

    def get_url(self, name):

        urls_dict = LocalEnv(name='urls').dict
        url_object = urls_dict.get(name)

        if url_object:
            url = url_object.get('url')
            return url

        else:
            raise ValueError('URL input not found in URLs dictionary.')
