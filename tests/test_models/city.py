#!/usr/bin/python3
""" This module defines the City class """

from .base_model import BaseModel


class City(BaseModel):
    """ A class representing a city """
    state_id = ""
    name = ""
