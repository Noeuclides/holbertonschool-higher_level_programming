#!/usr/bin/python3
"""
module that store file
"""

import json


class FileStorage:
    """
    class to File storage
    """

    __file_path = "object.json"
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
        self.__objects.update({str(BaseModel.id):obj})

    def save(self):
        """
        serialize object
        """
        if self.__objects:
            with open(self.__file_path, 'a') as f:
                json.dump(self.__objects.to_dict(), f)

    def reload(self):
        """
        deserialize JSON file
        """
        if self.__file_path:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
