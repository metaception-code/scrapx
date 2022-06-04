import os
from unittest import TestCase
import logging


class BaseScrapTestCase(TestCase):
    

    @classmethod
    def setUpClass(cls):
        cls.setup()

    @classmethod
    def tearDownClass(cls):
        pass 

