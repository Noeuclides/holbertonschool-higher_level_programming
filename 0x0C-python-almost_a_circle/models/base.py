#!/usr/bin/python3
"""
module that has Base class
"""
import json


class Base:
    """
    class Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON string representation of list_dictionaries
        """
        if list_dictionaries and len(list_dictionaries) != 0:
            return(json.dumps(list_dictionaries))
        else:
            return("[]")

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        listj = []
        f = cls.__name__ + '.json'
        with open(f, 'w', encoding="UTF-8") as file:
            if list_objs:
                for k in list_objs:
                    listj.append(k.to_dictionary())
                file.write(cls.to_json_string(listj))
            else:
                file.write(listj)

    @staticmethod
    def from_json_string(json_string):
        """
        returns list of JSON Sring
        """
        if json_string:
            return(json.loads(json_string))
        else:
            return([])
