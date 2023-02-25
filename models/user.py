#!/usr/bin/python3
""" This module defines the User class """

from .base_model import BaseModel


class User(BaseModel):
    """ A class representing a user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
