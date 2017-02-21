

class String(object):

    def __init__(self, string):
        self._string = string

    @property
    def string(self):
        return self._string

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


def text_with_separators(text):

    separator = 90 * '-'
    result = '\n{separator}\n{text}\n{separator}\n'.format(text=text, separator=separator)

    return result


def text_with_bottom_space(text):

    result = '{text}\n'.format(text=text)

    return result


def print_with_space(text):

    print(text_with_space(text))


def print_with_separators(text):

    print(text_with_separators(text))


def print_with_bottom_space(text):

    print(text_with_bottom_space(text))
