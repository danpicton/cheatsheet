#!/usr/bin/env python

"""v0_01.py: Provides interface for templatehandler to pull data from template v0.01 JSON cheat sheet into Python."""

import json
from pprint import pprint

__author__ = "Dan Picton"
__license__ = "GPL3"
__version__ = "0.01"
__maintainer__ = "Dan Picton"
__status__ = "Prototype"

# move to template handler
def get_template_json(json_template_file)
    with open (json_template_file) as data_file:
        return json.load(data_file)

    print "Value: %s" % data["title"]
    print "Value: %s" % data["column"][0]["section"][0]["entries"][0]["displayType"]
