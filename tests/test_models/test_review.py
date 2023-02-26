#!/usr/bin/python3
"""Test for Review class"""

import unittest
import models

class_path = models.base_model.Review


class Test_Review(unittest.TestCase):
    """Testing Review class attributes and documentation"""

    def test_module_doc(self):
        """Testing Review module documentation"""
        self.assertIsNotNone(models.Review.__doc__)

    def test_class_doc(self):
        """Testing Review class documentation"""
        self.assertIsNotNone(class_path.__doc__)

    def test_place_id_attribute(self):
        """Testing Review's place_id attribute value"""
        self.assertIs(type(class_path.place_id), str)

    def test_user_id_attribute(self):
        """Testing Review's user_id attribute value"""
        self.assertIs(type(class_path.user_id), str)

    def test_text_attribute(self):
        """Testing Review's text attribute value"""
        self.assertIs(type(class_path.text), str)


if __name__ == '__main__':
    unittest.main
