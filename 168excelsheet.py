# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 13:33:07 2019

@author: liuga
"""

class Solution(object):
    def convertTitle(self,n):
        res = ''
        while n:
            res =  chr((n-1)%26 + 65) + res
            n = (n-1)//26
        return res
