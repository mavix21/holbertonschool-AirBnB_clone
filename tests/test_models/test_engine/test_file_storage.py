#!/usr/bin/python3
"""Test for class FileStorage."""

import unittest
import models


class_path = models.engine.file_storage.FileStorage
instance = class_path()

class TestFileStorage(unittest.TestCase):
    """Class for testing FileStorage docs."""

    def test_doc_module(self):
        """Test moduel documentation."""
        self.assertIsNotNone(models.engine.file_storage.__doc__)

    def test_doc_class(self):
        """Test for class documentation."""
        self.assertIsNotNone(class_path.__doc__)

    def test__file_path(self):
        """Test for class private attribute __file_path."""
        self.assertIsNotNone(class_path.__file_path)

    def test__objects(self):
        """Test for class private attribute __objects."""
        self.assertIs(type(class_path.__objects), list)

    def test_all_method(self):
        """Test for all method"""
        self.assertIsNotNone(instance.all.__doc__)
        self.assertIs(type(instance.all()), dict)

    def test_new_method(self)
        """Test for new method"""
        self.assertIsNotNone(instance.new.__doc__)

    def test_save_method(self)
        """Test for save method"""
        self.assertIsNotNone(instance.save.__doc__)

    def test_reload_method(self)
        """Test for reload method"""
        self.assertIsNotNone(instance.reload.__doc__)
    

if __name__ == '__main__':
    unittest.main
