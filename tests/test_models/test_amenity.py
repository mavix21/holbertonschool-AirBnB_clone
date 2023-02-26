#!/usr/bin/python3
"""Test for Amenity class"""

import unittest
import models

class_path = models.amenity.Amenity


class Test_Amenity(unittest.TestCase):
    """Testing Amenity class attributes and documentation"""

    def test_module_doc(self):
        """Testing Amenity module documentation"""
        self.assertIsNotNone(models.Amenity.__doc__)

    def test_class_doc(self):
        """Testing Amenity class documentation"""
        self.assertIsNotNone(class_path.__doc__)

    def test_name_attribute(self):
        """Testing Amenity's name attribute value"""
        self.assertIs(type(class_path.name), str)


if __name__ == '__main__':
    unittest.main
