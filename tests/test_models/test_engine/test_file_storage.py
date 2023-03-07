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
        """Test for class private attribute __file_path value"""
        self.assertIsNotNone(instance._FileStorage__file_path)
        self.assertNotIn(" ", instance._FileStorage__file_path)
        with self.assertRaises(Exception):
            instance._FileStorage__file_path = 12345
        with self.assertRaises(Exception):
            instance._FileStorage__file_path = {}



    def test__objects(self):
        """Test for class private attribute __objects."""
        self.assertIs(type(instance._FileStorage__objects), dict)

    def test_all_method_documentation(self):
        """Test for all method documentation"""
        self.assertIsNotNone(instance.all.__doc__)
        self.assertNotIn(" ", instace.all.__doc__)

    def test_all_parameters(self):
        """test for all method parameters"""
        with self.assertRaises(TypeError):
            storage.all(None)
        with self.assertRaises(TypeError):
            storage.all([])

    def test_all_return(self):
        """tests for all method return value"""
        self.assertIs(type(instance.all()), dict)

    def test_new_method_documentaion(self):
        """Tests for new method documentation"""
        self.assertIsNotNone(instance.new.__doc__)
        self.assertNotIn(" ", instace.new.__doc__)

    def test_new_parameters(self):
        """tests for new method parameters"""
        with self.assertRaises(TypeError):
            storage.new(None)
        with self.assertRaises(TypeError):
            storage.new([])

    def test_save_method_documentation(self):
        """Test for save method documentation"""
        self.assertIsNotNone(instance.save.__doc__)
        self.assertNotIn(" ", instace.save.__doc__)

    def test_save_parameters(self):
        """tests for save method parameters"""
        with self.assertRaises(TypeError):
            storage.save(None)
        with self.assertRaises(TypeError):
            storage.save([])

    def test_reload_method(self):
        """Test for reload method documentation"""
        self.assertIsNotNone(instance.reload.__doc__)
        self.assertNotIn(" ", instace.reload.__doc__)

    def test_reload_parameters(self):
        """tests for reload method parameters"""
        with self.assertRaises(TypeError):
            storage.reload(None)
        with self.assertRaises(TypeError):
            storage.reload([])


if __name__ == '__main__':
    unittest.main
