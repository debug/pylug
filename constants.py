import os

# TODO change file to have no logic

__FILE_LOCATION = os.path.dirname(os.path.realpath(__file__))
EXAMPLES = "examples"
BASE_PLUGIN_PATH = os.path.join(__FILE_LOCATION, EXAMPLES)

def enum(**named_values):
    return type('Enum', (), named_values)

BASE_DEPENDENCIES = enum(NONE='none')
