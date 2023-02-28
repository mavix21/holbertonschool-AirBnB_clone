#!/usr/bin/python3
"""Test for base_model module"""

import unittest
import models

class_path = models.base_model.BaseModel
instance = class_path()


class Test_Base_Model(unittest.TestCase):
    """Test class for testing base_model module attributes and methods"""

    def test_base_model_doc(self):
        """Testing base_model module documentation"""
        self.assertIsNotNone(models.base_model.__doc__)

    def test_BaseModel_class_doc(self):
        """Testing BaseModel class documentation"""
        self.assertIsNotNone(class_path.__doc__)

    def test_save_method_doc(self):
        """Testing save method documentation"""
        self.assertIsNotNone(instance.save.__doc__)

    def test_to_dict_method_doc(self):
        """Testing to_dict method documentation"""
        self.assertIsNotNone(instance.to_dict.__doc__)

    def test_to_dict_method(self):
        """Testing to_dict method return type"""
        self.assertIs(type(instance.to_dict()), dict)

    def test_id_value(self):
        """Testing id attribute value"""
        self.assertIs(type(instance.id), str)

    def test_str_method_doc(self):
        """Testing str method documentation"""
        self.assertIsNotNone(instance.__str__.__doc__)

    def test_str_method_(self):
        """Testing str method documentation"""
        self.assertIs(type(instance.__str__), str)

    def test_init_method_doc(self):
        """Testing str method documentation"""
        self.assertIsNotNone(instance.__init__.__doc__)

    def test_init_method_(self):
        """Testing str method documentation"""
        self.assertIs(type(instance.id), str)


if __name__ == '__main__':
    unittest.main
