#!/usr/bin/python3
"""TEST TEST TEST essah sssah saah...
Fine it's working"""


from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import os
import sys
from console import HBNBCommand


class TestConsole(TestCase):
    """test for console"""
    def test0(self):
        """test0"""
        pass

    def test1(self):
        """test1"""
        try:
            os.remove('file.json')
        except:
            pass
    def test2(self):
        """no class name input"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class name missing **")

    def test3(self):
        """input wrong class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create testing")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

    def test4(self):
        """input normal class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        msg = f.getvalue()[:-1]
        self.assertEqual(type(msg), str)

    def test5(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
            HBNBCommand().onecmd('all State')
        msg = f.getvalue()[:-1]
        self.assertTrue("'name': 'California'" in msg)

    def test(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place number_bathrooms=4 price=0.069')
            HBNBCommand().onecmd('all Place')
        msg = f.getvalue()[:-1]
        self.assertTrue("'number_bathrooms': 4" in msg)
        self.assertTrue("'price': 0.069" in msg)
