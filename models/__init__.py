#!/usr/bin/python3
"""
    This module creates a unique FileStorage instance and reloads the objects
"""

from .engine.file_storage import FileStorage
from .base_model import BaseModel
from .user import User


classes = {
    "BaseModel": BaseModel,
    "User": User
}

storage = FileStorage()
storage.reload()
