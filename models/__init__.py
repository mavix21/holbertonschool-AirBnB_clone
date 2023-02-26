#!/usr/bin/python3
"""
    This module creates a unique FileStorage instance and reloads the objects
"""

from .engine.file_storage import FileStorage
from .base_model import BaseModel
from .user import User
from .place import Place
from .state import State
from .city import City
from .amenity import Amenity
from .review import Review


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}

storage = FileStorage()
storage.reload()
