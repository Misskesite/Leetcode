# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:20:19 2020

@author: liuga
"""

class Solution(object):
    def uglynumber(self,num):
        if num <= 0:
            return False
        for i in [2,3,5]:
            while num % i == 0:
                num = num/i
        return True if num == 1 else False
