#!/usr/bin/python3
"""Test for State class"""

import unittest
import models

class_path = models.state.State


class Test_State(unittest.TestCase):
    """Testing State class attributes and documentation"""

    def test_module_doc(self):
        """Testing State module documentation"""
        self.assertIsNotNone(models.State.__doc__)

    def test_class_doc(self):
        """Testing State class documentation"""
        self.assertIsNotNone(class_path.__doc__)

    def test_name_attribute(self):
        """Testing State's name attribute value"""
        self.assertIs(type(class_path.name), str)


if __name__ == '__main__':
    unittest.main
