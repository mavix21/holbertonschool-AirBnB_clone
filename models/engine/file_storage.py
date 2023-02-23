#!/usr/bin/python3
""" This module defines the class FileStorage """

import json
import os


class FileStorage():
    """
    Class that serializes instances to a JSON file and deserializes
    JSON file to instances

    Private Class Attributes:
        __file_path (str):
            path to JSON file (ex: file.json)

        __objects (dict):
            empty dictionary that will store all objects. The format
            will be as follows: <class name>.id (ex: to store a
            BaseModel object with id=12121212, the key will be
            BaseModel.id)

    Public Instance Methods:
        all(self):
            returns the dictionary __objects

        new(self, obj):
            sets in __objects the obj with key <obj class> name.id

        save(self):
            serializes __objects to the JSON file (path: __file_path)

        reload(self):
            deserializes the JSON file to __objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        self.reload()
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id

        Parameters:
            obj (any):
                object to be stored in __objects dictionary

        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects dictionary to JSON string and stores in
        __file_path

        """
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(self.__objects, file)

    def reload(self):
        """ Deserializes the JSON file to __objects

        If the JSON file (__file_path) exists, deserializes the JSON
        file to __objects dictionary. Otherwise, does nothing, and no exception
        should be raised

        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                self.__objects = json.load(file)
