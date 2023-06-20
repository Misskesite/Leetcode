# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 23:14:47 2020

@author: liuga
"""

class Solution(object):
    def findThedifference(self, s, t):
        
        letters = {}
        for c in s:
            if c in letters:
                letters[c] = letters[c]+1
            else:
                letters[c] = 1
        for c in t:
            if c not in letters:
                return c
            letters[c] -= 1
            if letters[c] < 0:
                return c
            
            
