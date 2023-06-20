# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 22:17:19 2020

@author: liuga
"""

class Solution(object):
    def validAnagram(self,s,t):
        if len(s) != len(t):
            return False
        a = {}
        b = {}
         
        for c in s:
            a[c] = a.get(c,0) + 1
        for c in t:
            b[c] = b.get(c,0) + 1
        
        return a == b
         
        
