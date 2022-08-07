#!/usr/bin/python3

"""
Module with test suite for class BaseModel
"""

import unittest
import sys
import os
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    TestSuite for BaseModel
    """
    def test_if_id_exists(self):
        """
        Case to test if id exists upon initialization
        """
        i = BaseModel()
        self.assertTrue(hasattr(i, "id"))

    def test_unique_id_generated(self):
        """
        Test if a unique id is called each time
        """
        i_a = BaseModel()
        i_b = BaseModel()
        self.assertNotEqual(i_a.id, i_b.id)

    def test_str_print_format(self):
        """
        Test for the rirhst object representation
        """
        i = BaseModel()
        self.assertEqual(str(i),
                         "[BaseModel] ({}) {}".format(i.id, i.__dict__))


if __name__ == "__main__":
    unittest.main()
