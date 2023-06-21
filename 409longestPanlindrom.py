# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:14:45 2020

@author: liuga
"""
#字典
class Solution(object):
    def longestPanlindrom(self, s):
        h = {}
        for i in s:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        c = 0
        sig = 0
        for i in h:
            c += h[i]//2
            if h[i]%2 != 0:
                sig = 1
        return c*2 + sig
