

class Diff(object):

    def __init__(self):
        pass

    def diff(self, source1, source2):

        import difflib
        expected = source1.splitlines(1)
        actual = source2.splitlines(1)

        diff = difflib.unified_diff(expected, actual)

        return ''.join(diff)

