#!/usr/bin/python3
"""TEST TEST TEST essah sssah saah...
Fine it's working"""

import console
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import os
import sys
HBNBCommand = console.HBNBCommand

class TestConsole(TestCase):
    """test for console"""
    def no_class_name(self):
        """no class name input"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class name missing **")

    def wrong_class_name(self):
        """input wrong class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create testing")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

    def create_class(self):
        """input normal class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        msg = f.getvalue()[:-1]
        self.assertEqual(type(msg), str)

    def enter_param(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
            HBNBCommand().onecmd('all State')
        msg = f.getvalue()[:-1]
        self.assertTrue("'name': 'California'" in msg)

    def param_is_number(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place number_bathrooms=4 price=0.069')
            HBNBCommand().onecmd('all Place')
        msg = f.getvalue()[:-1]
        self.assertTrue("'number_bathrooms': 4" in msg)
        self.assertTrue("'price': 0.069" in msg)
