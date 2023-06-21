# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:08:20 2020

@author: liuga
"""

class Solution(object):
    def checkUpper(self, word):
        return word.lower() == word or word.upper() == word or word.title() == word
        