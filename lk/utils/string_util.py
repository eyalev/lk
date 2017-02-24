import json

from utils2.json_util import JSONUtil


class String(object):

    def __init__(self, string):
        self._string = string

    @property
    def string(self):
        return self._string

    def to_dict(self):

        return json.loads(self.string)

    def to_pretty_json_string(self):

        return json.dumps(self.to_odict(), indent=4)

    def to_odict(self):

        json_object = json.loads(self.string)

        if type(json_object) == dict:
            json_odict = JSONUtil(self.string).to_odict()
            return json_odict

        else:
            return json_object

    @property
    def is_url(self):

        from urlparse import urlparse

        # a = 'http://www.cwi.nl:80/%7Eguido/Python.html'
        # b = '/data/Python.html'
        # c = 532
        # d = u'dkakasdkjdjakdjadjfalskdjfalk'

        try:
            result = urlparse(self.string)
            if result.scheme == '':
                return False
            result = True if [result.scheme, result.netloc, result.path] else False

        except ValueError:
            result = False

        return result


def multi_command_template(command_template, separator=False, continue_on_error=False):

    if separator:

        separator_string = "echo; echo '-----------------------------------'; echo"

        replacement = ' &&\n' + separator_string + '\n'

        result = command_template.strip().replace('\n', replacement)

    else:

        if continue_on_error:
            result = command_template.strip().replace('\n', ' ;\n')
        else:
            result = command_template.strip().replace('\n', ' &&\n')

    return result


def text_with_space(text):

    result = '\n{text}\n'.format(text=text)

    return result


def text_with_separators(text, top_space=True):

    if top_space:
        prefix = '\n'
    else:
        prefix = ''

    separator = 90 * '-'
    result = '{prefix}{separator}\n{text}\n{separator}\n'.format(
        prefix=prefix,
        text=text,
        separator=separator
    )

    return result


def text_with_bottom_space(text):

    result = '{text}\n'.format(text=text)

    return result


def print_with_space(text):

    print(text_with_space(text))


def print_with_separators(text, top_space=True):

    print(text_with_separators(text, top_space=top_space))


def print_with_bottom_space(text):

    print(text_with_bottom_space(text))


def print_command(command):

    print_with_space('Command:\n{command}'.format(command=command))


def print_not_implemented():

    print('Option not implemented.')
