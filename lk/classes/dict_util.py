import json


class DictUtil(object):

    def __init__(self, dict):
        self._dict = dict

    @property
    def dict(self):
        return self._dict

    def to_pretty_json_string(self):

        return json.dumps(self.dict, indent=4)


Dict = DictUtil
