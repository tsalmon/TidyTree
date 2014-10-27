#!/usr/bin/python

from __future__ import print_function
import sys, os

def warning(*objs):
    print("Warning: ", *objs, file=sys.stderr)

def getListofFiles(folder):
    l = []
    for filename in os.listdir(folder):
        l += [filename]
    return l

class TidyTree:

    def __init__(self, letter=None):
        self.letters = {}
        if(letter != None and letter != ""):
            self.add(letter)

    def add(self, filename):
        key = filename[0]
        if not key in self.letters:
            self.letters[key] = TidyTree(filename[1:])
        else:
            self.letters[key].add(filename[1:])

    def toString(self):
        str = ""
        for letter in self.letters:
            print(letter)
            str = str + " " + letter + "(" + self.letters[letter].toString() + ") \n"
        return str

#init FOLDER path and FILES collection
if __name__ == '__main__':
    if(len(sys.argv) != 2):
        warning("Need a folder name past in argument")
        sys.exit(1);
    folder=sys.argv[1]
    if(not os.path.exists(folder)):
        warning("The folder '" + folder + "' doesn't exist")
        sys.exit(1);

    #files = getListofFiles(folder);
    files = [ "salit1", "salit2", "salit3", "salit4", "salit5", "salit6", "salut1", "salut2", "salut3", "salut4", "salut5", "salut6", "salut7", "toto1", "toto2", "toto3", "toto4", "toto5", "toto6", "m1", "m2", "m3", "m4", "m5", "m6"]

    tidy = TidyTree()
    for i in files:
        tidy.add(i)

    print(tidy.toString())
