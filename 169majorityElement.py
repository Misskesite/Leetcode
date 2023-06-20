# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 11:00:42 2019

@author: liuga
"""

class Solution(object):
    def majorirtyElemet(self, nums):
        digits = {}
        for i in nums:
            digits[i] = digits[i].get(i,0) +1
            if digits[i] > len(nums)/2:
                return i
        
        #solution 2
        nums_set = set(nums)
        for i in nums_set:
            if nums.count(i) > len(nums)/2:
                return i