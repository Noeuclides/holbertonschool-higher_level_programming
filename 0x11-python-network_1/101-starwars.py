#!/usr/bin/python3
'''Search API
'''
import requests
import sys

try:
    all_res = []
    num = 0
    data = {'search': sys.argv[1]}
    req = requests.get('https://swapi.co/api/people/', params=data)
    req = req.json()
    while req.get('next') is not None:
        result = req.get('results')
        num = num + len(result)
        for i in range(len(result)):
            all_res.append(result[i].get('name'))
        req = requests.get(req.get('next'), params=data)
        req = req.json()
    result = req.get('results')
    num = num + len(result)
    for i in range(len(result)):
        all_res.append(result[i].get('name'))
    print("Number of results:", num)
    for people in all_res:
        print(people)
except Exception as e:
    print(e)
