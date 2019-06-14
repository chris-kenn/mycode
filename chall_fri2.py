#!/usr/bin/env python3
#
import urllib.request
import json
import webbrowser
import datetime
from pprint import pprint as pp # part of the standard libray

## define some constants
ISSinfo = 'http://api.open-notify.org/iss-now.json' # this is our api to call

## pretty print json
def main():
    """run-time code"""
    issobj = urllib.request.urlopen(ISSinfo) # call the webservice
    nasaread = issobj.read() # parse the JSON blob returned
    convertiss = json.loads(nasaread.decode('utf-8')) # convert json
    print (convertiss['iss_position']['latitude'])
    print (convertiss['iss_position']['longitude'])
    currentDT = datetime.datetime.now()
    print (str(currentDT))

main()

