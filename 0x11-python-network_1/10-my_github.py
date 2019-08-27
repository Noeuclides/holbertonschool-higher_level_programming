#!/usr/bin/python3
'''Search API
'''
import requests
from requests.auth import HTTPBasicAuth as hba
import sys

try:
    data = {'username': sys.argv[1], 'password': sys.argv[2]}
    req = requests.get(
        'https://api.github.com/user',
        auth=hba(
            sys.argv[1],
            sys.argv[2]))
    req = req.json()
    print(req.get('id'))

except Exception as e:
    print(e)
