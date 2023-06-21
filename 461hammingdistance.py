# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:28:28 2020

@author: liuga
"""

class Solution(object):
    def hammingDistance(self,a,b):
        
        return bin(a^b).count(1)

#
class Solution2(object):
    def hammingDistance(self, a, b):
        s = a^b
        res = 0
        while s:
            res += s&1
            s >>= 1
        return res
