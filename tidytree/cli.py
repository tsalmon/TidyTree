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

def getUniqueKey(dictio):
    if(len(dictio) != 1):
        return False
    for k in dictio:
        return k

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

    # ( len(letter) == 1 ) ? merge keys & repeat : repeat
    def optimize(self):
        new_letters = {}
        aux_key = ""
        l = self.letters

        for letter in l:
            ite = l[letter]
            aux_key = letter
            if(len(ite.letters) == 1):
                while(len(ite.letters) == 1 ):
                    k = getUniqueKey(ite.letters)
                    new_letters[aux_key + k] = ite.letters[k]
                    ite = ite.letters[k]
                    new_letters.pop(aux_key, None)
                    aux_key = aux_key + k
                    ite.optimize()
            else:
                ite.optimize()
                new_letters[letter] = l[letter]
        self.letters = new_letters

    def toString(self):
        ret_str = ""
        for l in self.letters:
            ret_str = ret_str + l + "(" + self.letters[l].toString() + ")"
        return (ret_str)

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
