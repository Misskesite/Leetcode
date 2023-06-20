# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:34:09 2020

@author: liuga
"""
#所有binay number的公共前缀 
class Solution(object):
    def bitwise(self, m, n):
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i+=1
        return m << i
