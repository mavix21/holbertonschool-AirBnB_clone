#!/usr/bin/python3
"""Define a class BaseModel to support other classes.
"""

import uuid
from datetime import datetime


class BaseModel:
    """Represent support to other classes.
    """

    def __init__(self, *args, **kwargs):
        """Constructor new instances of class.
        """
        if kwargs:
            for key in kwargs:
                if key != '__class__':
                    setattr(self, key, kwargs[key])
                if hasattr(self, "created_at") and type(self.created_at) is str:
                    self.created_at = datetime.strptime(self.created_at,
                                       '%Y-%m-%dT%H:%M:%S.%f')
                if hasattr(self, "updated_at") and type(self.updated_at) is str:
                    self.updated_at = (datetime.strptime(self.updated_at,
                                       '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the instances.
        """
        str = "[{}] ({}) {}".format(type(self).__name__,
                                    self.id, self.__dict__)
        return (str)

    def save(self):
        """Updates the public instance attributes.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values.
        """
        n_dict = self.__dict__.copy()
        if "created_at" in n_dict:
            n_dict["created_at"] = n_dict["created_at"].isoformat()
        if "updated_at" in n_dict:
            n_dict["updated_at"] = n_dict["updated_at"].isoformat()
        n_dict["__class__"] = self.__class__.__name__
        return (n_dict)
