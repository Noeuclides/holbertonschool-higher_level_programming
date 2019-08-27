#!/usr/bin/python3
'''Fetch using requests
'''
import requests

req = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type:", type(req.text))
print("\t- content:", req.text)
