#!/usr/bin/python3
"""Test for User class"""

import unittest
from models import User

class_path = models.user.User


class Test_User(unittest.TestCase):
    """Testing User class attributes and documentation"""

    def test_module_doc(self):
        """Testing User module documentation"""
        self.assertIsNotNone(models.User.__doc__)

    def test_class_doc(self):
        """Testing User class documentation"""
        self.assertIsNotNone(class_path.__doc__)

    def test_email_attribute(self):
        """Testing User's email attribute value"""
        self.assertIs(type(class_path.email), str)

    def test_password_attribute(self):
        """Testing User's password attribute value"""
        self.assertIs(type(class_path.password), str)

    def test_first_name_attribute(self):
        """Testing User's first_name attribute value"""
        self.assertIs(type(class_path.first_name), str)

    def test_last_name_attribute(self):
        """Testing User's last_name attribute value"""
        self.assertIs(type(class_path.last_name), str)


if __name__ == '__main__':
    unittest.main
