#!/usr/bin/python3
'''Search API
'''
import requests
import sys

try:
    t_people = ()
    people_film = []
    film_l = []
    num = 0
    data = {'search': sys.argv[1]}
    req = requests.get('https://swapi.co/api/people/', params=data)
    req = req.json()
    while req.get('next') is not None:
        result = req.get('results')
        num = num + len(result)
        for i in range(len(result)):
            people = result[i].get('name')
            film = result[i].get('films')
            for item_f in film:
                req_film = requests.get(item_f)
                req_film = req_film.json()
                film_name = req_film.get('title')
                film_l.append(film_name)
            t_people = people, film_l
            people_film.append(t_people)
            t_people = ()
            film_l = []
        req = requests.get(req.get('next'), params=data)
        req = req.json()

    result = req.get('results')
    num = num + len(result)
    for i in range(len(result)):
        people = result[i].get('name')
        film = result[i].get('films')
        for item_f in film:
            req_film = requests.get(item_f)
            req_film = req_film.json()
            film_name = req_film.get('title')
            film_l.append(film_name)
        t_people = people, film_l
        people_film.append(t_people)
        t_people = ()
        film_l = []
    print("Number of results:", num)
    for tup in people_film:
        print(tup[0])
        for item in tup[1]:
            print("   ", item)
except Exception as e:
    print(e)
