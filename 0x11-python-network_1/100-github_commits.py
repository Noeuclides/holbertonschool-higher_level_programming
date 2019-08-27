#!/usr/bin/python3
'''Search API
'''
import requests
import sys

try:
    tupl = ()
    l_commit = []
    req = requests.get(
        'https://api.github.com/repos/{}/{}/commits'.format(
            sys.argv[1], sys.argv[2]))
    req = req.json()
    for item in req:
        commit = item.get('commit')
        author = commit.get('author')
        tupl = item.get('sha'), author.get('name'), author.get('date')
        l_commit.append(tupl)
        tupl = ()
        l_commit.sort(key=lambda k: k[2])
        l_commit.reverse()
    for i in range(11):
        print(l_commit[i][0] + ': ' + l_commit[i][1])

except Exception as e:
    print(e)
