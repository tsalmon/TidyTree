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
#print(tidy.toString())
