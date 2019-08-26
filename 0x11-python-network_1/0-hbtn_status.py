#!/usr/bin/python3
'''fetch url
'''
import urllib.request as ur

req = ur.Request('https://intranet.hbtn.io/status')
with ur.urlopen(req) as response:
    fetch = response.read()
    print("Body response:")
    print("\t- type:", type(fetch))
    print("\t- content:", fetch)
    print("\t- utf8 content:", fetch.decode('utf-8'))
