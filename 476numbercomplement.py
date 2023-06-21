# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:10:35 2020

@author: liuga
"""

class Solution(object):
    def numbercomplement(self, num):
        return num^2 *(len(bin(num))-2)-1