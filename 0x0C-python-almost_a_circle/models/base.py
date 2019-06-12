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
        if list_dictionaries:
            return(json.dumps(list_dictionaries))
        else:
            return([])                

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        array = []
        f = cls.__name__ + '.json'
        with open(f, 'w') as file:
            if list_objs:
                for k in list_objs:
                    array.append(k.to_dictionary())
                file.write(cls.to_json_string(array))
            else:
                file.dump(array, file)
                
