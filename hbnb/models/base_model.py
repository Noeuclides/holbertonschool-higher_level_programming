#!/usr/bin/python3
import datetime
import uuid
"""
module that define the BaseModel
"""


class BaseModel:
    """
    BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        constructor method of the BaseModel
        """
        if kwargs:
            for key in kwargs:
                if key is '__class__':
                    setattr(self, str(self.__class__), kwargs[key])
                else:
                    setattr(self, key, kwargs[key])

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()


    def __str__(self):
        """
        string method
        """
        classname = self.__class__.__name__
        return("[{}] ({}) {}".format(classname, self.id, self.__dict__))

    def save(self):
        """
        save updated date method
        """
        self.updated_at = datetime.datetime.now()
        return(self.updated_at.isoformat())

    def to_dict(self):
        """
        return dictionary
        """
        self.__dict__.update({'__class__' : self.__class__.__name__})
        return(self.__dict__)