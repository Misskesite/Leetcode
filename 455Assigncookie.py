# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:34:51 2020

@author: liuga
"""

class Solution(object):
    def assigncookie(self, g, s):
        g.sort()
        s.sort()
        sp = 0
        res = 0
        
        for gi in g:
            while sp < len(s) and s[sp] < gi:
                sp += 1
            if sp < len(s) and s[sp] >= gi:
                res += 1
                sp += 1
        return res

