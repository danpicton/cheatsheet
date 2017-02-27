#!/usr/bin/env python

"""sheetReader.py: Reads JSON cheat sheet into Python object."""

import json
from pprint import pprint

__author__ = "Dan Picton"
__license__ = "GPL3"
__version__ = "0.01"
__maintainer__ = "Dan Picton"
__status__ = "Prototype"

with open('template_0_01.json') as data_file:    
    data = json.load(data_file)

    print "Value: %s" % data["title"]
    print "Value: %s" % data["column"][0]["section"][0]["entries"][0]["displayType"]
