#!/usr/bin/python3
"""
    This module creates a unique FileStorage instance and reloads the objects
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
