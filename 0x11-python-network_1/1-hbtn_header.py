#!/usr/bin/python3
'''fetch url
'''
import urllib.request as ur
import sys

req = ur.Request(sys.argv[1])
with ur.urlopen(req) as response:
    print(response.getheader('X-Request-Id'))
