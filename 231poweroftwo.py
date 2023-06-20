# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:44:31 2020

@author: liuga
"""
#n 的二进制表示中仅包含1个1
class Solution(object):
    def powerofTwo(self, n):
        if n <= 0:
            return
        return not (n & (n-1))
