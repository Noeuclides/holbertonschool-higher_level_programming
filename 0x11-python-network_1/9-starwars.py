#!/usr/bin/python3
'''Search API
'''
import requests
import sys

try:
    data = {'search': sys.argv[1]}
    req = requests.get('https://swapi.co/api/people/', params=data)
    req = req.json()
    result = req.get('results')
    print("Number of results:", len(result))
    for i in range(len(result)):
        print(result[i].get('name'))
except Exception as e:
    pass
