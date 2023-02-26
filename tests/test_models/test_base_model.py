#!/usr/bin/python3
"""Test for base_model module"""

import unittest
from models.base_model import BaseModel


class Test_Base_Model(unittest.TestCase):
    """Test class for testing base_model module attributes and methods"""

    def test_base_model_doc(self):
        """Testing base_model module documentation"""
        self.assertIsNotNone(models.base_model.__doc__)

    def test_BaseModel_class_doc(self):
        """Testing BaseModel class documentation"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_save_method_doc(self):
        """Testing save method documentation"""
        self.assertIsNotNone(BaseModel.save.__doc__)

    def test_to_dict_method_doc(self):
        """Testing to_dict method documentation"""
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_to_dict_method(self):
        """Testing to_dict method return type"""
        self.assertIs(type(self.model.to_dict()), dict)

    def test_init_doc(self)
        """Testing __init__ method documentation"""
        self.assertIsNotNone(BaseModel.__init__.__doc__)

    def test_id_value(self):
        """Testing id attribute value"""
        self.assertIs(type(self.model.id), str)


if __name__ == '__main__':
    unittest.main
