#!/usr/bin/python3
'''HTTPError
'''
import urllib.request as ur
import urllib.error as uerr
import sys

req = ur.Request(sys.argv[1])
try:
    with ur.urlopen(req) as response:
                print(response.read().decode('utf-8'))
except uerr.HTTPError as e:
    print("Error code:", e.code)
