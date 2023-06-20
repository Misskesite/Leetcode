# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:01:03 2020

@author: liuga
"""

class Solution(object):
    def poweroffour(self, num):
        if num <= 0:
            return False
        while num % 4 == 0:
            num /= 4
        return num ==1
    
