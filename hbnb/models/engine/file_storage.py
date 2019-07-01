#!/usr/bin/python3
"""
module that store file
"""

import json

class FileStorage:
    """
    class to File storage
    """

    __file_path = "../file.json"
    __objects = {}

    def all(self):
        """
        return dictionary
        """
        return(self.__objects)

    def new(self, obj):
        """
        set dictionary
        """
        __objects.update({str(self.id) : obj})

    def save(self):
        """
        serialize object
        """
        with open(__file_path, 'w') as f:
            json.dump(__objects, f)

    def reload(self):
        """
        deserialize JSON file
        """
        if __file_path:
            with open(__file_path, 'r') as f:
                __objects = json.load(f)