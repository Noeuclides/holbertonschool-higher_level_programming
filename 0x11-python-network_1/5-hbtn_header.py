#!/usr/bin/python3
'''response header value
'''
import requests
import sys

try:
    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-Id'))
except BaseException:
    pass
