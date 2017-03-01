#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import re

class TrieTree(object):
    def __init__(self):
        self.tree = {}

    def add(self, word):
        tree = self.tree

        for char in word:
            if char in tree:
                tree = tree[char]
            else:
                tree[char] = {}
                tree = tree[char]
        tree['exist'] = True

    def search(self, word):
        tree = self.tree
        for char in word:
            if char in tree:
                tree = tree[char]
            else:
                return False
        if "exist" in tree and tree["exist"] == True:
            return True
        else:
            return False


class skip_ost(object):
    def __init__(self):
        self.ost_patt = re.compile(r'\s*(ost|o\.s\.t)\s*(vol|part)*\.*[0-9]*$')
        self.brackets_patt = re.compile('[\\<\\[\\(].*?[\\)\\>\\]]')
        self.ost_keys = []

    def load_ost(self, file):
        fobj = open(file, 'r')
        lines = fobj.readlines()
        fobj.close()
        for line in lines:
            line = line.strip()
            if len(line) <= 0:
                continue
            self.ost_keys.append(line)
    
    def filter_ost(self, name):
        name_bak = self.brackets_patt.sub("", name)
        if len(name_bak) != len(name) and len(name_bak.strip()) != 0:
            return name_bak
        name_bak = self.ost_patt.sub("", name) 
        if len(name_bak) != len(name) and len(name_bak.strip()) != 0:
            return name_bak


        match_key = ""
        max_len = 0
        for key in self.ost_keys:
            if key in name and len(key) > max_len:
                match_key = key
                max_len = len(key)

        name_bak = name.replace(match_key, "")
        if len(name_bak) != 0:
            return name_bak
        return name


if __name__ == "__main__":
    test_ost = skip_ost()
    test_ost.load_ost("../dict/ost.data")
    print test_ost.filter_ost("三生三世十里桃花 电视原声带")
    print test_ost.filter_ost("Who's That Girl (Original Motion Picture Score)".lower())
    print test_ost.filter_ost("Noisette [live]".lower())
    print test_ost.filter_ost("多桑电影原声带".lower())
    print test_ost.filter_ost("东邪西毒 电影音乐展".lower())
