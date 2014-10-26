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

    def __init__(self, files, folder, letter=None):
        self.files = files
        self.letter = letter
        self.limit = 5

    def is_list(self, elem):
        return isinstance(elem, list)

    def getAllmatchs(self, pattern, list_files):
        l = []
        for filename in list_files:
            if(filename[0] == pattern):
                l += [filename[1:]]
        return l

    def remAllmatchs(self, pattern, list_files):
        l = []
        for filename in list_files:
            if(filename[0] != pattern):
                l += [filename]
        return l


    def tidy_list(self, list_files):
        change = True
        i = 0
        while(change):
            change = False
            len_list = len(list_files)
            while(i < len_list - 1):
                if(self.is_list(list_files[i])):
                    continue
                gc = self.getAllmatchs(list_files[i][0], list_files)
                if(len(gc) > self.limit):
                    list_files = self.remAllmatchs(list_files[i][0], list_files)
                    list_files = [gc] + list_files
                    change = True
                    len_list = len(list_files)
                    i =  0
                i = i + 1
        for i in range(0, len(list_files) - 1):
            if(self.is_list(list_files[i])):
                list_files[i] = self.tidy_list(list_files[i])
        return list_files

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
    files = [ "salut1", "salut2", "salut3", "salut4", "salut5", "salut6", "salut7", "toto1", "toto2", "toto3", "toto4", "toto5", "toto6"]

    tidy = TidyTree(files, folder)
    l = tidy.tidy_list(tidy.files)
    print(l)
