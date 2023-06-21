# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:41:14 2020

@author: liuga
"""

class Solution(object):
    def miniMoves(self, nums):
        median = sorted(nums)[len(nums)/2]
        return sum([abs(num-median) for num in nums])