# -*- coding: UTF-8 -*-

import sys, os

import unittest

from tidytree.cli import TidyTree, getListofFiles

class TestTidyClass(unittest.TestCase):

    #def setUp(self):

    def test_tree_1commonNode2branchs(self):
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

    def test_getListOfFile(self, tidy1=None, tidy2=None):
        if(tidy1 == None):
            folder = getListofFiles(".")
            tidy1 = TidyTree()
            for i in folder:
                tidy1.add(i)

        if(tidy2 == None):
            test_folder = ['.coverage',
                            '.git',
                            '.gitignore',
                            'Makefile',
                            'requirements.txt',
                            'tests',
                            'tidytree',
                            'venv']
            tidy2 = TidyTree()
            for j in test_folder:
                tidy2.add(j)

        self.assertEquals(len(tidy1.letters), len(tidy2.letters))

        if(len(tidy1.letters) > 0):
            for i in tidy1.letters:
                self.test_getListOfFile(tidy1.letters[i], tidy2.letters[i])
