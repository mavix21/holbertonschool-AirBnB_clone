#!/usr/bin/python3
"""Test for Place class"""

import unittest
import models

dummy_obj = models.place.Place()


class Test_Place(unittest.TestCase):
    """Testing Place class attributes and documentation"""

    def test_module_doc(self):
        """Testing Place module documentation"""
        self.assertIsNotNone(models.Place.__doc__)

    def test_class_doc(self):
        """Testing Place class documentation"""
        self.assertIsNotNone(dummy_obj.__class__.__doc__)

    def test_name_attribute(self):
        """Testing Place's name attribute value"""
        self.assertIs(type(dummy_obj.name), str)

    def test_city_id_attribute(self):
        """Testing Place's city_id attribute value"""
        self.assertIs(type(dummy_obj.city_id), str)

    def test_user_id_attribute(self):
        """Testing Place's user_id attribute value"""
        self.assertIs(type(dummy_obj.user_id), str)

    def test_description_attribute(self):
        """Testing Place's description attribute value"""
        self.assertIs(type(dummy_obj.description), str)

    def test_number_rooms_attribute(self):
        """Testing Place's number_rooms attribute value"""
        self.assertIs(type(dummy_obj.number_rooms), int)

    def test_number_bathrooms_attribute(self):
        """Testing Place's number_bathrooms attribute value"""
        self.assertIs(type(dummy_obj.number_bathrooms), int)

    def test_max_guest_attribute(self):
        """Testing Place's max_guest attribute value"""
        self.assertIs(type(dummy_obj.max_guest), int)

    def test_price_by_night_attribute(self):
        """Testing Place's price_by_night attribute value"""
        self.assertIs(type(dummy_obj.price_by_night), int)

    def test_latitude_attribute(self):
        """Testing Place's latitude attribute value"""
        self.assertIs(type(dummy_obj.latitude), float)

    def test_longitude_attribute(self):
        """Testing Place's longitude attribute value"""
        self.assertIs(type(dummy_obj.longitude), float)

    def test_amenity_id_attribute(self):
        """Testing Place's amenity_id attribute value"""
        self.assertIs(type(dummy_obj.amenity_ids), list)


if __name__ == '__main__':
    unittest.main
