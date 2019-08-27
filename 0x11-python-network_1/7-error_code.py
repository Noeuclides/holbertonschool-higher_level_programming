#!/usr/bin/python3
'''Post an email
'''
import requests
from requests.exceptions import HTTPError
import sys

try:
    res = requests.get(sys.argv[1])
    res.raise_for_status()
    print(res.text)
except requests.RequestException:
    print("Error code:", res.status_code)
except BaseException:
    pass
