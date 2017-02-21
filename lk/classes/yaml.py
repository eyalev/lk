

import ruamel.yaml as ryaml


def load(string):

    result = ryaml.load(string, ryaml.RoundTripLoader)

    return result


def dump(yaml_object):

    yaml_string = ryaml.dump(yaml_object, Dumper=ryaml.RoundTripDumper)

    return yaml_string
