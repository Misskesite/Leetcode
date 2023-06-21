# -*- coding: utf-8 -*-
"""
Created on Sun May 24 21:36:24 2020

@author: liuga
"""

class Solution(object):
    def reverseString(self, s, k):
        n = len(s)
        res = ""
        pos = 0
        while pos < n:
            nx = s[pos: pos+k] #切片法
            res = res + nx[::-1] + s[pos + k : pos + 2*k]
            pos += 2*k
        return res
            
        
