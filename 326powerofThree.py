# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 22:21:50 2020

@author: liuga
"""

class Solution(object):
    def powerofThree(self, n):
        if n <= 0:
            return False
        while n%3 ==0:
            n /= 3
        return n == 1
            
