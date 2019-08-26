#!/usr/bin/python3
'''fetch url
'''
import urllib.request as ur
import urllib.parse as up
import sys

try:
    form = {'email': sys.argv[2]}
    datab = up.urlencode(form)
    datab = datab.encode()
    req = ur.Request(sys.argv[1], datab)
    with ur.urlopen(req) as response:
        print(response.read().decode('utf-8'))
except BaseException as e:
    print(e)
