#!/usr/bin/python3
"""Test for City class"""

import unittest
import models

class_path = models.city.City


class Test_City(unittest.TestCase):
    """Testing City class attributes and documentation"""

    def test_module_doc(self):
        """Testing City module documentation"""
        self.assertIsNotNone(models.City.__doc__)

    def test_class_doc(self):
        """Testing City class documentation"""
        self.assertIsNotNone(class_path.__doc__)

    def test_name_attribute(self):
        """Testing City's name attribute value"""
        self.assertIs(type(class_path.name), str)

    def test_state_id_attribute(self):
        """Testing City's state_id attribute value"""
        self.assertIs(type(class_path.state_id), str)


if __name__ == '__main__':
    unittest.main
