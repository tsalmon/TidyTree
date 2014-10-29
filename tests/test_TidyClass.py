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

    def test_EqualsTidy(self, tidy1=None, tidy2=None):
        if(tidy1 != None and tidy1 != None):
            tostring1 = tidy1.toString()
            tostring2 = tidy2.toString()
            self.assertEquals(tostring1, tostring2)
        else:
            self.assertEquals(tidy1, None)
            self.assertEquals(tidy2, None)

    def test_optimize(self):
        test_opti = TidyTree()
        test_opti.letters["a"] = TidyTree()
        test_opti.letters["a"].letters["zerty"] = TidyTree()
        test_opti.letters["a"].letters["zerty"].letters["lol"] = TidyTree()
        test_opti.letters["a"].letters["zerty"].letters["mdr"] = TidyTree()
        test_opti.letters["a"].letters["bc"] = TidyTree()
        test_opti.letters["qwerty"] = TidyTree()

        files = ["azertylol", "azertymdr", "qwerty", "abc"]
        tidy = TidyTree()
        for i in files:
            tidy.add(i)
        tidy.optimize()

        self.test_EqualsTidy(test_opti, tidy)

    def test_jointure(self):
        files = []
        for i in range(1, 10):
            files += ["cli_p" + str(i) + ".py"]
        tidy = TidyTree(files)
        print(tidy.toString())
        #tidy.jointure()

    def test_getFiles(self):
        files = ["azertylol", "azertymdr", "qwerty", "abc"]

        test_opti = TidyTree()
        test_opti.letters["a"] = TidyTree()
        test_opti.letters["a"].letters["zerty"] = TidyTree()
        test_opti.letters["a"].letters["zerty"].letters["lol"] = TidyTree()
        test_opti.letters["a"].letters["zerty"].letters["mdr"] = TidyTree()
        test_opti.letters["a"].letters["bc"] = TidyTree()
        test_opti.letters["qwerty"] = TidyTree()

        test_files = test_opti.getFiles();

        self.assertEquals(sorted(test_files), sorted(files))
