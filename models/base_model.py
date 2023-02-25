#!/usr/bin/python3
"""Define a class BaseModel to support other classes.
"""

import uuid
from datetime import datetime
import __init__


class BaseModel:
    """ Represent support for other classes. """

    def __init__(self, *args, **kwargs):
        """ Constructor method

        Parameters:
            args (tuple):
                Not intented to be used. If passed, it will be skiped

            kwargs (dict):
                The keys of this dicionary are the name attributes and
                the values are the values of each attribute

        """

        if kwargs:
            """
            This block is intended to RELOAD an object,
            thats why it does not call the storage.new method
            i.e is not added to the dicionary that saves the
            objects created
            """

            del kwargs["__class__"]
            kwargs["created_at"] = datetime.fromisoformat(kwargs["created_at"])
            kwargs["updated_at"] = datetime.fromisoformat(kwargs["updated_at"])
            self.__dict__.update(**kwargs)
        else:
            """
            If not kwargs provided, it means that a new object is being
            created, therefore it must be added to the dictionary
            storage.new
            """

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            __init__.storage.new(self)

    def __str__(self):
        """ String representation of the instances """

        str = "[{}] ({}) {}".format(type(self).__name__,
                                    self.id, self.__dict__)
        return (str)

    def save(self):
        """ Saves with the actual time """

        self.updated_at = datetime.now()
        __init__.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values. """

        n_dict = self.__dict__.copy()
        n_dict["__class__"] = self.__class__.__name__
        if hasattr(self, "created_at"):
            n_dict["created_at"] = n_dict["created_at"].isoformat()

        if hasattr(self, "updated_at"):
            n_dict["updated_at"] = n_dict["updated_at"].isoformat()

        return (n_dict)
