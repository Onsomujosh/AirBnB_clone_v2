#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import os


class test_review(test_basemodel):
    """class test review """

    def __init__(self, *args, **kwargs):
        """init class review """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """place id testing """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """review user_id """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """testing review text attr"""
        new = self.value()
        self.assertEqual(type(new.text), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
