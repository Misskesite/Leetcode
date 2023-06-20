# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 14:57:45 2019

@author: liuga
"""

class Solution(object):
    def titletoNumber(self,s):
        sum = 0
        for c in s:
            sum = sum*26 + ord(c) -64 # - ord("A") + 1
        return sum
