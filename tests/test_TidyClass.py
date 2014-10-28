# -*- coding: UTF-8 -*-

import sys

import unittest

from tidytree.cli import TidyTree

class TestTidyClass(unittest.TestCase):

    #def setUp(self):

    def test_tree(self):
        files = [ "sa", "sb"]
        self.tidy = TidyTree()
        for i in files:
            self.tidy.add(i)

        #test arboresence
        self.assertEquals(self.tidy.letters["s"].letters["a"].letters, {})
        self.assertEquals(self.tidy.letters["s"].letters["b"].letters, {})

        #test Size
        self.assertEquals(len(self.tidy.letters), 1)
        self.assertEquals(len(self.tidy.letters), 1)
