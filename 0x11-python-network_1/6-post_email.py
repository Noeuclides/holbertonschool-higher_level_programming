#!/usr/bin/python3
'''Post an email
'''
import requests
import sys

try:
    data = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data)
    print(req.text)
except BaseException:
    pass
