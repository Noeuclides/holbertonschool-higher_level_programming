#!/usr/bin/python3
'''Search API
'''
import requests
import sys

try:
    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]
    data = {'q': letter}
    req = requests.post('http://0.0.0.0:5000/search_user', data)
    req = req.json()
    if len(req) == 0:
        print("No result")
    elif type(req) is not dict:
        print("Not a valid JSON")
    else:
        print("[{}] {}".format(req.get('id'), req.get('name')))
except Exception as e:
    print(e)
